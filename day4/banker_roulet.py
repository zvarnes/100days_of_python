# using knowledge of random module and lists to create random name decider

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_int = random.randint(0,5)

print(friends[random_int])