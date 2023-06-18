from os import strerror


class Loader:
    def __init__(self):
        self.container = []

    def load(self, file_name, parser):

        line = ''

        try:
            for line in open(file_name, 'r'):

                parsed_line = parser.parse(line)

                if parsed_line:
                    self.container.append(parsed_line)

            for i in range(len(self.container) - 1):
                print(self.container[i])

            return self.container

        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))
