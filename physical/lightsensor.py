from gpiozero import LightSensor, Buzzer

#Our kit does not have the right capacitor for this lab
ldr = LightSensor(18, charge_time_limit=0.1)


while True:
    print(ldr.value, ldr.is_active)
    #ldr.wait_for_light()
    #print('It is light')
    ldr.wait_for_dark()
    print('It is dark')