from os import strerror


class Loader:
    def __init__(self):
        self.container = []

    def load(self, file_name, parser):
        try:
            for line in open(file_name, 'r'):

                parsed_line = parser.parse(line)

                if parsed_line:
                    self.container.append(parsed_line)

            return self.container

        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
