import os
import requests
from bs4 import BeautifulSoup

print("✅ Bot started")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL")

if not TELEGRAM_TOKEN or not CHANNEL_ID:
    print("❌ Telegram token or channel missing.")
    exit(1)

def get_latest_deals():
    url = "https://www.desidime.com/groups/loot-deals"
    print(f"🔗 Scraping {url}")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        deals = []

        posts = soup.select("div[data-controller='post-list'] article")[:3]
        print(f"🛍️ Found {len(posts)} loot deals")

        for post in posts:
            title_tag = post.select_one("h1 a, h2 a")
            link = "https://www.desidime.com" + title_tag.get("href", "") if title_tag else ""
            title = title_tag.get_text(strip=True) if title_tag else "No title"

            image_tag = post.select_one("img")
            image_url = image_tag.get("src") if image_tag else None

            message = f"🔥 *{title}*\n\n🔗 [View Deal]({link})"
            deals.append((message, image_url))

        return deals
    except Exception as e:
        print("❌ Error fetching deals:", e)
        return []

def send_to_telegram(message, image_url=None):
    try:
        if image_url:
            payload = {
                "chat_id": CHANNEL_ID,
                "caption": message,
                "photo": image_url,
                "parse_mode": "Markdown"
            }
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        else:
            payload = {
                "chat_id": CHANNEL_ID,
                "text": message,
                "parse_mode": "Markdown"
            }
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        r = requests.post(url, data=payload)
        print("📤 Sent to Telegram:", r.status_code, r.text)
    except Exception as e:
        print("❌ Error sending to Telegram:", e)

def main():
    deals = get_latest_deals()
    if not deals:
        print("⚠️ No deals to post.")
    for msg, img in deals:
        print("📨 Posting:", msg[:60])
        send_to_telegram(msg, img)

if __name__ == "__main__":
    main()
