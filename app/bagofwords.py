import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
import re
import numpy as np

sentences = ["[Simple Plot] | [ELDRICT HORROR CORE] |  |",  "A Historian |  infernal |  Wants to erase a memory of-with |  A discovery |  innovative |  But it will dive them to the brink of madness"]

corpus = pd.Series(sentences)
corpus

preprocessed_corpus = preprocess(corpus,
                                 keep_list = common_dot_words,
                                 stemming = False,
                                 stem_type = None,
                                 lemmatization = True,
                                 remove_stopwords = True)