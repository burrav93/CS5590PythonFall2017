
string1= input("Enter a string:") ##**input to the user**##
words=[word for word in string1.split(" ")] ##**it will split the string and remove the duplicate words**##
result="".join(sorted(list(set(words))))##**set of words, then it will sort the split words and join them in order **##
print(result)




