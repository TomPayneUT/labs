import i2c_driver
import time
import schedule

lcd = i2c_driver.LCD()

def job():
    lcd.lcd_display_string('Wake up')

schedule.every().day.at('13:29').do(job)

while True:
    lcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
    lcd.lcd_display_string(time.strftime('%a %d %b %Y'), 2)
