import os
import requests

print("✅ Starting test...")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL")

if not TELEGRAM_TOKEN or not CHANNEL_ID:
    print("❌ Missing Telegram credentials.")
    exit(1)

message = "👋 *Hello from GitHub bot!*"

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": message,
    "parse_mode": "Markdown"
}

response = requests.post(url, data=payload)
print("📤 Sent message:", response.status_code, response.text)
