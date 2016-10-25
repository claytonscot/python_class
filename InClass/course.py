__author__ = 'Home'
#uses dictionaries to determine where, when, and with whom a class will be
#based on class name. Hence, CS101 is in all three dictionaries.

def main():
#get dictionaries from functions

    room_numbers = get_room_numbers()

    instructors = get_instructor()

    times = get_time()

    class_info = input('Enter the class number: ')
    my_room = room_numbers[class_info]
    print("Room number: ", my_room)
    my_instructor = instructors[class_info]
    print("Instructor: ", my_instructor)
    my_time = times[class_info]
    print("Time: ", my_time)


def get_room_numbers():
    room_number = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    return room_number

def get_instructor():
    instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    return instructor

def get_time():
    time = {'CS101':'8:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}
    return time




main()