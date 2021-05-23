import numpy as np
import pandas as pd
import pickle
from azureml.core import Run

run = Run.get_context()


if __name__ == "__main__":

    data = pd.read_csv('https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso2/master/Datasets/titanic.csv')

    data.drop(['PassengerId','Name','Ticket','Cabin','Embarked'], axis=1, inplace=True)

    

    from sklearn.impute import SimpleImputer
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')

    data.loc[data['Survived']==1,['Age']]=imp.fit_transform(data.loc[data['Survived']==1,['Age']])
    data.loc[data['Survived']==0,['Age']]=imp.fit_transform(data.loc[data['Survived']==0,['Age']])

    data=pd.get_dummies(data)

    data['Family_size']=data['SibSp'] + data['Parch']
    data.drop(['SibSp', 'Parch'] ,axis=1, inplace=True)


    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,1:], data.iloc[:,0],test_size = 0.2, random_state=0)


    y_train=np.array(y_train)
    y_test=np.array(y_test)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier()

    rf.fit(X_train_scaled, y_train)

    y_predi = rf.predict(X_test_scaled)

    from sklearn.metrics import accuracy_score

    auc=accuracy_score(y_test,y_predi)

    print(auc)

    #Registro
    with open('./outputs/titanic-model.pkl', 'wb') as model_pkl:
        pickle.dump(rf, model_pkl)
        