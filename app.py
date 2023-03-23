import requests
import schedule
import time

def check_website():
    url = "https://eddyded.glitch.me" # The URL of the page you want to monitor
    response = requests.get(url)
    if response.status_code == 200: print("Online")
    else: print("Offline")

def execute():

    try:
        # Schedule the task to run every 5 seconds
        schedule.every(0.05).minutes.do(check_website)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        time.sleep(10)
        execute()
        pass

if __name__ == '__main__':
    execute()