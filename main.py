from Game import Game
from Deck import Deck
from Card import Card
import pygame


def setup():
    card1 = Card(1, "rosu", "inima", 'Cards\\asDeInima.jpg', 0, 0, 0, 0)
    card2 = Card(2, "rosu", "inima", 'Cards\\doiDeInima.jpg', 0, 0, 0, 0)
    card3 = Card(3, "rosu", "inima", 'Cards\\treiDeInima.jpg', 0, 0, 0, 0)
    card4 = Card(4, "rosu", "inima", 'Cards\\patruDeInima.jpg', 0, 0, 0, 0)
    card5 = Card(5, "rosu", "inima", 'Cards\\cinciDeInima.jpg', 0, 0, 0, 0)
    card6 = Card(6, "rosu", "inima", 'Cards\\saseDeInima.jpg', 0, 0, 0, 0)
    card7 = Card(7, "rosu", "inima", 'Cards\\sapteDeInima.jpg', 0, 0, 0, 0)
    card8 = Card(8, "rosu", "inima", 'Cards\\optDeInima.jpg', 0, 0, 0, 0)
    card9 = Card(9, "rosu", "inima", 'Cards\\nouaDeInima.jpg', 0, 0, 0, 0)
    card10 = Card(10, "rosu", "inima", 'Cards\\zeceDeInima.jpg', 0, 0, 0, 0)
    card11 = Card(11, "rosu", "inima", 'Cards\\jaletDeInima.jpg', 0, 0, 0, 0)
    card12 = Card(12, "rosu", "inima", 'Cards\\damaDeInima.jpg', 0, 0, 0, 0)
    card13 = Card(13, "rosu", "inima", 'Cards\\popaDeInima.jpg', 0, 0, 0, 0)
    card14 = Card(1, "rosu", "romb", 'Cards\\asDeRomb.jpg', 0, 0, 0, 0)
    card15 = Card(2, "rosu", "romb", 'Cards\\doiDeRomb.jpg', 0, 0, 0, 0)
    card16 = Card(3, "rosu", "romb", 'Cards\\treiDeRomb.jpg', 0, 0, 0, 0)
    card17 = Card(4, "rosu", "romb", 'Cards\\patruDeRomb.jpg', 0, 0, 0, 0)
    card18 = Card(5, "rosu", "romb", 'Cards\\cinciDeRomb.jpg', 0, 0, 0, 0)
    card19 = Card(6, "rosu", "romb", 'Cards\\saseDeRomb.jpg', 0, 0, 0, 0)
    card20 = Card(7, "rosu", "romb", 'Cards\\sapteDeRomb.jpg', 0, 0, 0, 0)
    card21 = Card(8, "rosu", "romb", 'Cards\\optDeRomb.jpg', 0, 0, 0, 0)
    card22 = Card(9, "rosu", "romb", 'Cards\\nouaDeRomb.jpg', 0, 0, 0, 0)
    card23 = Card(10, "rosu", "romb", 'Cards\\zeceDeRomb.jpg', 0, 0, 0, 0)
    card24 = Card(11, "rosu", "romb", 'Cards\\jaletDeRomb.jpg', 0, 0, 0, 0)
    card25 = Card(12, "rosu", "romb", 'Cards\\damaDeRomb.jpg', 0, 0, 0, 0)
    card26 = Card(13, "rosu", "romb", 'Cards\\popaDeRomb.jpg', 0, 0, 0, 0)
    card27 = Card(1, "negru", "frunza", 'Cards\\asDeFrunza.jpg', 0, 0, 0, 0)
    card28 = Card(2, "negru", "frunza", 'Cards\\doiDeFrunza.jpg', 0, 0, 0, 0)
    card29 = Card(3, "negru", "frunza", 'Cards\\treiDeFrunza.jpg', 0, 0, 0, 0)
    card30 = Card(4, "negru", "frunza", 'Cards\\patruDeFrunza.jpg', 0, 0, 0, 0)
    card31 = Card(5, "negru", "frunza", 'Cards\\cinciDeFrunza.jpg', 0, 0, 0, 0)
    card32 = Card(6, "negru", "frunza", 'Cards\\saseDeFrunza.jpg', 0, 0, 0, 0)
    card33 = Card(7, "negru", "frunza", 'Cards\\sapteDeFrunza.jpg', 0, 0, 0, 0)
    card34 = Card(8, "negru", "frunza", 'Cards\\optDeFrunza.jpg', 0, 0, 0, 0)
    card35 = Card(9, "negru", "frunza", 'Cards\\nouaDeFrunza.jpg', 0, 0, 0, 0)
    card36 = Card(10, "negru", "frunza", 'Cards\\zeceDeFrunza.jpg', 0, 0, 0, 0)
    card37 = Card(11, "negru", "frunza", 'Cards\\jaletDeFrunza.jpg', 0, 0, 0, 0)
    card38 = Card(12, "negru", "frunza", 'Cards\\damaDeFrunza.jpg', 0, 0, 0, 0)
    card39 = Card(13, "negru", "frunza", 'Cards\\popaDeFrunza.jpg', 0, 0, 0, 0)
    card40 = Card(1, "negru", "trefla", 'Cards\\asDeTrefla.jpg', 0, 0, 0, 0)
    card41 = Card(2, "negru", "trefla", 'Cards\\doiDeTrefla.jpg', 0, 0, 0, 0)
    card42 = Card(3, "negru", "trefla", 'Cards\\treiDeTrefla.jpg', 0, 0, 0, 0)
    card43 = Card(4, "negru", "trefla", 'Cards\\patruDeTrefla.jpg', 0, 0, 0, 0)
    card44 = Card(5, "negru", "trefla", 'Cards\\cinciDeTrefla.jpg', 0, 0, 0, 0)
    card45 = Card(6, "negru", "trefla", 'Cards\\saseDeTrefla.jpg', 0, 0, 0, 0)
    card46 = Card(7, "negru", "trefla", 'Cards\\sapteDeTrefla.jpg', 0, 0, 0, 0)
    card47 = Card(8, "negru", "trefla", 'Cards\\optDeTrefla.jpg', 0, 0, 0, 0)
    card48 = Card(9, "negru", "trefla", 'Cards\\nouaDeTrefla.jpg', 0, 0, 0, 0)
    card49 = Card(10, "negru", "trefla", 'Cards\\zeceDeTrefla.jpg', 0, 0, 0, 0)
    card50 = Card(11, "negru", "trefla", 'Cards\\jaletDeTrefla.jpg', 0, 0, 0, 0)
    card51 = Card(12, "negru", "trefla", 'Cards\\damaDeTrefla.jpg', 0, 0, 0, 0)
    card52 = Card(13, "negru", "trefla", 'Cards\\popaDeTrefla.jpg', 0, 0, 0, 0)

    deck = Deck()
    deck.add_card_to_deck(card1)
    deck.add_card_to_deck(card2)
    deck.add_card_to_deck(card3)
    deck.add_card_to_deck(card4)
    deck.add_card_to_deck(card5)
    deck.add_card_to_deck(card6)
    deck.add_card_to_deck(card7)
    deck.add_card_to_deck(card8)
    deck.add_card_to_deck(card9)
    deck.add_card_to_deck(card10)
    deck.add_card_to_deck(card11)
    deck.add_card_to_deck(card12)
    deck.add_card_to_deck(card13)
    deck.add_card_to_deck(card14)
    deck.add_card_to_deck(card15)
    deck.add_card_to_deck(card16)
    deck.add_card_to_deck(card17)
    deck.add_card_to_deck(card18)
    deck.add_card_to_deck(card19)
    deck.add_card_to_deck(card20)
    deck.add_card_to_deck(card21)
    deck.add_card_to_deck(card22)
    deck.add_card_to_deck(card23)
    deck.add_card_to_deck(card24)
    deck.add_card_to_deck(card25)
    deck.add_card_to_deck(card26)
    deck.add_card_to_deck(card27)
    deck.add_card_to_deck(card28)
    deck.add_card_to_deck(card29)
    deck.add_card_to_deck(card30)
    deck.add_card_to_deck(card31)
    deck.add_card_to_deck(card32)
    deck.add_card_to_deck(card33)
    deck.add_card_to_deck(card34)
    deck.add_card_to_deck(card35)
    deck.add_card_to_deck(card36)
    deck.add_card_to_deck(card37)
    deck.add_card_to_deck(card38)
    deck.add_card_to_deck(card39)
    deck.add_card_to_deck(card40)
    deck.add_card_to_deck(card41)
    deck.add_card_to_deck(card42)
    deck.add_card_to_deck(card43)
    deck.add_card_to_deck(card44)
    deck.add_card_to_deck(card45)
    deck.add_card_to_deck(card46)
    deck.add_card_to_deck(card47)
    deck.add_card_to_deck(card48)
    deck.add_card_to_deck(card49)
    deck.add_card_to_deck(card50)
    deck.add_card_to_deck(card51)
    deck.add_card_to_deck(card52)
    g = Game(deck)
    g.arange()
    return g


