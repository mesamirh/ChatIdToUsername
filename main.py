import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.error import BadRequest
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
token = os.getenv('BOT_TOKEN')
owner_id = os.getenv('OWNER_ID')

def print_header():
    header = "\033[1;34m" + "=" * 40 + "\033[0m\n" + \
             "\033[1;32m" + " " * 10 + "M E S A M I R H" + " " * 10 + "\033[0m\n" + \
             "\033[1;34m" + "=" * 40 + "\033[0m"
    print(header)

async def send_confirmation_message(context: CallbackContext):
    try:
        owner_chat = await context.bot.get_chat(owner_id)
        owner_first_name = owner_chat.first_name
        message = f"Hello {owner_first_name} sir, I'm awake!"
        await context.bot.send_message(chat_id=owner_id, text=message)
    except Exception as e:
        pass

async def animate_loading():
    animation = ['|', '/', '-', '\\']
    for i in range(10):
        await asyncio.sleep(0.5)
        print(f"\rLoading {animation[i % len(animation)]}", end='')

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Send me a chat ID or a username, and I will fetch information about that chat.')

async def get_chat_info(update: Update, context: CallbackContext):
    input_text = update.message.text.strip()
    chat_id_or_username = input_text

    try:
        chat = await context.bot.get_chat(chat_id_or_username)
    except BadRequest:
        await update.message.reply_text('Invalid chat ID or username. Please provide a valid one.')
        return
    except Exception as e:
        if 'bot cannot access the user' in str(e):
            await update.message.reply_text("I can't access this personal account. Please ensure the user has interacted with me before.")
        else:
            await update.message.reply_text(f"An error occurred: {str(e)}")
        return

    wait_message = await update.message.reply_text('Fetching chat info...')
    try:
        await animate_loading()
        await context.bot.edit_message_text(
            text=f'Chat info:\nID: {chat.id}\nTitle: {chat.title}\nType: {chat.type}\nUsername: @{chat.username if chat.username else "N/A"}',
            chat_id=wait_message.chat_id,
            message_id=wait_message.message_id
        )
    except BadRequest as e:
        await context.bot.edit_message_text(
            text=f'Error: {e.message}',
            chat_id=wait_message.chat_id,
            message_id=wait_message.message_id
        )

def main():
    print_header()
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_chat_info))

    def schedule_confirmation_message():
        try:
            application.job_queue.run_once(send_confirmation_message, 0)
        except Exception as e:
            application.job_queue.run_once(send_confirmation_message, 5)

    application.job_queue.run_once(send_confirmation_message, 1)

    application.run_polling()

if __name__ == "__main__":
    main()