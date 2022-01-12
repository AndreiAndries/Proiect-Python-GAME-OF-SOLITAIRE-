from Deck import Deck
from Card import Card


class Game:

    def __init__(self, deck: Deck):
        self.initial_deck = deck
        self.initial_deck.shuffle()
        self.romburi = Deck()
        self.romburi.set_width(200,340)
        self.romburi.set_height(30,230)
        self.inimi = Deck()
        self.inimi.set_width(30,170)
        self.inimi.set_height(30,230)
        self.trefle = Deck()
        self.trefle.set_width(540,680)
        self.trefle.set_height(30,230)
        self.frunze = Deck()
        self.frunze.set_width(370,510)
        self.frunze.set_height(30,230)
        self.unu = Deck()
        self.unu.set_width(60,200)
        self.unu.set_height(280,480)
        self.doi = Deck()
        self.doi.set_width(230,370)
        self.doi.set_height(280,480)
        self.trei = Deck()
        self.trei.set_width(400,540)
        self.trei.set_height(280,480)
        self.patru = Deck()
        self.patru.set_width(570,710)
        self.patru.set_height(280,480)
        self.cinci = Deck()
        self.cinci.set_width(740,880)
        self.cinci.set_height(280,480)
        self.sase = Deck()
        self.sase.set_width(910,1050)
        self.sase.set_height(280,480)
        self.sapte = Deck()
        self.sapte.set_width(1080,1220)
        self.sapte.set_width(280,480)
        self.rests1 = Deck()
        self.rests1.set_width(1320,1460)
        self.rests1.set_height(30,230)
        self.rests2 = Deck()
        self.rests2.set_width(1150,1290)
        self.rests2.set_height(30,230)

    def arange(self):
        self.unu.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.unu.retun_element(0).set_new_range(60, 280, 200, 480)

        self.doi.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.doi.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.doi.retun_element(0).change_hide()
        self.doi.retun_element(0).set_new_range(230, 280, 370, 324)
        self.doi.retun_element(1).set_new_range(230, 325, 370, 525)

        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.trei.retun_element(0).change_hide()
        self.trei.retun_element(1).change_hide()
        self.trei.retun_element(0).set_new_range(400, 280, 540, 324)
        self.trei.retun_element(1).set_new_range(400, 325, 540, 369)
        self.trei.retun_element(2).set_new_range(400, 370, 540, 570)

        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.patru.retun_element(0).change_hide()
        self.patru.retun_element(1).change_hide()
        self.patru.retun_element(2).change_hide()
        self.patru.retun_element(0).set_new_range(570, 280, 710, 324)
        self.patru.retun_element(1).set_new_range(570, 325, 710, 369)
        self.patru.retun_element(2).set_new_range(570, 370, 710, 414)
        self.patru.retun_element(3).set_new_range(570, 415, 710, 615)

        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.cinci.retun_element(0).change_hide()
        self.cinci.retun_element(1).change_hide()
        self.cinci.retun_element(2).change_hide()
        self.cinci.retun_element(3).change_hide()
        self.cinci.retun_element(0).set_new_range(740, 280, 880, 324)
        self.cinci.retun_element(1).set_new_range(740, 325, 880, 369)
        self.cinci.retun_element(2).set_new_range(740, 370, 880, 414)
        self.cinci.retun_element(3).set_new_range(740, 415, 880, 459)
        self.cinci.retun_element(4).set_new_range(740, 460, 880, 660)

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
        self.sase.retun_element(0).set_new_range(910, 280, 1050, 324)
        self.sase.retun_element(1).set_new_range(910, 325, 1050, 369)
        self.sase.retun_element(2).set_new_range(910, 370, 1050, 414)
        self.sase.retun_element(3).set_new_range(910, 415, 1050, 459)
        self.sase.retun_element(4).set_new_range(910, 460, 1050, 504)
        self.sase.retun_element(5).set_new_range(910, 505, 1050, 705)

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
        self.sapte.retun_element(0).set_new_range(1080, 280, 1220, 324)
        self.sapte.retun_element(1).set_new_range(1080, 325, 1220, 369)
        self.sapte.retun_element(2).set_new_range(1080, 370, 1220, 414)
        self.sapte.retun_element(3).set_new_range(1080, 415, 1220, 459)
        self.sapte.retun_element(4).set_new_range(1080, 460, 1220, 504)
        self.sapte.retun_element(5).set_new_range(1080, 505, 1220, 549)
        self.sapte.retun_element(6).set_new_range(1080, 550, 1220, 750)

        while self.initial_deck.size() > 0:
            self.initial_deck.return_last_element().change_hide()
            self.rests1.add_card_to_deck(self.initial_deck.eliminate_and_return())
        self.rests1.reverse()
        for card in self.rests1.get_cards():
            card.set_new_range(1320, 30, 1460, 230)

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
        for card in self.unu.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.doi.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.trei.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.patru.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.cinci.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.sase.get_cards():
            if card.return_hide():
                ok4 = False
        for card in self.sapte.get_cards():
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

    def get_unu(self):
        return self.unu.get_cards()

    def get_doi(self):
        return self.doi.get_cards()

    def get_trei(self):
        return self.trei.get_cards()

    def get_patru(self):
        return self.patru.get_cards()

    def get_cinci(self):
        return self.cinci.get_cards()

    def get_sase(self):
        return self.sase.get_cards()

    def get_sapte(self):
        return self.sapte.get_cards()

    def get_rests1(self):
        return self.rests1.get_cards()

    def get_rests2(self):
        return self.rests2.get_cards()

    def get_inimi(self):
        return self.inimi.get_cards()

    def get_romburi(self):
        return self.romburi.get_cards()

    def get_frunze(self):
        return self.frunze.get_cards()

    def get_trefle(self):
        return self.trefle.get_cards()

    def get_rests1_deck(self):
        return self.rests1

    def get_rests2_deck(self):
        return self.rests2

    def get_inimi_deck(self):
        return self.inimi

    def get_frunze_deck(self):
        return self.frunze

    def get_trefle_deck(self):
        return self.trefle

    def get_unu_deck(self):
        return self.unu

    def get_romburi_deck(self):
        return self.romburi

    def get_doi_deck(self):
        return self.doi

    def get_trei_deck(self):
        return self.trei

    def get_patru_deck(self):
        return self.patru

    def get_cinci_deck(self):
        return self.cinci

    def get_sase_deck(self):
        return self.sase

    def get_sapte_deck(self):
        return self.sapte