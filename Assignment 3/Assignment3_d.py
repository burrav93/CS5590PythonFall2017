import nltk
from nltk.corpus import wordnet as wn
import re, collections
from nltk.book import FreqDist

file=open("got.txt")
t=file.read()

#lemmetization
from nltk.stem import WordNetLemmatizer
lemmetizer=WordNetLemmatizer()
print(lemmetizer.lemmatize(t))

#POS tagging
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
s=nltk.pos_tag(nltk.word_tokenize(t))
print(s)

#removing verbs from input file
file_without_verbs = [word for word,tag in s if tag != 'VBG' and tag != 'VBZ' and tag!='VBN']
z=' '.join(file_without_verbs)         # z is the file without verbs
print(z)
s1=nltk.pos_tag(nltk.word_tokenize(z))
print(s1)                              # you can see in the output that all the verbs are removed





fdist=FreqDist(z)
print(fdist)
q=fdist.most_common(5)
print(q)

#word frequency of remaining words
def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())
WORD_COUNTS = collections.Counter(tokens(z))
print (WORD_COUNTS)
print (WORD_COUNTS.most_common(5))


##go through the original file

file=open("got.txt")
t=file.read()


