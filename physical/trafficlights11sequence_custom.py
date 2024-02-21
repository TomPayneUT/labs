from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
#led = LED(25)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    lights.green.on()
    sleep(2.5)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(2)
    lights.off()
    