def cards_on_table(imgage, x, y):
    screen.blit(imgage, (x, y))


def make_resturi1_move(game: Game):
    if len(game.get_rests1()) > 0:
        element = game.get_rests1().pop()
        element.change_hide()
        game.get_rests2().append(element)
    elif len(game.get_rests1()) == 0 and len(game.get_rests2()) > 0:
        while len(game.get_rests2()) > 0:
            element = game.get_rests2().pop()
            element.change_hide()
            game.get_rests1().append(element)

def make_resturi2_move(game: Game):
    if len(game.get_rests2()) > 0 :
        element = game.get_rests2()[-1]
        ok = False
        if element.retrun_value() == 1 :
            if element.return_symbol() == "inima":
                game.get_rests2().pop()
                element.set_new_range(game.get_inimi_deck().get_x1(),game.get_inimi_deck().get_y1(),
                                      game.get_inimi_deck().get_x2(),game.get_inimi_deck().get_y2())
                game.get_inimi().append(element)
                ok = True

            elif element.return_symbol() == "romb":
                game.get_rests2().pop()
                element.set_new_range(game.get_romburi_deck().get_x1(), game.get_romburi_deck().get_y1(),
                                      game.get_romburi_deck().get_x2(), game.get_romburi_deck().get_y2())
                game.get_romburi().append(element)
                ok = True

            elif element.return_symbol() == "trefla":
                game.get_rests2().pop()
                element.set_new_range(game.get_trefle_deck().get_x1(), game.get_trefle_deck().get_y1(),
                                      game.get_trefle_deck().get_x2(), game.get_trefle_deck().get_y2())
                game.get_trefle().append(element)
                ok = True

            elif element.return_symbol() == "frunza":
                game.get_rests2().pop()
                element.set_new_range(game.get_frunze_deck().get_x1(), game.get_frunze_deck().get_y1(),
                                      game.get_frunze_deck().get_x2(), game.get_frunze_deck().get_y2())
                game.get_frunze().append(element)
                ok = True

        else :
            if len(game.get_inimi()) > 0 and ok == False:
                if element.return_symbol() == "inima" and element.retrun_value() == game.get_inimi()[-1].retrun_value() + 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_inimi_deck().get_x1(), game.get_inimi_deck().get_y1(),
                                          game.get_inimi_deck().get_x2(), game.get_inimi_deck().get_y2())
                    game.get_inimi().append(element)
                    ok = True

            if len(game.get_romburi()) > 0 and ok == False:
                if element.return_symbol() == "romb" and element.retrun_value() == game.get_romburi()[-1].retrun_value() + 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_romburi_deck().get_x1(), game.get_romburi_deck().get_y1(),
                                          game.get_romburi_deck().get_x2(), game.get_romburi_deck().get_y2())
                    game.get_romburi().append(element)
                    ok = True

            if len(game.get_trefle()) > 0 and ok == False:
                if element.return_symbol() == "trefla" and element.retrun_value() == game.get_trefle()[-1].retrun_value() + 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_trefle_deck().get_x1(), game.get_trefle_deck().get_y1(),
                                          game.get_trefle_deck().get_x2(), game.get_trefle_deck().get_y2())
                    game.get_trefle().append(element)
                    ok = True

            if len(game.get_frunze()) > 0 and ok == False:
                if element.return_symbol() == "frunza" and element.retrun_value() == game.get_frunze()[-1].retrun_value() + 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_frunze_deck().get_x1(), game.get_frunze_deck().get_y1(),
                                          game.get_frunze_deck().get_x2(), game.get_frunze_deck().get_y2())
                    game.get_frunze().append(element)
                    ok = True

            if len(game.get_unu()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_unu()[-1].return_color() == "negru" and element.retrun_value() == game.get_unu()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_unu()[-1].get_x1(), game.get_unu()[-1].get_y1() + 45,
                                          game.get_unu()[-1].get_x2(), game.get_unu()[-1].get_y2() + 45)
                    game.get_unu()[-1].set_new_range(game.get_unu()[-1].get_x1(), game.get_unu()[-1].get_y1(),
                                          game.get_unu()[-1].get_x2(), game.get_unu()[-1].get_y1() + 44)
                    game.get_unu().append(element)
                    ok = True
                elif element.return_color() == "negru" and game.get_unu()[-1].return_color() == "rosu" and element.retrun_value() == game.get_unu()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_unu()[-1].get_x1(), game.get_unu()[-1].get_y1() + 45,
                                          game.get_unu()[-1].get_x2(), game.get_unu()[-1].get_y2() + 45)
                    game.get_unu()[-1].set_new_range(game.get_unu()[-1].get_x1(), game.get_unu()[-1].get_y1(),
                                          game.get_unu()[-1].get_x2(), game.get_unu()[-1].get_y1() + 44)
                    game.get_unu().append(element)
                    ok = True

            elif len(game.get_unu()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_unu_deck().get_x1(),game.get_unu_deck().get_x2(),
                                      game.get_unu_deck().get_y1(),game.get_unu_deck().get_y2() )
                game.get_unu().append(element)
                ok = True

            if len(game.get_doi()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_doi()[-1].return_color() == "negru" and  element.retrun_value() == game.get_doi()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    print("A")
                    element.set_new_range(game.get_doi()[-1].get_x1(), game.get_doi()[-1].get_y1() + 45,
                                          game.get_doi()[-1].get_x2(), game.get_doi()[-1].get_y2() + 45)
                    game.get_doi()[-1].set_new_range(game.get_doi()[-1].get_x1(), game.get_doi()[-1].get_y1(),
                                          game.get_doi()[-1].get_x2(), game.get_doi()[-1].get_y1() + 44)
                    game.get_doi().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_doi()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_doi()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_doi()[-1].get_x1(), game.get_doi()[-1].get_y1() + 45,
                                          game.get_doi()[-1].get_x2(), game.get_doi()[-1].get_y2() + 45)
                    game.get_doi()[-1].set_new_range(game.get_doi()[-1].get_x1(), game.get_doi()[-1].get_y1(),
                                          game.get_doi()[-1].get_x2(), game.get_doi()[-1].get_y1() + 44)
                    game.get_doi().append(element)
                    ok = True

            elif len(game.get_doi()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_doi_deck().get_x1(),game.get_doi_deck().get_x2(),
                                      game.get_doi_deck().get_y1(),game.get_doi_deck().get_y2() )
                game.get_doi().append(element)
                ok = True

            if len(game.get_trei()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_trei()[-1].return_color() == "negru" and  element.retrun_value() == game.get_trei()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_trei()[-1].get_x1(), game.get_trei()[-1].get_y1() + 45,
                                          game.get_trei()[-1].get_x2(), game.get_trei()[-1].get_y2() + 45)
                    game.get_trei()[-1].set_new_range(game.get_trei()[-1].get_x1(), game.get_trei()[-1].get_y1(),
                                          game.get_trei()[-1].get_x2(), game.get_trei()[-1].get_y1() + 44)
                    game.get_trei().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_trei()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_trei()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_trei()[-1].get_x1(), game.get_trei()[-1].get_y1() + 45,
                                          game.get_trei()[-1].get_x2(), game.get_trei()[-1].get_y2() + 45)
                    game.get_trei()[-1].set_new_range(game.get_trei()[-1].get_x1(), game.get_trei()[-1].get_y1(),
                                          game.get_trei()[-1].get_x2(), game.get_trei()[-1].get_y1() + 44)
                    game.get_trei().append(element)
                    ok = True

            elif len(game.get_trei()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_trei_deck().get_x1(),game.get_trei_deck().get_x2(),
                                      game.get_trei_deck().get_y1(),game.get_trei_deck().get_y2() )
                game.get_trei().append(element)
                ok = True

            if len(game.get_patru()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_patru()[-1].return_color() == "negru" and  element.retrun_value() == game.get_patru()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_patru()[-1].get_x1(), game.get_patru()[-1].get_y1() + 45,
                                          game.get_patru()[-1].get_x2(), game.get_patru()[-1].get_y2() + 45)
                    game.get_patru()[-1].set_new_range(game.get_patru()[-1].get_x1(), game.get_patru()[-1].get_y1(),
                                          game.get_patru()[-1].get_x2(), game.get_patru()[-1].get_y1() + 44)
                    game.get_patru().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_patru()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_patru()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_patru()[-1].get_x1(), game.get_patru()[-1].get_y1() + 45,
                                          game.get_patru()[-1].get_x2(), game.get_patru()[-1].get_y2() + 45)
                    game.get_patru()[-1].set_new_range(game.get_patru()[-1].get_x1(), game.get_patru()[-1].get_y1(),
                                          game.get_patru()[-1].get_x2(), game.get_patru()[-1].get_y1() + 44)
                    game.get_patru().append(element)
                    ok = True

            elif len(game.get_patru()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_patru_deck().get_x1(),game.get_patru_deck().get_x2(),
                                      game.get_patru_deck().get_y1(),game.get_patru_deck().get_y2() )
                game.get_patru().append(element)
                ok = True

            if len(game.get_cinci()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_cinci()[-1].return_color() == "negru" and  element.retrun_value() == game.get_cinci()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_cinci()[-1].get_x1(), game.get_cinci()[-1].get_y1() + 45,
                                          game.get_cinci()[-1].get_x2(), game.get_cinci()[-1].get_y2() + 45)
                    game.get_cinci()[-1].set_new_range(game.get_cinci()[-1].get_x1(), game.get_cinci()[-1].get_y1(),
                                          game.get_cinci()[-1].get_x2(), game.get_cinci()[-1].get_y1() + 44)
                    game.get_cinci().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_cinci()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_cinci()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_cinci()[-1].get_x1(), game.get_cinci()[-1].get_y1() + 45,
                                          game.get_cinci()[-1].get_x2(), game.get_cinci()[-1].get_y2() + 45)
                    game.get_cinci()[-1].set_new_range(game.get_cinci()[-1].get_x1(), game.get_cinci()[-1].get_y1(),
                                          game.get_cinci()[-1].get_x2(), game.get_cinci()[-1].get_y1() + 44)
                    game.get_cinci().append(element)
                    ok = True

            elif len(game.get_cinci()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_cinci_deck().get_x1(),game.get_cinci_deck().get_x2(),
                                      game.get_cinci_deck().get_y1(),game.get_cinci_deck().get_y2() )
                game.get_cinci().append(element)
                ok = True

            if len(game.get_sase()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_sase()[-1].return_color() == "negru" and  element.retrun_value() == game.get_sase()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_sase()[-1].get_x1(), game.get_sase()[-1].get_y1() + 45,
                                          game.get_sase()[-1].get_x2(), game.get_sase()[-1].get_y2() + 45)
                    game.get_sase()[-1].set_new_range(game.get_sase()[-1].get_x1(), game.get_sase()[-1].get_y1(),
                                          game.get_sase()[-1].get_x2(), game.get_sase()[-1].get_y1() + 44)
                    game.get_sase().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_sase()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_sase()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_sase()[-1].get_x1(), game.get_sase()[-1].get_y1() + 45,
                                          game.get_sase()[-1].get_x2(), game.get_sase()[-1].get_y2() + 45)
                    game.get_sase()[-1].set_new_range(game.get_sase()[-1].get_x1(), game.get_sase()[-1].get_y1(),
                                          game.get_sase()[-1].get_x2(), game.get_sase()[-1].get_y1() + 44)
                    game.get_sase().append(element)
                    ok = True

            elif len(game.get_sase()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_sase_deck().get_x1(),game.get_sase_deck().get_x2(),
                                      game.get_sase_deck().get_y1(),game.get_sase_deck().get_y2() )
                game.get_sase().append(element)
                ok = True

            if len(game.get_sapte()) > 0 and ok == False:
                if element.return_color() == "rosu" and game.get_sapte()[-1].return_color() == "negru" and  element.retrun_value() == game.get_sapte()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_sapte()[-1].get_x1(), game.get_sapte()[-1].get_y1() + 45,
                                          game.get_sapte()[-1].get_x2(), game.get_sapte()[-1].get_y2() + 45)
                    game.get_sapte()[-1].set_new_range(game.get_sapte()[-1].get_x1(), game.get_sapte()[-1].get_y1(),
                                          game.get_sapte()[-1].get_x2(), game.get_sapte()[-1].get_y1() + 44)
                    game.get_sapte().append(element)
                    ok = True

                elif element.return_color() == "negru" and game.get_sapte()[-1].return_color() == "rosu" and  element.retrun_value() == game.get_sapte()[-1].retrun_value() - 1:
                    game.get_rests2().pop()
                    element.set_new_range(game.get_sapte()[-1].get_x1(), game.get_sapte()[-1].get_y1() + 45,
                                          game.get_sapte()[-1].get_x2(), game.get_sapte()[-1].get_y2() + 45)
                    game.get_sapte()[-1].set_new_range(game.get_sapte()[-1].get_x1(), game.get_sapte()[-1].get_y1(),
                                          game.get_sapte()[-1].get_x2(), game.get_sapte()[-1].get_y1() + 44)
                    game.get_sapte().append(element)
                    ok = True

            elif len(game.get_sapte()) == 0 and ok == False and element.retrun_value() == 13:
                game.get_rests2().pop()
                element.set_new_range(game.get_sapte_deck().get_x1(),game.get_sapte_deck().get_x2(),
                                      game.get_sapte_deck().get_y1(),game.get_sapte_deck().get_y2() )
                game.get_sapte().append(element)






