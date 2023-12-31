from Model.Glove import Glove


class GloveParser():
    st = []

    def __init__(self, customerStorage):
        self.c_st = customerStorage

    def parse(self, line):

        data = line.split(';')

        if data[0] == "Glove":
            self.c_st.append(data[4] + ' ' + data[5])

            return Glove(int(data[1]), int(data[2]), data[3])
        else:
            return None
