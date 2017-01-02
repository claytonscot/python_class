__author__ = 'Home'

def main():
    #pop_list is a list with 41 items
    pop_list = get_pop_list()
    average = avg_annual_change(pop_list)
    #average is a list with only 40 items, since there is no growth percentage for the final year
    print("The following program calculates the average annual growth rate of the\n"
          "United States from 1950-1990 (USPopulation.txt) and analyzes the largest and smallest\n"
          "population growth rates.\n")

    greatest_increase = get_greatest_increase(average)
    print("The greatest population increase was ", format(greatest_increase, '.3'), "%.", sep='')

    lowest_increase = get_lowest_increase(average)
    print("The lowest population increase was ", format(lowest_increase, '.3'), "%.", sep='')


#reads USPopulation.txt into infile and returns it to main
def get_pop_list():
    infile = open('USPopulation.txt', 'r')
    string_input = list(infile.readlines())
    infile.close()
#    print(string_input)

    index = 0
    for n in string_input:
        string_input[index] = int(n)
        index += 1
#    print(string_input)
    return string_input

#creates and returns a list with the annual change percentage from year to year.
def avg_annual_change(pop_list):
    index = 0
    for n in pop_list:

        #if statment to accomodate the [index + 1] and avoid range error
        if index < (len(pop_list) -1):
            percent = (((pop_list[index + 1] - pop_list[index]) / pop_list[index])) * 100
            pop_list[index] = percent
            index += 1
    return pop_list

def get_greatest_increase(average):
#    unsorted = average
    low_high = sorted(average)
    #returns last item in sorted percentage list
    return low_high[len(average) - 2]

def get_lowest_increase(average):
    low_high = sorted(average)
    #returns first item of sorted list of percentages
    return low_high[0]



main()