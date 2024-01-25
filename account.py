import json
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import time

# Replace 'API_ID' and 'API_HASH' with your Telegram API credentials
api_id = '27693492'
api_hash = 'e9c1340a722315dfc403874baf05af98'

# Replace 'PHONE_NUMBER' with your registered phone number
phone_number = '+998337179075'

# Path to the session file (it will be created if it doesn't exist)
session_path = 'bi  o_changer'

# Path to the JSON file containing bios
bios_file_path = './enterpreneur-quotes.json'

def  load_bios():
    with open(bios_file_path, 'r') as file:
        return json.load(file)
    
def set_bio(client, bio):
    about_text = bio.get("text", "")
    client(UpdateProfileRequest(about=about_text))

with TelegramClient(session_path, api_id, api_hash) as client:
    # If not authorized, send the code to your phone and enter it here
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))

    # Replace 'INTERVAL_SECONDS' with the interval you want (in seconds)
    interval_seconds = 3600  # 1 hour

    while True:
        bios = load_bios()
        for bio in bios:
            set_bio(client, bio)
            time.sleep(interval_seconds)
