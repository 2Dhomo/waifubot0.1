import asyncio
import re
import time
from html import escape

from telegram import Update, InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler, CallbackContext

from Grabber import user_collection, collection, application

async def inlinequery(update: Update, context: CallbackContext) -> None:
    try:
        query = update.inline_query.query
        offset = int(update.inline_query.offset) if update.inline_query.offset else 0

        characters = []

        if query.startswith('collection.'):
            user_id, *search_terms = query.split(' ')[0].split('.')[1], ' '.join(query.split(' ')[1:])
            if user_id.isdigit():
                user = await user_collection.find_one({'id': int(user_id)})
                if user:
                    all_characters = list({v['id']: v for v in user.get('characters', [])}.values())
                    if search_terms:
                        regex = re.compile(' '.join(search_terms), re.IGNORECASE)
                        all_characters = [character for character in all_characters if
                                          regex.search(character.get('name', '')) or
                                          regex.search(character.get('anime', ''))]
                    characters.extend(all_characters)
        else:
            if query:
                regex = re.compile(query, re.IGNORECASE)
                characters = await collection.find({"$or": [{"name": regex}, {"anime": regex}]}).to_list(length=None)
            else:
                characters = await collection.find({}).to_list(length=None)

        characters = characters[offset:offset + 50]
        if len(characters) > 50:
            characters = characters[:50]
            next_offset = str(offset + 50)
        else:
            next_offset = str(offset + len(characters))

        results = []
        for character in characters:
            global_count = await user_collection.count_documents({'characters.id': character.get('id')})
            anime_characters = await collection.count_documents({'anime': character.get('anime')})

            caption = (
                f"<b>Look At <a href='tg://user?id={user['id']}'>{escape(user.get('first_name', str(user['id'])))}</a>'s Character</b>\n\n"
                f"🌸: <b>{character.get('name', '')}</b>\n"
                f"🖼️: <b>{character.get('anime', '')} ({global_count}/{anime_characters})</b>\n"
                f"<b>{character.get('rarity', '')}</b>\n\n"
                f"<b>🆔️:</b> {character.get('id', '')}"
            ) if query.startswith('collection.') else (
                f"<b>Look At This Character !!</b>\n\n"
                f"🌸:<b> {character.get('name', '')}</b>\n"
                f"🖼️: <b>{character.get('anime', '')}</b>\n"
                f"<b>{character.get('rarity', '')}</b>\n🆔️: <b>{character.get('id', '')}</b>\n\n"
                f"<b>Globally Guessed {global_count} Times...</b>"
            )
            results.append(
                InlineQueryResultPhoto(
                    thumbnail_url=character.get('img_url', ''),
                    id=f"{character.get('id', '')}_{time.time()}",
                    photo_url=character.get('img_url', ''),
                    caption=caption,
                    parse_mode='HTML'
                )
            )

          await update.inline_query.answer(results, next_offset=next_offset, cache_time=5)

    except Exception as e:
        # Log the exception or handle it accordingly
        print(f"Error: {e}")

def inlinequery_handler(update: Update, context: CallbackContext) -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(inlinequery(update, context))

application.add_handler(InlineQueryHandler(inlinequery_handler))
