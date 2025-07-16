import os
import requests

# Dummy message and image
message = "🔥 *Test Deal Alert!*\n\nThis is a test message from the bot.\n\n🔗 [Check Now](https://example.com)"
image_url = "https://via.placeholder.com/300x200.png?text=Test+Deal"

# Telegram credentials
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL")

if not TELEGRAM_TOKEN or not CHANNEL_ID:
    print("❌ Missing Telegram credentials.")
    exit(1)

# Send message to Telegram
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
payload = {
    "chat_id": CHANNEL_ID,
    "caption": message,
    "photo": image_url,
    "parse_mode": "Markdown"
}

response = requests.post(url, data=payload)
print("📤 Sent test message:", response.status_code, response.text)
