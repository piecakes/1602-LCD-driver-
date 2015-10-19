from LCD_1602 import lcddriver
import time

def main():
        lcd = lcddriver.lcd()
        lcd.lcd_display_string("Hello world!", 1)
        lcd.lcd_display_string("My name is Pi", 2)
        time.sleep(30)

if __name__ == "__main__":
    main()




