import random

from Card import Card

class Deck(object):
    def __init__(self):
        self.cards = []
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def add_card_to_deck(self,card:Card):
        self.cards.append(card)

    def is_deck_empty(self):
        if len(self.cards) == 0:
            return True
        return False

    def retun_first_value(self):
        return self.cards[0]

    def eliminate_and_return(self):
        return self.cards.pop()

    def return_last_element(self):
        return self.cards[-1]

    def retun_element(self,index:int):
        return self.cards[index]

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def reverse(self):
        self.cards.reverse()

    def show_deck(self):
        for card in self.cards:
            card.show()

    def get_cards(self):
        return self.cards

    def set_width(self,x1,x2):
        self.x1 = x1
        self.x2 = x2

    def set_height(self,y1,y2):
        self.y1 = y1
        self.y2 = y2

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2