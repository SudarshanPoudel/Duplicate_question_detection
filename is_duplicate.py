import pickle
import pandas as pd

from features import add_features
from preprocess import preprocess
from vectorizer import vectorize_df


model = pickle.load(open('models/model.pkl','rb'))
def is_duplicate(question1, question2):
    d = pd.DataFrame({'question1': [preprocess(question1)], 'question2': [preprocess(question2)]})
    d = add_features(d)
    d = vectorize_df(d)
    return model.predict(d)[0]