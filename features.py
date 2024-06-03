import nltk
nltk.download('stopwords')

from fuzzywuzzy import fuzz
from nltk.corpus import stopwords

# List of negative words
negative_words = ['not', 'no', 'never', 'none', 'neither', 'nor', 'cannot', 'couldn\'t', 'didn\'t', 'doesn\'t', 'aren\'t', 'isn\'t', 'wasn\'t', 'won\'t', 'wouldn\'t']
nltk_stopwords = set(stopwords.words('english'))

def count_negative_and_stopwords(sentence):
    words = sentence.split()

    # Count the number of negative words in the sentence
    negative_word_count = sum(1 for word in words if word.lower() in negative_words)
    stopwords_count = sum(1 for word in words if word.lower() in nltk_stopwords)

    return negative_word_count, stopwords_count

def get_features(text1, text2):
    # Length of questions
    len1 = len(text1)
    len2 = len(text2)

    #No of words
    word_len1 = len(text1.split())
    word_len2 = len(text2.split())

    # No of common words
    set1 = set(text1.split())
    set2 = set(text2.split())
    common_word_ratio =  len(set1 & set2) / (word_len1 + word_len2 + 0.0000001)

    #First and last words
    f_word_same = 0
    l_word_same = 0
    if(len(text1.split()) and len(text2.split())):
        f_word_same = int(text1.split()[0] == text2.split()[0])
        l_word_same = int(text1.split()[-1] == text2.split()[-1])

    #No of negative words and stopwords
    negative_len1, stopwords_len1 = count_negative_and_stopwords(text1)
    negative_len2, stopwords_len2 = count_negative_and_stopwords(text2)

    #Fuzzywuzzy
    fuzz_ratio = fuzz.ratio(text1, text2)
    fuzz_partial = fuzz.partial_ratio(text1, text2)
    fuzz_sort = fuzz.token_sort_ratio(text1, text2)
    fuzz_set = fuzz.token_set_ratio(text1, text2)

    return [len1, len2, word_len1, word_len2, common_word_ratio, f_word_same, l_word_same,
            negative_len1, negative_len2, stopwords_len1, stopwords_len2,
            fuzz_ratio, fuzz_partial, fuzz_sort, fuzz_set]



def add_features(df):
    len_features = ['len1', 'len2', 'word_len1', 'word_len_2', 'common_words_ratio', 'f_word_same', 'l_word_same',
                    'negative_len1', 'negative_len2', 'stopwords_len1', 'stopwords_len2', 'fuzz_ratio', 'f_partial', 'f_sort', 'f_set']

    df[len_features] = df.apply(lambda row: get_features(row['question1'], row['question2']), axis=1, result_type='expand')
    return df