class EPD:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy
        self.width = 296  # Update to your display's resolution
        self.height = 152

    def init(self):
        # Initialization sequence
        pass

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
