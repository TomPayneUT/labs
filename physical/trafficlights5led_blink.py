from gpiozero import Button, LED

button = Button(21)
led = LED(25)

while True:
    #led.blink()
    #led.blink(2, 2)
    #led.blink(0.5, 0.5)
    led.blink(0.1, 0.2)
    button.wait_for_press()
    led.off()
    button.wait_for_release()
    