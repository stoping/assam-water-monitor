import requests
from bs4 import BeautifulSoup
from telegram import Bot
import os
from datetime import datetime
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def get_station_data():
    url = "https://ffs.india-water.gov.in/"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    return text[:500]  # temporary check

async def send_update():
    data = get_station_data()

    message = f"""
🌊 Water Level Update

Sample Data:
{data}

Updated: {datetime.now().strftime('%d %b %Y %I:%M %p')}
"""

    await bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    asyncio.run(send_update())
