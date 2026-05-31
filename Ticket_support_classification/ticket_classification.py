import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("all_tickets_processed_improved_v3.csv")
df.head()


df.columns = df.columns.str.strip().str.lower()
df = df.rename(columns={
    'document': 'text',
    'topic_group': 'target'
})

df = df[['text','target']]
df = df.dropna()


counts = df['target'].value_counts()

valid_classes = counts[counts > 2000].index
df = df[df['target'].isin(valid_classes)]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df['text'] = df['text'].apply(clean_text)

X = df['text']
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=30000,
        ngram_range=(1,2),
        min_df=3,
        max_df=0.9
    )),
    ('model', LinearSVC(
        C=3,
        class_weight='balanced'
    ))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

