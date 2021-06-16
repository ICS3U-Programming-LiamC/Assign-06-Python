#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 14, 2021
# This program STUFF STUFF

capitalizer = False
capitalizer_test = False


# greets the user when they get in the program
def greeting():
    print("Welcome! This program converts any text into pig latin")
    print("It will save most punctuation that you put at the end of a text")
    print("As well as most punctuation you put inside the text")


# this handles any punctuation that the user tried to add, moving it
# to the end of whatever word then put in
def punctuator(word, puncter):
    global capitalizer
    global capitalizer_test
    word = word.replace(puncter, "")
    word = word + puncter
    # explained in more depth in the c++ project
    # basically if theres a . after the previous word
    # then it will make the next word capitalized
    if (capitalizer is True):
        word = str.upper(word[0]) + word[1:]
        capitalizer = False

    if (capitalizer_test is True):
        capitalizer = True
        capitalizer_test = False
    return word


def swapper(word):
    letter = word[0]
    while True:
        if (letter == 'a'):
            break
        elif (letter == 'e'):
            break
        elif (letter == 'i'):
            break
        elif (letter == 'o'):
            break
        elif (letter == 'u'):
            break
        else:
            word = word[1:] + word[0]
            letter = word[0]
    return word


# main converting function
def latin_converter(user_list):
    # removes all uppercases then splits the words into individual strings
    user_list = str.lower(user_list)
    user_list = list(user_list.split(" "))

    pig_latin_sentence = ""

    # does the rest
    for each in user_list:
        global capitalizer
        global capitalizer_test
        each = each.strip()
        swapped = each
        suffix = ""
        # this code prints from the second character to the last then
        # adds the first character to the end
        letter = swapped[0]
        if (letter == "a"):
            suffix = "way"
        elif(letter == "e"):
            suffix = "way"
        elif(letter == "i"):
            suffix = "way"
        elif(letter == "o"):
            suffix = "way"
        elif(letter == "u"):
            suffix = "way"
        else:
            swapped = swapper(swapped)
            suffix = "ay"

        # adds ay to the end of the words
        pig_latin_word = swapped + suffix

        # defaults punctuation to empty
        punctuation = ""

        # if there is punctuation it sets the variable to that
        if "." in pig_latin_word:
            punctuation = "."
            capitalizer_test = True
        if "!" in pig_latin_word:
            punctuation = "!"
            capitalizer_test = True
        if "?" in pig_latin_word:
            punctuation = "?"
            capitalizer_test = True
        if (":" in pig_latin_word):
            capitalizer_test = True
            punctuation = ":"
        if (";" in pig_latin_word):
            punctuation = ";"
        if ("," in pig_latin_word):
            punctuation = ","

        # if one of these was triggered it will call the function
        # and pass it the punctuation that it detected
        pig_latin_word = punctuator(pig_latin_word, punctuation)

        # starts reconstructing the sentence
        pig_latin_sentence = pig_latin_sentence + " " + pig_latin_word

        # makes the first character uppercase
        final = str.upper(pig_latin_sentence[1]) + pig_latin_sentence[2:]

    # return the result to the main()
    return(final)


def main():
    # gets the string the user wants to convert
    user_input = input("What would you like to convert to pig latin: ")
    # calls the function

    # there seems to be a problem where if you put a space at the end it
    # will crash the program, this stops that from happening
    # there is an easy way to remove the space from the end of the string
    # however it seems to only exist in python 3.9 which is not on here

    user_input = user_input.strip()
    result = latin_converter(user_input)
    # prtints the resutl to the user
    print(result)


# starts everyting
if __name__ == "__main__":
    greeting()
    main()
