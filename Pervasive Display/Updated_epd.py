#updated epd driver
class EPD:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy
        self.width = 296  # Update to match your display resolution
        self.height = 152

    def init(self):
        # Reset the display
        self.rst.value(0)
        time.sleep(0.1)
        self.rst.value(1)
        time.sleep(0.1)

        # Initialization commands
        self.send_command(0x01)  # Power setting
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x2B)
        self.send_data(0x2B)
        self.send_command(0x06)  # Booster soft start
        self.send_data(0x17)
        self.send_data(0x17)
        self.send_data(0x17)
        self.send_command(0x04)  # Power on
        while self.busy.value() == 1:
            pass
        self.send_command(0x00)  # Panel setting
        self.send_data(0xCF)

    def send_command(self, command):
        self.dc.value(0)
        self.cs.value(0)
        self.spi.write(bytearray([command]))
        self.cs.value(1)

    def send_data(self, data):
        self.dc.value(1)
        self.cs.value(0)
        self.spi.write(bytearray([data]))
        self.cs.value(1)

    def update_display(self):
        self.send_command(0x22)
        self.send_data(0xC7)
        self.send_command(0x20)
        while self.busy.value() == 1:
            pass

    def display_frame(self, frame_buffer):
        self.send_command(0x24)
        for byte in frame_buffer:
            self.send_data(byte)
        self.update_display()

    def clear(self):
        frame_buffer = [0xFF] * (self.width * self.height // 8)
        self.display_frame(frame_buffer)

    def sleep(self):
        self.send_command(0x10)  # Enter deep sleep
        self.send_data(0x01)