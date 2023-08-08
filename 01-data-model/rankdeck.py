# The suit_values dictionary is created by using the dict() function,
# which takes keyword arguments and returns a dictionary.
# For example, this is how the suit_values dictionary is created:
#
#   suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# The dict() function is equivalent to using curly braces and colons
# to create a dictionary.
# For example, this is another way to create the same suit_values
# dictionary:
#
#   suit_values = {"spades": 3, "hearts": 2, "diamonds": 1, "clubs": 0}


from frenchdeck import FrenchDeck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
