__author__ = 'Clay H'
#Compares an Answer Key to contents of useranswers.txt
#and determines pass or fail

def main():

    index = 0
    number_correct = 0
    #Answer List. 20 items in list.
    answer_key = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D','A']
    my_answer = get_my_answer()

    while index <= 19:
        print (answer_key[index], my_answer[index])
        if answer_key[index] == my_answer[index]:
            print("Correct!")
            number_correct += 1
        else:
            print("Wrong")
        index += 1
    print("You got", number_correct, "out of 20.")
    if number_correct >= 15:
        print("You passed the test!")
    else:
        print('FAILURE')

def get_my_answer():
    infile = open('useranswers.txt', 'r')
    filecontents = infile.read()
    return filecontents
    infile.close()

main()