import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix


data=pd.read_csv('credit-card-default prediction.csv' )
features=pd.get_dummies(data)
x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values

from sklearn.preprocessing import Imputer
imp=Imputer(missing_values='NaN', strategy="mean", axis=0)
imp=imp.fit(x[:,])
x[:,]= imp.transform(x[:,])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.1, random_state=0)



#------Feature Scaling---------
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test= sc.transform(x_test)

#--------------Random Forrest--------------
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit( x_train, y_train )
y_pred = classifier.predict( x_test )
cm = confusion_matrix( y_test, y_pred )



with open('check.pk1','wb') as f:
    pickle.dump(classifier,f)
    

