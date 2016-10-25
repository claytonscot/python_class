__author__ = 'Home'
from random import randint
#tests randint function's ability to pick numbers 0 - 500
#reports number of times picked within a certain range

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
index = 0
while index < 100000:
    cointoss = randint(0,500)
    if cointoss > 400:
        cat1 += 1
    elif cointoss > 300:
        cat2 += 1
    elif cointoss > 200:
        cat3 += 1
    elif cointoss > 100:
        cat4 += 1
    index += 1

print(cat1)
print(cat2)
print(cat3)
print(cat4)

