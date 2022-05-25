import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


#unacc, acc, good, vgood
#labels = acceptability
#features = buying,maintenance,doors,persons,lug boot,safety,acceptability
#both strings and numbers, translate strings into numbers

#translating
buying_maintenance = {'vhigh':0,'high':1,'med':2,'low':3}
doors = {'2':2,'3':3,'4':4,'5more':5}
persons = {'2':2,'4':4,'more':5}
lugboot = {'small':0,'med':1,'big':2}
#fix: lug boot vs lugboot
safety = {'low': 3,'med':2,'high':1}
cleanupnums = {'buying':buying_maintenance,'maintenance':buying_maintenance,'doors':doors,'persons':persons,'lugboot':lugboot,'safety':safety}

data = pd.read_csv('car.csv')
#replace
data.replace(cleanupnums,inplace = True)

#build feature vectors(x) and labels(y)
#drop acceptability bc its a label, not a feature
x = data.drop('acceptability',axis = 1)
y = data['acceptability']

#split into training and test
#returns 4 (x_train,x_test,y_train,y_test), accepts 4 arguments (x,y,test_size (percent in decimal form) ,random_state = any number)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 2983)

#trains classifier
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(x_train,y_train)

print(x_test)
#run classifier, 
y_pred = knn.predict(x_test)
#test against y_test data, return decimal accuracy score
print(accuracy_score(y_test,y_pred))

#Data Point [0,0,2,2,0,3] is unacc
#buying:vhigh, maintenance:vhigh, doors, persons, lugboot:small, safety:low

#how do you use classifiers to test above point?
datapoint = [0,0,2,2,0,3]
y_pred = knn.predict([datapoint])[0]
print("Data Point [0,0,2,2,0,3] is")
print(y_pred)








