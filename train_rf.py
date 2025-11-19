import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

# Data Preparation
df = pd.read_csv('heart_failure.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical:
    df[c] = df[c].str.lower().str.replace(' ', '_')

categorical = ['sex', 'chestpaintype', 'restingecg', 'exerciseangina', 'st_slope']
numeric = ['age', 'restingbp', 'cholesterol', 'fastingbs', 'maxhr', 'oldpeak']

# Data Split
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

def train(df_train, y_train):
  train_dicts = df_train[list(categorical) + list(numeric)].to_dict(orient='records')

  dv = DictVectorizer(sparse=False)
  X_train = dv.fit_transform(train_dicts)

  model = RandomForestClassifier(
      n_estimators=10, 
      max_depth=12,         
      random_state=1,  
      min_samples_leaf=1,        
      n_jobs=-1                 
  )
  model.fit(X_train, y_train)

  return dv, model

def predict(df, dv, model):
  dicts = df[list(categorical) + list(numeric)].to_dict(orient='records')
  X = dv.transform(dicts)
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred


#Training and evaluation
y_full_train = df_full_train.heartdisease.values
df_full_train = df_full_train.drop('heartdisease', axis=1)
y_test = df_test.heartdisease.values

dv, model = train(df_full_train, y_full_train) 
y_pred = predict(df_test, dv, model)

auc_test = roc_auc_score(y_test, y_pred)
print(f"AUC Score: {auc_test}")


# Save the model
output_file = 'rf_model.bin' 

with open(output_file, 'wb') as file_out:
  pickle.dump((dv, model), file_out)
print(f"The model is saved to {output_file}")
