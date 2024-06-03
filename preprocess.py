import string
from nltk.stem import PorterStemmer
import re

def preprocess(text):

    text = str(text)

    #Lowercase
    text = text.lower()

    #Remove html tags
    text = re.sub(r'<.*?>', ' ', text)

    #Remove other Punctuation
    text = re.sub(r'[^\w]', ' ', text)

    #Remove extra space
    text = ' '.join(text.split())

    #Stemming
    stemmer = PorterStemmer()
    text = stemmer.stem(text)


    return text