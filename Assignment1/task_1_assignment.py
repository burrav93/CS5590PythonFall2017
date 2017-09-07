import re    #importing regular expression to allow special characters
import string  #importing string module

frequency = {} #empty set
input_text = open('C:\\Users\\bvkka\\Desktop\\para', 'r')#Open the text file location stored on your desktop and then read it
text_string = input_text.read().lower()    #store the text file in a string variable, here all the letters in our document are turned into lower case letters
pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)#return all words with number of characters in the range [3-15], starting from 3 will help in avoiding words that may skip small words and words having a length larger than 15 might be incorrect. Here \b is word boundary

for word in pattern:
    count = frequency.get(word, 0) #intially it sets to 0
    frequency[word] = count + 1 #and then the count increases

list_freq = frequency.keys() #concept of pythons dictionaries(read online)

for words in list_freq:
    print  (words, frequency[words]) #finally in order to get the word and its frequency