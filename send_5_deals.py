import os
import requests
import time

print("✅ Starting...")

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

# Send each deal
for i, deal in enumerate(deals, 1):
    try:
        msg = f"*{deal['title']}*\n\n🔗 [Buy Now]({deal['link']})"
        payload = {
            "chat_id": CHANNEL_ID,
            "caption": msg,
            "photo": deal["image"],
            "parse_mode": "Markdown"
        }
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        r = requests.post(url, data=payload)
        print(f"✅ ({i}) Sent → Status: {r.status_code}")
        time.sleep(1)  # small delay
    except Exception as e:
        print(f"❌ Error sending deal {i}:", e)
