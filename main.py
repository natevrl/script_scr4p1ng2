import requests
import telegram_send
import time
import datetime

dattetime = datetime.datetime.now()

r = requests.get(HIDED, HIDED)
centres_disponibles = r.json().get("centres_disponibles", [])

while True:
    for centre in centres_disponibles:
        print("Checking RDV...")
        address = centre.get("metadata")["address"]
        url = centre.get("url")
        app_schedules = centre.get("appointment_schedules", [])
        for schedules in app_schedules:
            schedules_name = schedules.get("name", "")
            if schedules_name != "chronodose":
                continue
            total_doses = schedules.get("total", "")
            if total_doses > 0:
                telegram_send.send(messages=[f"{total_doses} dose disponible à {address} : {url}"])
                telegram_send.send(messages=["Nouveau tour dans 10 minutes..."])
                print(f"{total_doses} dose disponible à {address} : {url}")
    print("Nouveau tour dans 10 minutes...")
    print(dattetime)
    time.sleep(600)



