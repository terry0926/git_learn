import requests
TOKEN = "8004843742:AAHm-3TXXS5hkbdtWt6byclIDz58XpvXvHk"
CHAT_ID = "7982846707"
MESSAGE = "047terry"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": MESSAGE}
response = requests.post(url, json=payload)
print(response.json())
