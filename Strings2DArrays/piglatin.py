__author__ = 'Clay Hougham'
#This program takes a phrase from the user and converts it into pig latin

def main():

    words = input("Enter a word or phrase to be translated into Pig Latin: ")
    lower_case_words = words.lower()
    pig_latin = convert_string(lower_case_words)
    print(pig_latin)

def convert_string(lower_case_words):

    split = lower_case_words.split()
    phrase = ''
    for n in split:
        first_letter = n[0:1]
        strip_word = n.replace(n[:1], '')
        suffix = first_letter + "ay"
        pig_word = strip_word + suffix
        phrase += pig_word + ' '
    return phrase

main()