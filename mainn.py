import random
import string

def random_letter():
    while True:
        yield random.choice(string.ascii_lowercase)

gen = random_letter()

next(gen)
print(next(gen))