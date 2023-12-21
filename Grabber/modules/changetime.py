from pymongo import  ReturnDocument

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from Grabber import application 
from Grabber import user_totals_collection

async def change_time(update: Update, context: CallbackContext) -> None:
    
    user = update.effective_user
    chat = update.effective_chat

    try:
        member = await chat.get_member(user.id)
        if member.status not in ('administrator', 'creator'):
            await update.message.reply_text('You do not have permission to use this command.')
            return

        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Incorrect format. Please use: /changetime NUMBER')
            return

        
        new_frequency = int(args[0])
        if new_frequency < 100:
            await update.message.reply_text('The message frequency must be greater than or equal to 100.')
            return
        
        new_frequency = int(args[0])
        if new_frequency > 10000:
            await update.message.reply_text('Thats too much  buddy.use below 10000')
            return

        
        chat_frequency = await user_totals_collection.find_one_and_update(
            {'chat_id': str(chat.id)},
            {'$set': {'message_frequency': new_frequency}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

        await update.message.reply_text(f'Successfully changed character appearance frequency to every {new_frequency} messages.')
    except Exception as e:
        await update.message.reply_text('Failed to change character appearance frequency.')


application.add_handler(CommandHandler("changetime", change_time, block=False))
