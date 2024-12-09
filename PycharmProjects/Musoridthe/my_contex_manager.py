import datetime
import time


class LogWriter:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Open the file in append mode ('a') so new data is added to the end.
        self.file = open(self.filename, 'r+')
        return self

    def add(self, words):

        self.file.write(words + '\n')  # Add a newline after each entry
        self.file.write('------logs------\n'
                        'Data was changed: {}'.format( datetime.datetime.now()))
        print("Data was changed: {}".format(datetime.datetime.now()))

    def get_data_from_file(self):
        data = open(self.filename, 'r', encoding='utf-8')
        for line in data:
            print(line)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.file.close()

try:
    with LogWriter("l.txt") as log:
        log.add("hello world")
        log.get_data_from_file()
except:
    print("error with ADD")
