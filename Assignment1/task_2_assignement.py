import string #importing the string module containing a number of useful constant and classes
all_letters_of_the_alphabet = set(string.ascii_lowercase)#the lower case letters are chosen in the alphabets we are considering
string_input="abcdefghijklmnopqrstuvwxyz" #giving input in a string variable
print(set(string_input.lower())>=all_letters_of_the_alphabet)#it checks if the string input has all the lower case alphabets in it and prints output as true or false
string_input="bvkkarthik"
print(set(string_input.lower())>=all_letters_of_the_alphabet)#it checks if the string input has all the alphabets in it and prints output as true or false
string_input="PYTHONANDDEEPLEARNING"
print(set(string_input.lower())>=all_letters_of_the_alphabet)#it checks if the string input has all the alphabets in it and prints output as true or false
