from machine import Pin, SPI
from epd import EPD

# Configure SPI interface (SPI0)
spi = SPI(0, baudrate=2000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

# Define control pins
cs = Pin(17, Pin.OUT)
dc = Pin(12, Pin.OUT)
rst = Pin(11, Pin.OUT)
busy = Pin(13, Pin.IN)

# Initialize the display
print("Initializing EPD...")
epd = EPD(spi, cs, dc, rst, busy)

# Test initialization and clearing
print("EPD Initialization started...")
epd.init()
print("EPD Initialization completed.")

print("Clearing EPD...")
epd.clear()
print("EPD cleared.")


##for checking the behavior of busy pin
# print("Checking BUSY pin...")
# while busy.value() == 1:
#     print("Display is busy...")

