import pandas as pd 
import pickle 
from sklearn.ensemble import RandomForestClassifier

df_train = pd.read_csv("trainexit.csv")
df_train.dropna(inplace=True)
df_train = df_train.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1)

df_train = pd.get_dummies(df_train)
df_train = df_train.drop(['Sex_female', 'Embarked_C'], axis=1)

X = df_train.drop('Survived', axis = 1)
y = df_train['Survived']

model = RandomForestClassifier()
model.fit(X, y)

model_filename = 'model.pkl'
with open(model_filename, 'wb') as f: 
    pickle.dump(model, f)