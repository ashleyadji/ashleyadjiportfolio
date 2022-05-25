import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('flowers.csv')
x = data.drop('species',axis = 1)
y = data['species']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 2983)

model = MultinomialNB()
#takes no parameters

model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(accuracy_score(y_test,y_pred))