__author__ = 'Home'
from random import randint
#Experimenting with random's randint function
#Creates 4,000,000 random single digits and evaluates percentages
#Also tracks iterations to 'view' processing speed
#Tells if any particular number occurs at higher or lower frequency than others

index = 0

zero = 0
one = 0
two = 0
three = 0
four = 0
five =  0
six = 0
seven = 0
eight = 0
nine = 0

while index < 4000000:
    num = randint(0,9)
    if num == 0:
        zero += 1
    elif num == 1:
        one += 1
    elif num == 2:
        two += 1
    elif num == 3:
        three += 1
    elif num == 4:
        four += 1
    elif num == 5:
        five += 1
    elif num == 6:
        six += 1
    elif num == 7:
        seven += 1
    elif num == 8:
        eight += 1
    elif num == 9:
        nine += 1
    index += 1
    if index == 100000:
        print("Index currently at", index)
    elif index == 200000:
        print("Index currently at", index)
    elif index == 300000:
        print("Index currently at", index)
    elif index == 400000:
        print("Index currently at", index)
    elif index == 500000:
        print("Index currently at", index)
    elif index == 1000000:
        print("Index currently at", index)
    elif index == 1500000:
        print("Index currently at", index)
    elif index == 2000000:
        print("Index currently at", index)
    elif index == 4000000:
        print("Index currently at", index)

per0 = (zero / index)
per1 = (one / index)
per2 = (two / index)
per3 = (three / index)
per4 = (four / index)
per5 = (five / index)
per6 = (six / index)
per7 = (seven / index)
per8 = (eight / index)
per9 = (nine / index)

per_list = [per0,per1,per2,per3,per4,per5,per6,per7,per8,per9]

counter = 0
for n in per_list:
    n *= 100
    print(counter, "=", n, "%", )
    if (n > 10.05):
        print (counter, "is high")
    elif (n < 9.98):
        print (counter, "is low")
    counter += 1