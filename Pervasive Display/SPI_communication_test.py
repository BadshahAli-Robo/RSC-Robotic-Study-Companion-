from machine import SPI, Pin

spi = SPI(0, baudrate=2000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

print("Testing SPI communication...")
try:
    spi.write(b'\xAA')  # Send some test data
    print("SPI communication successful.")
except Exception as e:
    print("SPI test failed:", e)




# just for knowledge
# When you're using an e-paper display with SPI communication:
# 
# Master (RPi Pico) sends commands and pixel data to the display via MOSI.
# The display might send status information (e.g., "I'm busy") back to the Pico via MISO.
# Communication is synchronized by the clock signal (SCK), which the Pico generates.
# The CS pin ensures that the correct device on the SPI bus is active during communication.
