import requests
TOKEN = "8004843742:AAHm-3TXXS5hkbdtWt6byclIDz58XpvXvHk"
CHAT_ID = "7982846707"
MESSAGE = "047超會吃然後跳舞很好看"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": MESSAGE}
response = requests.post(url, json=payload)
print(response.json())

