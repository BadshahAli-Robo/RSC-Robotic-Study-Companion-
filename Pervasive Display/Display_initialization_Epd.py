import time
from machine import SPI, Pin
from epd import EPD  # Assuming you named the updated driver as epd.py

# SPI bus configuration
spi = SPI(1, baudrate=2000000, polarity=0, phase=0)

# EPD pins configuration
cs = Pin(17, Pin.OUT)     # Panel CS
dc = Pin(12, Pin.OUT)     # Data/Command
rst = Pin(11, Pin.OUT)    # Reset
busy = Pin(13, Pin.IN)    # Busy

# Create EPD instance
epd = EPD(spi, cs, dc, rst, busy)

# Initialize display
epd.init()
print("EPD initialized successfully")