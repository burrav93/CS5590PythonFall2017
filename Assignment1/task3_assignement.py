list=[]     #It is an empty list
for i in range(700,1700):   #for loop to check the range between 700 to 1700
    if(i%5==0)and (i%2==0): #if condition to see if it is divisible by 5 and multiple of 2
        list.append(i) # appending next element into the existing list
print("The numbers which are divisible by 5 and multiple of 2, between 700 and 1700 are",list)#prints the output
