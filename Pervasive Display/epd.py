import time
from machine import Pin, SPI

class EPD:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy
        self.width = 296  # Update based on your display's resolution
        self.height = 152

        # Initialize GPIO pins
        self.cs.init(Pin.OUT, value=1)
        self.dc.init(Pin.OUT, value=0)
        self.rst.init(Pin.OUT, value=1)
        self.busy.init(Pin.IN)

        # Initialize the display
        self.reset()

    def reset(self):
        self.rst.value(0)
        time.sleep(0.2)
        self.rst.value(1)
        time.sleep(0.2)

    def wait_until_idle(self):
        while self.busy.value() == 0:  # 0 means busy
            time.sleep(0.1)

    def send_command(self, command):
        self.dc.value(0)  # Command mode
        self.cs.value(0)
        self.spi.write(bytearray([command]))
        self.cs.value(1)

    def send_data(self, data):
        self.dc.value(1)  # Data mode
        self.cs.value(0)
        if isinstance(data, int):
            self.spi.write(bytearray([data]))
        else:
            self.spi.write(data)
        self.cs.value(1)

    def init(self):
        self.reset()
        self.wait_until_idle()

        # Add your display initialization sequence here
        self.send_command(0x01)  # POWER_SETTING
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x2B)
        self.send_data(0x2B)

        self.send_command(0x06)  # BOOSTER_SOFT_START
        self.send_data(0x17)
        self.send_data(0x17)
        self.send_data(0x17)

        self.send_command(0x04)  # POWER_ON
        self.wait_until_idle()

        self.send_command(0x00)  # PANEL_SETTING
        self.send_data(0x3F)

        self.send_command(0x30)  # PLL_CONTROL
        self.send_data(0x3C)

        self.send_command(0x61)  # RESOLUTION_SETTING
        self.send_data(0x01)
        self.send_data(0x90)
        self.send_data(0x01)
        self.send_data(0x2C)

        self.send_command(0x82)  # VCM_DC_SETTING
        self.send_data(0x28)

        self.send_command(0x50)  # VCOM_AND_DATA_INTERVAL_SETTING
        self.send_data(0x97)

    def clear(self):
        self.send_command(0x10)
        for _ in range(self.width * self.height // 8):
            self.send_data(0xFF)  # White pixels

        self.send_command(0x13)
        for _ in range(self.width * self.height // 8):
            self.send_data(0xFF)  # White pixels

        self.send_command(0x12)  # DISPLAY_REFRESH
        self.wait_until_idle()

    def display(self):
        self.send_command(0x12)  # DISPLAY_REFRESH
        self.wait_until_idle()

    def text(self, message, x, y, color):
        # Placeholder: Add text rendering logic here
        pass
