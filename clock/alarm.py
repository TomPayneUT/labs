import schedule
import subprocess
import time
from gpiozero import Buzzer


def job():
    #subprocess.call(['aplay /home/pi/alarm.wav'], shell=True)
    buzzer = Buzzer(17)
    buzzer.blink()
    

schedule.every().day.at('11:26').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)