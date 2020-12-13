import itertools
import random

# shufflfe a deck of cards

# try to build some simple card game

# macking a deck of classic cards
deck = list(itertools.product([2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"],
                              ['\u2661', '\u2662', '\u2664', '\u2667']))

# shuffle deck of cards
random.shuffle(deck)

# draw cards
print("Your cards:")
for i in range (5):
    print(deck[i][0], deck[i][1], end=" | ")