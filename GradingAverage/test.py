__author__ = 'Home'

#This program accepts 5 test scores from the user
#and calculates the average.

def main():
    score1 = int(input("Please enter score 1: "))
    score2 = int(input("Please enter score 2: "))
    score3 = int(input("Please enter score 3: "))
    score4 = int(input("Please enter score 4: "))
    score5 = int(input("Please enter score 5: "))
    print()

    average = calc_average(score1, score2, score3, score4, score5)
    print("The average grade was: ", average)

    print("The following letter grades were received:")
    grade1 = determine_grade(score1)
    print(grade1)
    grade2 = determine_grade(score2)
    print(grade2)
    grade3 = determine_grade(score3)
    print(grade3)
    grade4 = determine_grade(score4)
    print(grade4)
    grade5 = determine_grade(score5)
    print(grade5)

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average
def determine_grade(grade):
    if grade >= 90:
        letter = "A"
        return letter
    elif grade >= 80:
        letter = "B"
        return letter
    elif grade >= 70:
        letter = "C"
        return  letter
    elif grade >= 60:
        letter = "D"
        return letter
    else:
        letter = "F"
        return letter

main()