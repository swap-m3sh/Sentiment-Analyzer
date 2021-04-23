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

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)

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

with open('./api/model/tok.pickle',mode='rb') as handle:
    tok = pickle.load(handle)

model = tf.keras.models.load_model('./api/model/model.h5')

EMO_UNICODE = {
    u':angry:': u'\U0001F620', # angry
    u':very angry: ': u'\U0001F47F', #angry face with horns
    u':suprised: ': u'\U0001F627',
    u':yellow love: ': u'\U0001F49B', # yellow_heart
    u':worried:': u'\U0001F61F',
    u':winking face:': u'\U0001F609',
    u':shocked:': u'\U0001F640', #weary cat face
    u':waving hand:': u'\U0001F44B',#waving hand
    u':warning:': u'\U000026A0',
    u':unamused face:': u'\U0001F612',
    u':tired face:': u'\U0001F62B',
    u':good:': u'\U0001F44D',#thumbs_up
    u':upset:': u'\U0001F44E',
    u':smiling cat face with heart eyes:': u'\U0001F63B',
    u':smiling cat face with open mouth:': u'\U0001F63A',
    u':smiling face:': u'\U0000263A',
    u':smiling face with halo:': u'\U0001F607',
    u':smiling face with heart-eyes:': u'\U0001F60D',
    u':smiling face with horns:': u'\U0001F608',
    u':smiling face with open_mouth:': u'\U0001F603',
    u':smiling face with open mouth closed eyes:': u'\U0001F606',
    u':smiling face with open mouth & cold sweat:': u'\U0001F605',
    u':smiling face with open mouth & smiling eyes:': u'\U0001F604',
    u':smiling face with smiling eyes:': u'\U0001F60A',
    u':pig face:': u'\U0001F437',
    u':person gesturing NO:': u'\U0001F645',
    u':person gesturing OK:': u'\U0001F646',
    u':person frowning:': u'\U0001F64D',
    u':face blowing a kiss:': u'\U0001F618',
    u':face savouring delicious_food:': u'\U0001F60B',
    u':face screaming in fear:': u'\U0001F631',
    u':face with cold sweat:': u'\U0001F613',
    u':face with head bandage:': u'\U0001F915',
    u':face with medical mask:': u'\U0001F637',
    u':face with open mouth:': u'\U0001F62E',
    u':face with open mouth & cold sweat:': u'\U0001F630',
    u':face with rolling eyes:': u'\U0001F644',
    u':face with steam from nose:': u'\U0001F624',
    u':face with stuck out tongue:': u'\U0001F61B',
    u':face with stuck out tongue & closed eyes:': u'\U0001F61D',
    u':face with stuck out tongue & winking eye:': u'\U0001F61C',
    u':face with tears of joy:': u'\U0001F602',
    u':face with thermometer:': u'\U0001F912',
    u':face without mouth:': u'\U0001F636',
    u':disappointed face:': u'\U0001F61E',
    u':disappointed but relieved face:': u'\U0001F625',
    u':hopefull:': u'\U0001F91E', # crossed fingers
    u':confused face:': u'\U0001F615',
    u':appreciate:': u'\U0001F44F', #clapping hands
    u':blue heart:': u'\U0001F499',
    u':astonished face:': u'\U0001F632',
    
}

UNICODE_EMO = {v: k for k, v in EMO_UNICODE.items()}

def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = re.sub(r'('+emot+')', " ".join(UNICODE_EMO[emot].replace(","," ").replace(":"," ").split()), text)
    return text

def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def cleaning_message(df):
    df=df.apply(lambda x: convert_emojis(x))
    df=df.apply(lambda x: remove_emojis(x))
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

    dt = cleaning_message(data)
    max_len = 1000
    tok.fit_on_texts(dt)
    sequences = tok.texts_to_sequences(dt)
    sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)
    y_bar= model.predict(sequences_matrix)
    y_bar = (y_bar > 0.5)
    y_bar = y_bar*1   #changing True to 1 and False to 0
    columns = ['value']
    index = []
    for i in range(y_bar.size):
        index.append(i)
    df = pd.DataFrame(y_bar, columns=columns)
    df['index'] = index
    df['comment'] = data
    df= df.reindex(columns=['index', 'comment', 'value'])
    df['value'] = df['value'].apply(lambda x: "Positive Comment" if( x==1) else "Negative Comment") 

    result = df.to_json(orient="records")
    return result

if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    print(analyzer(arg))