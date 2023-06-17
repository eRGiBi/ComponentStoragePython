from os import strerror


class Loader:
    def __init__(self):
        self.__container = []

    def load(self, file_name, parser):

        line = ''

        try:
            stream = open(file_name, mode='r', encoding=None)

        except Exception as exc:
            print("Cannot open the file:", strerror(exc.errno))
