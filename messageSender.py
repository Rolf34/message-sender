#HELLO FRIENDS
#That a simple script for sending messages to telegram
#how to use:
#1. install telethon - pip install telethon
#2. get your api_id and api_hash from https://my.telegram.org/auth
#3. run the script
#4. enter the recipient username
#5. press enter to start
#input number like this: +380123456789
#you have conect yout client to telegram
import asyncio
import sys
import random
import traceback
from telethon import TelegramClient
import time

api_hash = 'your API'  # Ваш API hash
api_id = 123# API id
phone = 'your number'
defaultRecipient = 'default recipient' 
mesaga = 'Hello world!' 
interval = 1  

async def message(client, chat):
    while True:
        try:
            message = mesaga
            print('Sending message:', message)
            await client.send_message(chat, message)
            await asyncio.sleep(interval) 
        except Exception as e:
            print(f"Error sending message: {e}")
            await asyncio.sleep(5)  

async def main():
    async with TelegramClient('idk', api_id, api_hash) as client:
        print("Connecting to Telegram...")
        await client.connect()  

        if not await client.is_user_authorized():
            print('User not authorized. Please sign in.')
            await client.send_code_request(phone)
            await client.sign_in(phone, input('Enter the code you received: '))

        print("Client connected.")

        recipient = defaultRecipient 
        print('Default recipient:', recipient)
        
        recipient = input('Enter recipient username: ')  
        if not recipient:  
            recipient = defaultRecipient
        
        print('Sending messages to:', recipient)

    print('Press enter to start')

    input()  
    print('Starting... (Press Ctrl+C to stop)')

    await message(client, recipient)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stopped by user') 
    except Exception as e:
        print('Error:', e)
        traceback.print_exc()
    sys.exit(0) 
