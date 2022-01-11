class Card:
    def __init__(self, value: int, color: str, symbol: str, link, x1: int, y1: int, x2: int, y2: int):
        self.value = value
        self.color = color
        self.symbol = symbol
        self.link = link
        self.hide = False
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def show(self):
        print(f"({self.value} de {self.symbol}  {self.hide} x1:{self.x1} x2:{self.x2} y1:{self.y1} y2:{self.y2})")

    def return_color(self):
        return self.color

    def get_link(self):
        return self.link

    def retrun_range(self):
        range = [self.x1, self.y1, self.x2, self.y2]
        return range

    def retrun_value(self):
        return self.value

    def return_symbol(self):
        return self.symbol

    def set_new_range(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def return_hide(self):
        return self.hide

    def change_hide(self):
        if self.hide:
            self.hide = False
        else:
            self.hide = True

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2
