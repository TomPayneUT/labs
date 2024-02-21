from gpiozero import Button, TrafficLights, Buzzer

button = Button(21)
#led = LED(25)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    lights.blink()
    buzzer.beep()
    button.wait_for_press()
    lights.off()
    buzzer.off()
    button.wait_for_release()
    