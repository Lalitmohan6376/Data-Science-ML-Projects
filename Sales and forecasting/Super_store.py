import pandas as pd
import numpy as np

df = pd.read_csv("Sample_Superstore_clean.csv", encoding="latin-1")

def check_values(df):
  return df.isnull().sum(),df.duplicated().sum(),df.dtypes


missing_values,duplicate,data_type = check_values(df)

num_col = df.select_dtypes(include=['int64','float64','float32'])

Q1 = num_col.quantile(0.25)
Q3 = num_col.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = ((num_col < lower_bound) | (num_col > upper_bound))

print(outliers.sum())

for col in num_col:
    df[col] = np.log1p(df[col])


Q1 = num_col.quantile(0.25)
Q3 = num_col.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = ((num_col < lower_bound) | (num_col > upper_bound))

print(outliers.sum())

drop_col = ['Row ID','Order ID','Customer ID','Ship Date','Customer Name','Order Date','Product ID','Postal Code','Product Name','Country']
df = df.drop(columns=drop_col)

cat_col = df.select_dtypes(include=['object'])

for col in cat_col:
    df[col] = df[col].str.strip()

# import Machine learning Libraries

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.metrics import r2_score,precision_score,mean_absolute_error,mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pickle

df = df.sort_values(by=['Year','month'])

X = df.drop('Sales',axis=1)
y = df['Sales']

split_index = int(len(df) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]

y_train = y[:split_index]
y_test = y[split_index:]

X_train.isnull().sum()

num_cols = X_train.select_dtypes(include=['int64','float64','float32']).columns
cat_cols = X_train.select_dtypes(include=['object']).columns


num_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('scale',StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('Encoder',OneHotEncoder(handle_unknown='ignore'))
])


preprocessor = ColumnTransformer([
    ('num',num_pipeline,num_cols),
    ('cat',cat_pipeline,cat_cols)
])


pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model',RandomForestRegressor(random_state=42,n_estimators=50,max_depth=10,n_jobs=-1))
])


pipeline.fit(X_train,y_train)

y_pred = pipeline.predict(X_test)

r2 = r2_score(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)

print("R2 score",r2)
print("MAE",mae)
print("MSE",mse)

with open("model.pkl","wb") as f:
    pickle.dump(pipeline,f)

print("✅ Sucessfully Exported")