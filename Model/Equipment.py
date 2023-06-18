class Equipment:

    def __init__(self, quantity, sec_lvl):
        self.quantity = quantity
        self.sec_lvl = sec_lvl

    def get_sec_lvl(self):
        return self.sec_lvl

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        pass
