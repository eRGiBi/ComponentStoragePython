class Equipment:

    def __init__(self, quantity, sec_lvl):
        self.__quantity = quantity
        self.__sec_lvl = sec_lvl

    def get_sec_lvl(self):
        return self.__sec_lvl

    def get_quantity(self):
        return self.__quantity
