from machine import SPI, Pin

spi = SPI(0, baudrate=2000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

print("Testing SPI communication...")
try:
    spi.write(b'\xAA')  # Send some test data
    print("SPI communication successful.")
except Exception as e:
    print("SPI test failed:", e)
