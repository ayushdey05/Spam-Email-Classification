# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# %%
df = pd.read_csv('spam.csv', encoding='latin1')

# %%
df.head(5)

# %%
df.shape

# %%
df.info()

# %%
df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)


# %%
df.head()

# %%
df.rename(columns={'v1':'Target','v2':'Text'},inplace=True)

# %%
df.head()

# %%
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# %%
df['Target']=encoder.fit_transform(df['Target'])

# %%
df.head()

# %%
df.isnull().sum()

# %%
df.duplicated().sum()

# %%
df.drop_duplicates(keep='first')

# %%
df['Target'].value_counts()

# %%
plt.pie(df['Target'].value_counts(), labels=['ham','spam'],autopct="%0.2f")
plt.show()

# %%
# Data is imbalanced 

# %%
import nltk
nltk.download('punkt')


nltk.download('punkt')
nltk.download('punkt_tab')

# %%
df['num_words'] = df['Text'].apply(lambda x: len(nltk.word_tokenize(x)))

# %%
df['num_sentences']=df['Text'].apply(lambda x:int(len(nltk.sent_tokenize(x))))

# %%
df.head()

# %%
df[['num_char','num_words','num_sentences']].describe()

# %%
#For Ham Messages 
df[df['Target']==0][['num_char','num_words','num_sentences']].describe()

# %%
# For Spam Messages 
df[df['Target']==1][['num_char','num_words','num_sentences']].describe()

# %%
sns.histplot(df[df['Target']==0]['num_char'])
sns.histplot(df[df['Target']==1]['num_char'],color='red')

# %%
sns.histplot(df[df['Target']==0]['num_words'])
sns.histplot(df[df['Target']==1]['num_words'],color='red')

# %%
sns.histplot(df[df['Target']==0]['num_sentences'])
sns.histplot(df[df['Target']==1]['num_sentences'],color='red')

# %%
sns.pairplot(df,hue='Target')

# %%
Data Preprocessing 
1. Lower Case 
2. Tokenization 
3. Remove special Charecters 
4. Remove Stop words and Punctuations 
5. Stemming 

# %%
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)

# %%
import string
from nltk.corpus import stopwords
nltk.download('stopwords')

# %%
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # for tokenization


# %%
transform_text("I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today.")

# %%
df['Text'][10]

# %%
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
ps.stem('loving')

# %%
df['transformed_text'] = df['Text'].apply(transform_text)

# %%
df.head()

# %%
spam_corpus = []
for msg in df[df['Target'] == 1]['transformed_text'].tolist():
    for word in msg.split():
        spam_corpus.append(word)

# %%
len(spam_corpus)

# %%
ham_corpus = []
for msg in df[df['Target'] == 0]['transformed_text'].tolist():
    for word in msg.split():
        ham_corpus.append(word)

# %%
len(ham_corpus)

# %%
df.head()

# %% [markdown]
# Model Building 
# 

# %%
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = CountVectorizer()
tfidf = TfidfVectorizer(max_features=3000)

# %%
X = tfidf.fit_transform(df['transformed_text']).toarray()

# %% [markdown]
# 

# %%

X.shape

# %%
y = df['Target'].values

# %%
from sklearn.model_selection import train_test_split

# %%
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

# %%
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score

# %%
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

# %%
gnb.fit(X_train,y_train)
y_pred1 = gnb.predict(X_test)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
print(precision_score(y_test,y_pred1))

# %%
mnb.fit(X_train,y_train)
y_pred2 = mnb.predict(X_test)
print(accuracy_score(y_test,y_pred2))
print(confusion_matrix(y_test,y_pred2))
print(precision_score(y_test,y_pred2))

# %%
bnb.fit(X_train,y_train)
y_pred3 = bnb.predict(X_test)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
print(precision_score(y_test,y_pred3))

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
#from xgboost import XGBClassifier

