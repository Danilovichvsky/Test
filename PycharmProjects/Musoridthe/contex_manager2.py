class File():
    def __init__(self, filename, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        if self.mode == 'w':
            self.file = open(self.filename, 'w', encoding='utf-8')
        elif self.mode == 'a':
            self.file = open(self.filename, 'a', encoding='utf-8')
        elif self.mode == 'r':
            self.file = open(self.filename, 'r', encoding='utf-8')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('example.txt', 'r') as file:
    # file.write('Всем привет!!')
    data = file.read()
    print(data)
