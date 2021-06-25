from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import numpy as np
import pandas as pd

# check for missing values
df = pd.read_csv('')
df.dropna(inplace=True)
df.isnull().sum()

blanks = []

for i,lb,rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)

df.drop(blanks, inplace=True)


X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

# pipeline object

text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

text_clf.fit(X_train,y_train)

predictions = text_clf.predict(X_test)







#
# vocab = {}
# i = 1
# one = ['']+[0]*len(vocab)
# with open('') as f:
#     x = f.read().lower().split()
#
# for word in x:
#     if word in vocab:
#         continue
#     else:
#         one[vocab[word]] = i
#         i+=1
#
# import numpy as np
# import pandas as pd
#
# df = pd.read_csv()
# df.head()

