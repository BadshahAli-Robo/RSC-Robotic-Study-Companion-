from machine import Pin, SPI
import epd  
import time
spi = SPI(0, baudrate=2000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
epd_display = epd.EPD(spi, cs=Pin(17), dc=Pin(12), rst=Pin(11), busy=Pin(13))

epd_display.init()

epd_display.clear()

epd_display.display_text("Hello, World!", x=10, y=50)

time.sleep(5)

epd_display.sleep()
