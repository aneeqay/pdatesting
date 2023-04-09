import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("diamond", 1)
        self.card2 = Card("club", 5)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame

    def test_check_for_ace(self):
        actual1 = self.card_game.check_for_ace(self.card1)
        actual2 = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, actual1)
        self.assertEqual(False, actual2)

    def test_highest_card(self):
        actual = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, actual)

    def test_cards_total(self):
        actual = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 6", actual)