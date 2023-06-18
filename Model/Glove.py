from Model.Equipment import Equipment


class Glove(Equipment):

    def __init__(self, sec_lvl, quantity, size):
        super().__init__(sec_lvl, quantity)
        self.size = size

    def __str__(self):
        return "Glove {Security Level: " + str(self.sec_lvl) + ", Quantity: " + str(self.quantity) + \
            ", Size:" + str(self.size) + '}'