def make_a_move(game: Game, x, y):
    g = game
    copy = g.get_rests1_deck()
    x1 = copy.get_x1()
    x2 = copy.get_x2()
    y1 = copy.get_y1()
    y2 = copy.get_y2()
    if x <= x2 and x >= x1 and y <= y2 and y >= y1:
        make_resturi1_move(g)
    copy = g.get_rests2_deck()
    x1 = copy.get_x1()
    x2 = copy.get_x2()
    y1 = copy.get_y1()
    y2 = copy.get_y2()
    if x <= x2 and x >= x1 and y <= y2 and y >= y1:
        make_resturi2_move(g)



def print_scene(g: Game):
    # inimi (x = 30 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (30, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (30, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (165, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (30, 225, 140, 5))

    # romburi (x = 200 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (200, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (200, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (335, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (200, 225, 140, 5))

    # frunze (x = 370 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (370, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (370, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (505, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (370, 225, 140, 5))

    # trefle (x = 540 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (540, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (540, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (675, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (540, 225, 140, 5))

    # resturi2 (x = 1320 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (1320, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1320, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (1455, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1320, 225, 140, 5))

    # resturi1 (x = 1150 , y = 30 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (1150, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1150, 30, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (1285, 30, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1150, 225, 140, 5))

    # unu (x = 60 , y = 280 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (60, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (60, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (195, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (60, 475, 140, 5))

    # doi (x = 230 , y = 280 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (230, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (230, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (365, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (230, 475, 140, 5))

    # trei(x=400, y=280, latime=140, inaltime=200)
    pygame.draw.rect(screen, (0, 0, 0), (400, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (400, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (535, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (400, 475, 140, 5))

    # patru(x=570, y=280, latime=140, inaltime=200)
    pygame.draw.rect(screen, (0, 0, 0), (570, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (570, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (705, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (570, 475, 140, 5))

    # cinci (x = 740 , y = 280 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (740, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (740, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (875, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (740, 475, 140, 5))

    # sase (x = 910 , y = 280 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (910, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (910, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (1045, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (910, 475, 140, 5))

    # sapte (x = 1080 , y = 280 , latime = 140, inaltime = 200)
    pygame.draw.rect(screen, (0, 0, 0), (1080, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1080, 280, 140, 5))
    pygame.draw.rect(screen, (0, 0, 0), (1215, 280, 5, 200))
    pygame.draw.rect(screen, (0, 0, 0), (1080, 475, 140, 5))

    pygame.draw.rect(screen, (0, 0, 0), (0, 240, 1500, 20))

    inimi = g.get_inimi()
    if len(inimi) > 0:
        image = inimi[-1].get_link()
        x = inimi[-1].get_x1()
        y = inimi[-1].get_y1()
        card_inimi = pygame.transform.scale(pygame.image.load(image), (140, 200))
        cards_on_table(card_inimi, x, y)
    romburi = g.get_romburi()
    if len(romburi) > 0:
        image = romburi[-1].get_link()
        x = romburi[-1].get_x1()
        y = romburi[-1].get_y1()
        card_romburi = pygame.transform.scale(pygame.image.load(image), (140, 200))
        cards_on_table(card_romburi, x, y)
    frunze = g.get_frunze()
    if len(frunze) > 0:
        image = frunze[-1].get_link()
        x = frunze[-1].get_x1()
        y = frunze[-1].get_y1()
        card_frunze = pygame.transform.scale(pygame.image.load(image), (140, 200))
        cards_on_table(card_frunze, x, y)
    trefle = g.get_trefle()
    if len(trefle) > 0:
        image = trefle[-1].get_link()
        x = trefle[-1].get_x1()
        y = trefle[-1].get_y1()
        card_trefle = pygame.transform.scale(pygame.image.load(image), (140, 200))
        cards_on_table(card_trefle, x, y)
    resturi2 = g.get_rests2()
    if len(resturi2) > 0:
        image = resturi2[-1].get_link()
        x = g.get_rests2_deck().get_x1()
        y = g.get_rests2_deck().get_y1()
        card_resturi2 = pygame.transform.scale(pygame.image.load(image), (140, 200))
        cards_on_table(card_resturi2, x, y)
    resturi1 = g.get_rests1()
    if len(resturi1) > 0:
        card_resturi1 = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
        cards_on_table(card_resturi1, 1320, 30)
    unu = g.get_unu()
    if len(unu) > 0:
        for carte in unu:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    doi = g.get_doi()
    if len(doi) > 0:
        for carte in doi:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    trei = g.get_trei()
    if len(trei) > 0:
        for carte in trei:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    patru = g.get_patru()
    if len(patru) > 0:
        for carte in patru:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    cinci = g.get_cinci()
    if len(cinci) > 0:
        for carte in cinci:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    sase = g.get_sase()
    if len(sase) > 0:
        for carte in sase:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
    sapte = g.get_sapte()
    if len(sapte) > 0:
        for carte in sapte:
            if carte.return_hide():
                card = pygame.transform.scale(pygame.image.load('Cards\\back.jpg'), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())
            else:
                card = pygame.transform.scale(pygame.image.load(carte.get_link()), (140, 200))
                cards_on_table(card, carte.get_x1(), carte.get_y1())


if __name__ == '__main__':
    game = setup()
    game.show_Table()
    pygame.init()
    screen = pygame.display.set_mode((1500, 900))
    # Background
    background = pygame.transform.scale(pygame.image.load('Cards\\map.png'), (1500, 900))
    # Title and Icon
    pygame.display.set_caption("GAME OF SOLITAIRE")
    icon = pygame.image.load('Cards\\logo.jpg')
    pygame.display.set_icon(icon)
    # Game Loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    x = position[0]
                    y = position[1]
                    make_a_move(game, x, y)
                    game.show_Table()

        print_scene(game)

        pygame.display.update()
