import random

from Card import Card

class Deck(object):
    def __init__(self):
        self.cards = []

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