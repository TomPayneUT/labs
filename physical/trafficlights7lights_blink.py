from gpiozero import Button, TrafficLights

button = Button(21)
#led = LED(25)
lights = TrafficLights(25, 8, 7)

while True:
    lights.blink()
    button.wait_for_press()
    lights.off()
    button.wait_for_release()
    