"""
This class that represents a standard 52-card deck of playing cards.

The `FrenchDeck` class has the following attributes:

* `ranks`: A list of the ranks of the cards in the deck.
* `suits`: A list of the suits of the cards in the deck.
* `_cards`: A list of all of the cards in the deck.

The `FrenchDeck` class has the following methods:

* `__init__()`: Initializes the `FrenchDeck` object.
* `__len__()`: Returns the number of cards in the deck.
* `__getitem__()`: Returns the card at the specified position in the deck.

"""

from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        return self._cards[position]

if __name__ == "__main__":
    import doctest
    doctest.testfile("frenchdeck.doctest", verbose=True)