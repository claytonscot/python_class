__author__ = 'Clay H'

#This program reads each player's name and golf score as keyboard input
#The records are written to golf.txt

def main():

    next = "yes"

    while next != "no" and next != "No" and next != "NO":
        golf_write()
        next = input("Would you like to enter another player?")



    print("Thank you")




def golf_write():
    scorefile = open('golf.txt', 'a')
    name = input("Please enter your name: ") + "\t"
    score = input("please enter your score: ") + "\n"
    scorefile.write(name)
    scorefile.write(score)
    scorefile.close()

main()

#Question: since only strings can be written to files, is it necessary to convert
#the score to an int, only to convert it back again? I guess it would make
#sense, but only for the sake of letting the try except do it's job. Otherwise
#it's not really possible to crash this program.