# %%
svc = SVC(kernel='sigmoid', gamma=1.0)
knc = KNeighborsClassifier()
mnb = MultinomialNB()
dtc = DecisionTreeClassifier(max_depth=5)
lrc = LogisticRegression(solver='liblinear', penalty='l1')
rfc = RandomForestClassifier(n_estimators=50, random_state=2)
abc = AdaBoostClassifier(n_estimators=50, random_state=2)
bc = BaggingClassifier(n_estimators=50, random_state=2)
etc = ExtraTreesClassifier(n_estimators=50, random_state=2)
gbdt = GradientBoostingClassifier(n_estimators=50,random_state=2)

# %%
clfs = {
    'SVC' : svc,
    'KN' : knc, 
    'NB': mnb, 
    'DT': dtc, 
    'LR': lrc, 
    'RF': rfc, 
    'AdaBoost': abc, 
    'BgC': bc, 
    'ETC': etc,
    'GBDT':gbdt,
    #'xgb':xgb
}

# %%
def train_classifier(clf,X_train,y_train,X_test,y_test):
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    precision = precision_score(y_test,y_pred)
    
    return accuracy,precision

# %%
train_classifier(svc,X_train,y_train,X_test,y_test)


# %%
accuracy_scores = []
precision_scores = []

for name,clf in clfs.items():
    
    current_accuracy,current_precision = train_classifier(clf, X_train,y_train,X_test,y_test)
    
    print("For ",name)
    print("Accuracy - ",current_accuracy)
    print("Precision - ",current_precision)
    
    accuracy_scores.append(current_accuracy)
    precision_scores.append(current_precision)

# %%
performance_df = pd.DataFrame({'Algorithm':clfs.keys(),'Accuracy':accuracy_scores,'Precision':precision_scores}).sort_values('Precision',ascending=False)

# %%

performance_df

# %%
performance_df1 = pd.melt(performance_df, id_vars = "Algorithm")
performance_df1

# %%
sns.catplot(x = 'Algorithm', y='value', 
               hue = 'variable',data=performance_df1, kind='bar',height=5)
plt.ylim(0.5,1.0)
plt.xticks(rotation='vertical')
plt.show()

# %% [markdown]
# MODEL IMPROVEMENT 

# %%
temp_df = pd.DataFrame({'Algorithm':clfs.keys(),'Accuracy_max_ft_3000':accuracy_scores,'Precision_max_ft_3000':precision_scores}).sort_values('Precision_max_ft_3000',ascending=False)

# %%
temp_df = pd.DataFrame({'Algorithm':clfs.keys(),'Accuracy_scaling':accuracy_scores,'Precision_scaling':precision_scores}).sort_values('Precision_scaling',ascending=False)

# %%
new_df = performance_df.merge(temp_df,on='Algorithm')

# %%
new_df_scaled = new_df.merge(temp_df,on='Algorithm')

# %%
temp_df = pd.DataFrame({'Algorithm':clfs.keys(),'Accuracy_num_chars':accuracy_scores,'Precision_num_chars':precision_scores}).sort_values('Precision_num_chars',ascending=False)

# %%
new_df_scaled.merge(temp_df,on='Algorithm')

# %%
# Voting Classifier
svc = SVC(kernel='sigmoid', gamma=1.0,probability=True)
mnb = MultinomialNB()
etc = ExtraTreesClassifier(n_estimators=50, random_state=2)

from sklearn.ensemble import VotingClassifier

# %%
voting = VotingClassifier(estimators=[('svm', svc), ('nb', mnb), ('et', etc)],voting='soft')

# %%
voting.fit(X_train,y_train)


# %%
y_pred = voting.predict(X_test)
print("Accuracy",accuracy_score(y_test,y_pred))
print("Precision",precision_score(y_test,y_pred))

# %%
# Applying stacking
estimators=[('svm', svc), ('nb', mnb), ('et', etc)]
final_estimator=RandomForestClassifier()

# %%
from sklearn.ensemble import StackingClassifier

# %%
clf = StackingClassifier(estimators=estimators, final_estimator=final_estimator)

# %%
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy",accuracy_score(y_test,y_pred))
print("Precision",precision_score(y_test,y_pred))

# %%
import pickle
pickle.dump(tfidf,open('vectorizer.pkl','wb'))
pickle.dump(mnb,open('model.pkl','wb'))

# %%



