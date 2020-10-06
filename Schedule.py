import schedule
from datetime import datetime
from time import sleep
from threading import Thread

def job():
    print("Somebody call me?\n")

def schedule_checker():
    print (datetime.now())
    while True:
        schedule.run_pending() 
        sleep(1)

schedule.every().day.at("12:15").do(job)
Thread(target=schedule_checker).start() 
