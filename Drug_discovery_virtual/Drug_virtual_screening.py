# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset load
def read_data():
    return pd.read_csv("drug_ discovery _virtual_screening.csv")

df = read_data()

df.head(10)

def values_check(df):
    return df.isnull().sum(),df.duplicated().sum(),df.dtypes

missing_values,duplicate,data_value = values_check(df)

print(missing_values)
print("Duplicates values",duplicate)
print(data_value)

plt.Figure(figsize=(6,5))
df['active'].value_counts().plot(kind="bar")
plt.xlabel("Active")
plt.ylabel("Count")
plt.title("Target Distribution")
plt.show()

# import machine learning library
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

X = df.drop(['compound_id','protein_id','active','binding_affinity'],axis=1)
y = df['active']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

num_cols = X_train.select_dtypes(include=['float64','int64']).columns
cat_cols = X_train.select_dtypes(include=['object']).columns

num_pipeline = Pipeline([
    ('num',SimpleImputer(strategy="median")),
    ('scale', StandardScaler())
])

cat_pipeline = Pipeline([
    ('cat',SimpleImputer(strategy="most_frequent")),
    ('encode', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num',num_pipeline,num_cols),
    ('cat',cat_pipeline,cat_cols)
])

pipeline = Pipeline([
    ('preprocessor',preprocessor),
    ('smote',SMOTE(random_state=42)),
    ('model',RandomForestClassifier(n_estimators=20,max_depth=5,random_state=42))
])

try:
    pipeline.fit(X_train,y_train)
except:
    print("Error")

y_pred = pipeline.predict(X_test)
check = accuracy_score(y_test,y_pred)

print(check)

cm = confusion_matrix(y_test,y_pred)
print(cm)

print(classification_report(y_test,y_pred))