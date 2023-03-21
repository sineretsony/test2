class BufferedFileWriter:
    def __init__(self, file_name):
        self.file = open(file_name, "w")
        self.buffer = []

    def write(self, text):
        for s in text:
            self.buffer.append(s)
            if len(self.buffer) == 5:
                temp = ''.join(self.buffer)
                self.file.write(temp)
                self.buffer = []

    def close(self):
        if len(self.buffer) > 0:
            temp = ''.join(self.buffer)
            self.file.write(temp)
            self.buffer = []
        self.file.close()

    def __del__(self):
        if not self.file.closed:
            self.close()


buffered_file = BufferedFileWriter("output.txt")
buffered_file.write("Hell")
buffered_file.write("o, world!")
buffered_file.write(" Hello Python!")
buffered_file.close()

