from gpiozero import Button, TrafficLights

button = Button(21)
#led = LED(25)
lights = TrafficLights(25, 8, 7)

while True:
    button.wait_for_press()
    lights.on()
    button.wait_for_release()
    lights.off()
    