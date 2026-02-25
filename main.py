import requests
from bs4 import BeautifulSoup
import telegram
import os
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

NEAMATI_URL = "https://ffs.india-water.gov.in/"
DIBRUGARH_URL = "https://ffs.india-water.gov.in/"

def get_station_data(station_name):
    response = requests.get(NEAMATI_URL, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    def extract_value(label):
        try:
            start = text.index(label) + len(label)
            return float(text[start:start+20].split()[0])
        except:
            return None

    present = extract_value("Present Water Level")
    warning = extract_value("Warning Level (WL)")
    danger = extract_value("Danger Level (DL)")

    return present, warning, danger

def get_status(current, wl, dl):
    if current is None:
        return "Data not found"
    if current >= dl:
        return "🔴 DANGER LEVEL"
    elif current >= wl:
        return "🟡 WARNING LEVEL"
    else:
        return "🟢 NORMAL"

def send_update():
    n_level, n_wl, n_dl = get_station_data("Neamatighat")
    d_level, d_wl, d_dl = get_station_data("Dibrugarh")

    message = f"""
🌊 Brahmaputra Water Level Update

📍 Neamatighat
Level: {n_level}
Status: {get_status(n_level, n_wl, n_dl)}

📍 Dibrugarh
Level: {d_level}
Status: {get_status(d_level, d_wl, d_dl)}

Updated: {datetime.now().strftime('%d %b %Y %I:%M %p')}
"""

    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_update()
