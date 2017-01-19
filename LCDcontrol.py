import Adafruit_CharLCD as LCD
import time

lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 13
lcd_backlight = 4

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)

def writeMessage(message):
  lcd.message(message)

def writeClear(message):
  lcd.clear()
  #time.sleep(3)
  lcd.message(message)

def createChar(position,char):
  lcd.create_char(position, char)

def createCustomChar():
  createChar(1,[0x0,0x8,0xc,0xe,0xc,0x8,0x0,0x0])
  createChar(2,[0x0,0x2,0x6,0xe,0x6,0x2,0x0,0x0])

def clear():
  lcd.clear()

def setBacklight(setLight):
  lcd.set_backlight(setLight)

def enableDisplay(enable):
  lcd.enable_display(enable)

def delayMicro(microseconds):
  lcd._delay_microseconds(microseconds)
