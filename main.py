from stock_utils import get_nabil_price
import requests

# 🔁 Telegram Bot credentials
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# Run logic
price = get_nabil_price()
send_telegram_message(f"NABIL Price Alert: {price}")
