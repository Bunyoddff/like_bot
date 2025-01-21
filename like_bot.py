from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import os
from telegram import Update

like_sanagich=0
dislike_sanagich=0

# Get the bot token from environment variables
TOKEN = os.getenv('TOKEN')

def bronnarsa_qaytaradi(update: Update, context: CallbackContext):
    ismi = update.message.from_user.first_name
    update.message.reply_text(f'{ismi}. Like yoki Dislike yuboring!')

def likedislike(update: Update, context: CallbackContext):
    global like_sanagich,dislike_sanagich
    if update.message.text=='👎':
        dislike_sanagich+=1
        update.message.reply_text(f'Dislekelar soni {dislike_sanagich} ga teng,Likelar soni {like_sanagich} ga teng')
    if update.message.text=='👍':
        like_sanagich+=1
        update.message.reply_text(f'Dislekelar soni {dislike_sanagich} ga teng,Likelar soni {like_sanagich} ga teng')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add handlers
dispatcher.add_handler(CommandHandler('stop', bronnarsa_qaytaradi))
dispatcher.add_handler(MessageHandler(filters=None,callback=likedislike))
# Start the bot
updater.start_polling()

# Run the bot until you stop it
updater.idle()
