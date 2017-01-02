__author__ = 'Clay H'

def main():

    #Answer List. 20 items in list.
    my_answer = get_my_answer()
    number_correct = get_number_correct(my_answer)
    print("You got", number_correct, "out of 20.")
    if number_correct >= 15:
        print("You passed the test!")
    else:
        print('FAILURE')

#Passes in my_answer to calculate the number of correct answers.
def get_number_correct(my_answer):
    index = 0
    number_correct = 0
    answer_key = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D','A']

    while index <= 19:
        #These print functions are just to show that both lists are being compared item by item.
        print (answer_key[index], my_answer[index])
        #Compares each list item. Each time an answer is identical to the answer key,
        #the number correct increases by 1
        if answer_key[index] == my_answer[index]:
            print("Correct!")
            number_correct += 1
        else:
            print("Wrong")
        index += 1
    return number_correct

#reads useranswers.txt and returns the filecontents
def get_my_answer():
    infile = open('useranswers.txt', 'r')
    filecontents = infile.read()
    return filecontents
    infile.close()

main()