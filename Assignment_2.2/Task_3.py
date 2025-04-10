class FixedBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []

    def add(self, item):
        if len(self.buffer) == self.size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def get(self):
        return self.buffer

# Пример:
buf = FixedBuffer(3)
for i in range (1, 5):
    buf.add(i)
    print(buf.get())  # [2, 3, 4] в конце
