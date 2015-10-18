from LCD_1602 import lcddriver
from time import *

def main():
    lcd = lcddriver.lcd()
    lcd.backlight(0)
    lcd.lcd_display_string("Hello world!", 1)
    lcd.lcd_display_string("My name is Pi", 2)

if __name__ == "__main__":
    main()

