import os
import requests
import time
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

NEAMATI_DANGER = 85.90
DIBRUGARH_DANGER = 105.00

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def get_water_levels():
    # Placeholder values (we will connect real data later)
    neamati_level = 84.5
    dibrugarh_level = 103.2
    return neamati_level, dibrugarh_level

while True:
    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    neamati, dibrugarh = get_water_levels()

    message = f"""
Hourly Update ({now})

Neamati: {neamati} m
Dibrugarh: {dibrugarh} m
"""

    send_message(message)

    if neamati >= NEAMATI_DANGER:
        send_message("⚠ WARNING: Neamati crossed danger level!")

    if dibrugarh >= DIBRUGARH_DANGER:
        send_message("⚠ WARNING: Dibrugarh crossed danger level!")

    time.sleep(3600)
