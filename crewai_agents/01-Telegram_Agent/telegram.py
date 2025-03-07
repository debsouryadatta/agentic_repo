from crew import crew
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Global variables
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}/"
FILE_URL = f"https://api.telegram.org/file/bot{TOKEN}/"
last_update_id = 0

# Basic API functions
def send_request(method, params=None, files=None):
    """Send a request to the Telegram API"""
    url = f"{API_URL}{method}"
    response = requests.post(url, data=params, files=files)
    
    if response.status_code != 200:
        print(f"Error with {method}: {response.text}")
        return {}
        
    return response.json()

def get_updates():
    """Get new messages from Telegram"""
    global last_update_id
    
    params = {
        'offset': last_update_id + 1,
        'timeout': 30
    }
    
    result = send_request('getUpdates', params)
    updates = result.get('result', [])
    
    if updates:
        last_update_id = updates[-1]['update_id']
        
    return updates

def send_message(chat_id, text):
    """Send a text message to a chat"""
    params = {
        'chat_id': chat_id,
        'text': text
    }
    
    return send_request('sendMessage', params)

def send_voice(chat_id, voice_path):
    """Send a voice message to a chat"""
    params = {'chat_id': chat_id}
    
    with open(voice_path, 'rb') as voice:
        files = {'voice': voice}
        return send_request('sendVoice', params, files)

def download_voice(file_id, save_dir="voice_messages"):
    """Download a voice message from Telegram"""
    # Get file path on Telegram servers
    file_info = send_request('getFile', {'file_id': file_id})
    
    if not file_info.get('ok'):
        print(f"Error getting file info: {file_info}")
        return ""
    
    file_path = file_info['result']['file_path']
    download_url = f"{FILE_URL}{file_path}"
    
    # Download the file
    response = requests.get(download_url)
    if response.status_code != 200:
        print(f"Error downloading file: {response.status_code}")
        return ""
    
    # Create directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Save the file
    local_file_path = os.path.join(save_dir, f"{file_id}.ogg")
    with open(local_file_path, 'wb') as f:
        f.write(response.content)
    
    return local_file_path

# Message handlers
def handle_text_message(chat_id, text):
    """Handle incoming text messages"""
    print(f"Received text: {text}")
    crew.kickoff()
    send_message(chat_id, f"You said: {text}")

def handle_voice_message(chat_id, file_id):
    """Handle incoming voice messages"""
    print(f"Received voice message with file_id: {file_id}")
    
    # Download the voice message
    voice_path = download_voice(file_id)
    
    if voice_path:
        send_message(chat_id, "I received your voice message!")
        send_voice(chat_id, voice_path)  # Echo the voice message back

def process_update(update):
    """Process a single update from Telegram"""
    message = update.get('message')
    if not message:
        return
    
    chat_id = message['chat']['id']
    
    # Handle text messages
    if 'text' in message:
        handle_text_message(chat_id, message['text'])
    
    # Handle voice messages
    elif 'voice' in message:
        handle_voice_message(chat_id, message['voice']['file_id'])

def main():
    """Main function to run the Telegram bot"""
    if not TOKEN:
        print("Please set the TELEGRAM_BOT_TOKEN environment variable")
        return
    
    print("Bot started. Press Ctrl+C to stop.")
    
    try:
        while True:
            updates = get_updates()
            
            for update in updates:
                process_update(update)
            
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    main()
