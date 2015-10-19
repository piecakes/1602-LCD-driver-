from LCD_1602 import lcddriver
import time

def main():
    while True:
        lcd = lcddriver.lcd()
        lcd.backlight(0)
        lcd.lcd_display_string("Hello world!", 1)
        lcd.lcd_display_string("My name is Pi", 2)
        time.sleep(1)
        lcd.lcd_clear()
        time.sleep(1)

if __name__ == "__main__":
    main()

