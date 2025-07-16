import os
import requests
import time

print("✅ Starting Deal Sender...")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL")

if not TELEGRAM_TOKEN or not CHANNEL_ID:
    print("❌ Missing Telegram credentials.")
    exit(1)

deals = [
    {
        "title": "🔥 Fire TV Stick Lite – 50% Off!",
        "link": "https://www.amazon.in/dp/B08C1W5N87",
        "image": "https://m.media-amazon.com/images/I/41QJ1G8CPzL._SX342_.jpg"
    },
    {
        "title": "💥 Boat Rockerz 255 Pro+ – Wireless Earphones",
        "link": "https://www.amazon.in/dp/B08TH8SNBN",
        "image": "https://m.media-amazon.com/images/I/61WnYQXcQ6L._SL1500_.jpg"
    },
    {
        "title": "⚡ Realme Narzo 60x 5G – Flat ₹2,000 Off",
        "link": "https://www.amazon.in/dp/B0CHGV3V2Y",
        "image": "https://m.media-amazon.com/images/I/41quKFc2eCL._SX300_SY300_QL70_FMwebp_.jpg"
    },
    {
        "title": "🧴 NIVEA Body Lotion, 400ml – 30% Off",
        "link": "https://www.amazon.in/dp/B07Z8V3S1F",
        "image": "https://m.media-amazon.com/images/I/61YmJodm7VL._SL1500_.jpg"
    },
    {
        "title": "🖥️ Logitech Wireless Mouse – 40% Off",
        "link": "https://www.amazon.in/dp/B003NR57BY",
        "image": "https://m.media-amazon.com/images/I/61LtuGzXeaL._SL1500_.jpg"
    }
]

def send_photo_or_text(msg, image_url):
    photo_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    text_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    # Send Photo
    payload = {
        "chat_id": CHANNEL_ID,
        "caption": msg,
        "photo": image_url,
        "parse_mode": "Markdown"
    }
    response = requests.post(photo_url, data=payload)

    if response.status_code != 200:
        print(f"⚠️ Failed to send image. Sending text instead. Status: {response.status_code}")
        # Send text fallback
        payload = {
            "chat_id": CHANNEL_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }
        r = requests.post(text_url, data=payload)
        print(f"📨 Text fallback sent. Status: {r.status_code}")
    else:
        print("✅ Photo sent successfully.")

# Loop to send all deals
for deal in deals:
    msg = f"*{deal['title']}*\n\n🔗 [Buy Now]({deal['link']})"
    print(f"➡️ Sending: {deal['title']}")
    send_photo_or_text(msg, deal["image"])
    time.sleep(3)  # wait 3 seconds to avoid Telegram limits
