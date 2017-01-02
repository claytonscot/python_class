def main():

    print("This program tests 4 two-dimensional lists to see if their values\n"
          "all add up to the same sum in a loshu square puzzle.\n")
    list_seq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list_rev = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    list_2d = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]
    list_2a = [[4, 3, 8],[9, 5, 1],[2, 7, 6]]

    trial_1 = sum_checker(list_2d)
    print("Trial 1: ", end='')
    if trial_1 == True:
        print("You found a solution!")
    else:
        print("Sorry, that doesn't work")




    trial_2 = sum_checker(list_seq)
    print("Trial 2: ", end='')
    if trial_2 == True:
        print("You found a solution!")
    else:
        print("Sorry, that doesn't work")

    trial_3 = sum_checker(list_rev)
    print("Trial 3: ", end='')
    if trial_3 == True:
        print("You found a solution!")
    else:
        print("Sorry, that doesn't work")

    trial_4 = sum_checker(list_2a)
    print("Trial 4: ", end='')
    if trial_4 == True:
        print("You found a solution!")
    else:
        print("Sorry, that doesn't work")




def sum_checker(list_2d):
    first_check = list_2d[0][0] + list_2d[0][1] + list_2d[0][2]
    second_check = list_2d[0][0] + list_2d[1][0] + list_2d[2][0]
    third_check = list_2d[0][0] + list_2d[1][1] + list_2d[2][2]
    fourth_check = list_2d[1][0] + list_2d[1][1] + list_2d[1][2]
    fifth_check = list_2d[2][0] + list_2d[2][1] + list_2d[2][2]
    sixth_check = list_2d[2][0] + list_2d[1][1] + list_2d[0][2]

    if first_check != second_check:
        return False
    elif second_check != third_check:
        return False
    elif third_check != fourth_check:
        return False
    elif fourth_check != fifth_check:
        return False
    elif fifth_check != sixth_check:
        return False
    else:
        return True



main()
