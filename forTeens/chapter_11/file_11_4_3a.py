import random

ab = "abcdefghijklmnopqrstuvwxyz"

random_letter1 = ab[random.randrange(26)]
random_letter2 = ab[random.randrange(26)]
random_letter3 = ab[random.randrange(26)]

random_word = random_letter1 + random_letter2 + random_letter3 
print(random_word)
