import pickle
import pandas as pd

vectorizer = pickle.load(open('models/vectorizer.pkl','rb'))

def vectorize_df(df):
    vector_array = vectorizer.transform(df['question1'] + df['question2']).toarray()
    vector_df = pd.DataFrame(vector_array, columns=vectorizer.get_feature_names_out())
    df = pd.concat([df.reset_index(drop=True),vector_df], axis=1)
    df.drop(columns=['question1', 'question2'], inplace=True)
    return df