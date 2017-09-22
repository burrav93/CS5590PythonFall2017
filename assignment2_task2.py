
string1 = int(input("Enter a number:")) ###INPUT TO THE USER##

result = dict()   ####ALLOCATING A NEW DICTIONARY##
for j in range(1, string1 + 1):   ### THE RANGE AFTER YOU INPUT A NUMBER STARTING FROM 1
    result[j] = j * j     ###RESULT GIVING SQUARE OF THE NUMBERS SEQUENTIALLY STARTING FROM 1 TO THE NUMBER USER INPUTS

print(result)