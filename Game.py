from Deck import Deck
from Card import Card

class Game:

    def __init__(self, deck: Deck):
        self.initial_deck = deck
        self.initial_deck.shuffle()
        self.romburi = Deck()
        self.inimi = Deck()
        self.trefle = Deck()
        self.frunze = Deck()
        self.unu = Deck()
        self.doi = Deck()
        self.trei = Deck()
        self.patru = Deck()
        self.cinci = Deck()
        self.sase = Deck()
        self.sapte = Deck()
        self.rests1 = Deck()
        self.rests2 = Deck()

    def arange(self):
        self.unu.add_card_to_deck(self.initial_deck.eliminate_and_return())

        self.doi.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.doi.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.doi.retun_element(0).change_hide()

        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.retun_element(0).change_hide()
        self.trei.retun_element(1).change_hide()

        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.retun_element(0).change_hide()
        self.patru.retun_element(1).change_hide()
        self.patru.retun_element(2).change_hide()

        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.retun_element(0).change_hide()
        self.cinci.retun_element(1).change_hide()
        self.cinci.retun_element(2).change_hide()
        self.cinci.retun_element(3).change_hide()

        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sase.retun_element(0).change_hide()
        self.sase.retun_element(1).change_hide()
        self.sase.retun_element(2).change_hide()
        self.sase.retun_element(3).change_hide()
        self.sase.retun_element(4).change_hide()

        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.sapte.retun_element(0).change_hide()
        self.sapte.retun_element(1).change_hide()
        self.sapte.retun_element(2).change_hide()
        self.sapte.retun_element(3).change_hide()
        self.sapte.retun_element(4).change_hide()
        self.sapte.retun_element(5).change_hide()

        while self.initial_deck.size() > 0:
            self.initial_deck.return_last_element().change_hide()
            self.rests1.add_card_to_deck(self.initial_deck.eliminate_and_return())

        self.rests1.reverse()

    def final(self):
        ok1 = False
        ok2 = False
        ok3 = False
        ok4 = False
        if self.inimi.size() == 13:
            ok1 = True
        if self.romburi.size() == 13:
            ok2 = True
        if self.frunze.size() == 13:
            ok3 = True
        if self.trefle.size() == 13:
            ok4 = True

        if ok1 and ok2 and ok3 and ok4:
            return True
        return False

    def check_auto_make(self):
        ok1 = True
        ok2 = True
        ok3 = True
        ok4 = True

        if self.rests1.size() > 0:
            ok1 = False
        if self.rests2.size() > 0:
            ok2 = False
        if self.inimi.size() == 0 or self.romburi.size() == 0 or self.frunze.size() == 0 or self.trefle.size() == 0:
            ok3 = False
        for card in self.unu:
            if card.return_hide():
                ok4 = False
        for card in self.doi:
            if card.return_hide():
                ok4 = False
        for card in self.trei:
            if card.return_hide():
                ok4 = False
        for card in self.patru:
            if card.return_hide():
                ok4 = False
        for card in self.cinci:
            if card.return_hide():
                ok4 = False
        for card in self.sase:
            if card.return_hide():
                ok4 = False
        for card in self.sapte:
            if card.return_hide():
                ok4 = False
        if ok1 and ok2 and ok3 and ok4:
            return True
        return False

    def auto_make(self):
        self.unu.reverse()
        self.doi.reverse()
        self.trei.reverse()
        self.patru.reverse()
        self.cinci.reverse()
        self.sase.reverse()
        self.sapte.reverse()
        while not self.final():
            if self.unu.size() > 0:
                card = self.unu.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.unu.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.unu.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.unu.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.unu.eliminate_and_return())
            if self.doi.size() > 0:
                card = self.doi.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.doi.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.doi.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.doi.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.doi.eliminate_and_return())
            if self.trei.size() > 0:
                card = self.trei.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.trei.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.trei.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.trei.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.trei.eliminate_and_return())
            if self.patru.size() > 0:
                card = self.patru.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.patru.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.patru.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.patru.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.patru.eliminate_and_return())
            if self.cinci.size() > 0:
                card = self.cinci.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.cinci.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.cinci.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.cinci.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.cinci.eliminate_and_return())
            if self.sase.size() > 0:
                card = self.sase.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.sase.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.sase.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.sase.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.sase.eliminate_and_return())
            if self.sapte.size() > 0:
                card = self.sapte.return_last_element()
                inima = self.inimi.return_last_element()
                romb = self.inimi.return_last_element()
                frunza = self.inimi.return_last_element()
                trefla = self.inimi.return_last_element()
                if card.return_symbol() == "inima" and card.retrun_value() == inima.retun_value() + 1:
                    self.inimi.add_card_to_deck(self.sapte.eliminate_and_return())
                elif card.return_symbol() == "romb" and card.retrun_value() == romb.retun_value() + 1:
                    self.romburi.add_card_to_deck(self.sapte.eliminate_and_return())
                elif card.return_symbol() == "frunza" and card.retrun_value() == frunza.retun_value() + 1:
                    self.frunze.add_card_to_deck(self.sapte.eliminate_and_return())
                elif card.return_symbol() == "trefla" and card.retrun_value() == trefla.retun_value() + 1:
                    self.trefle.add_card_to_deck(self.sapte.eliminate_and_return())



    def show_Table(self):
        print("Inital Deck: ")
        self.initial_deck.show_deck()
        print("Inimi: ")
        self.inimi.show_deck()
        print("Romburi: ")
        self.romburi.show_deck()
        print("Frunze: ")
        self.frunze.show_deck()
        print("Trefle: ")
        self.trefle.show_deck()
        print("1st: ")
        self.unu.show_deck()
        print("2nd: ")
        self.doi.show_deck()
        print("3rd: ")
        self.trei.show_deck()
        print("4th: ")
        self.patru.show_deck()
        print("5th: ")
        self.cinci.show_deck()
        print("6th: ")
        self.sase.show_deck()
        print("7th: ")
        self.sapte.show_deck()
        print("Rests 1: ")
        self.rests1.show_deck()
        print("Rests 2: ")
        self.rests2.show_deck()
