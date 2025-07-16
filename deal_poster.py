import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

print("✅ Bot started")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL")

if not TELEGRAM_TOKEN or not CHANNEL_ID:
    print("❌ Telegram token or channel missing.")
    exit(1)

def get_latest_deals():
    url = "https://www.indiadesideals.in/"
    print(f"🔗 Scraping {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("div.blog-posts .post-outer")[:3]
        print(f"🛍️ Found {len(articles)} posts")

        deals = []
        for post in articles:
            title_tag = post.select_one(".entry-title a")
            img_tag = post.select_one("img")
            title = title_tag.text.strip()
            link = title_tag['href']
            image = img_tag['src'] if img_tag else None
            msg = f"🔥 *{title}*\n\n🔗 [Buy Now]({link})"
            deals.append((msg, image))
        return deals
    except Exception as e:
        print("❌ Error fetching deals:", e)
        return []

def send_to_telegram(message, image_url):
    try:
        payload = {
            "chat_id": CHANNEL_ID,
            "caption": message,
            "photo": image_url,
            "parse_mode": "Markdown"
        }
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        r = requests.post(url, data=payload)
        print("📤 Sent to Telegram:", r.status_code, r.text)
    except Exception as e:
        print("❌ Error sending message:", e)

def main():
    deals = get_latest_deals()
    if not deals:
        print("⚠️ No deals to post.")
    for msg, img in deals:
        print("📨 Posting:", msg[:60])
        send_to_telegram(msg, img)

if __name__ == "__main__":
    main()
