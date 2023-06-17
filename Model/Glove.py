from Model.Equipment import Equipment


class Glove(Equipment):

    def __init__(self, sec_lvl,  quantity, size, ):
        super().__init__(sec_lvl, quantity)
        self.size = size

    def __str__(self) -> str:
        return "Glove{ Security Level: " + super().get_sec_lvl() + ", Quantity: " + super().get_quantity() + \
            ", Size:" + self.size + '}'



