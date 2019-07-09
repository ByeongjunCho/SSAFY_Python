import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)

print(sorted(lotto))