import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import json
import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
import warnings
warnings.filterwarnings("ignore")
tf.get_logger().setLevel('ERROR')

import nltk

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

from nltk.corpus import stopwords
stopwords_list = stopwords.words('english')

# Cleaning stopwords
STOPWORDS = set(stopwords.words('english'))
def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

# Cleaning punctuations
import string
english_punctuations = string.punctuation
punctuations_list = english_punctuations
punctuations_list[0:]

def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

# Cleaning URLS
import re
def cleaning_URLs(data):
    return re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',str(data))

# Cleaning Numbers
def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)

# Initializing tokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

# Initializing stemer
from nltk.stem import PorterStemmer
stemer = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [stemer.stem(word) for word in data]
    return data

# Initializing lemmatizer
lm = nltk.WordNetLemmatizer()
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data

import pickle
# with open('/model/tok.pickle', mode='wb') as handle:
#     pickle.dump(tok, handle, protocol = pickle.HIGHEST_PROTOCOL)

with open('model/tok.pickle',mode='rb') as handle:
    tok = pickle.load(handle)

model = tf.keras.models.load_model('model/model.h5')

def cleaning_message(df):
    df=df.str.lower()
    df=df.apply(lambda x: cleaning_stopwords(x))
    df=df.apply(lambda x: cleaning_punctuations(x))
    df=df.apply(lambda x: cleaning_URLs(x))
    df=df.apply(lambda x: cleaning_numbers(x))
    df=df.apply(tokenizer.tokenize)
    df=df.apply(lambda x: stemming_on_text(x))
    df=df.apply(lambda x: lemmatizer_on_text(x))
    return df

def analyzer(data): 
    # Test 
    # t1="I am feeling upset problem sad hate"
    # t2="Happy love cheerful feeling"
  
    # dfd = pd.DataFrame({
    #     'text': [t1,t2]
    # })

    # data = dfd['text']
    data = cleaning_message(data)
    max_len = 1000
    tok.fit_on_texts(data)
    sequences = tok.texts_to_sequences(data)
    sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)

    y_bar= model.predict(sequences_matrix)
    y_bar = (y_bar > 0.5)

    y_bar = y_bar*1

    columns = ['value']
    index = []
    for i in range(y_bar.size):
        index.append(i)
    df = pd.DataFrame(y_bar, columns=columns)
    df['index'] = index
    df= df.reindex(columns=['index', 'value'])

    result = df.to_json(orient="records")
    print(result)
    return result

if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = analyzer(arg)