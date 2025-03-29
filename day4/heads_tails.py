# utilizing the random module, create a heads of tails generator

import random

random_float = random.random() * 100

if random_float <= 50:
    print("Heads")
else:
    print("Tails")
