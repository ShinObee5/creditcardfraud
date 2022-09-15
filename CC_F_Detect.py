import pandas as pd
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score,confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
data=pd.read_csv("creditcard.csv")
sc = StandardScaler()
amount = data['Amount'].values
data['Amount'] = sc.fit_transform(amount.reshape(-1, 1))
data.drop(['Time'], axis=1, inplace=True)
data.drop_duplicates(inplace=True)
X = data.drop('Class', axis = 1).values
y = data['Class'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)
#Decision Tree
DT = DecisionTreeClassifier(max_depth = 4, criterion = 'entropy')
DT.fit(X_train, y_train)
dt_yhat = DT.predict(X_test)
print('Accuracy score of the Decision Tree model is {}'.format(accuracy_score(y_test, dt_yhat)))

print('F1 score of the Decision Tree model is {}'.format(f1_score(y_test, dt_yhat)))

confusion_matrix(y_test, dt_yhat, labels = [0, 1])

#KNN
n = 7
KNN = KNeighborsClassifier(n_neighbors = n)
KNN.fit(X_train, y_train)
knn_yhat = KNN.predict(X_test)

print('Accuracy score of the K-Nearest Neighbors model is {}'.format(accuracy_score(y_test, knn_yhat)))

print('F1 score of the K-Nearest Neighbors model is {}'.format(f1_score(y_test, knn_yhat)))

#Logistic Regression


lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_yhat = lr.predict(X_test)

print('Accuracy score of the Logistic Regression model is {}'.format(accuracy_score(y_test, lr_yhat)))

print('F1 score of the Logistic Regression model is {}'.format(f1_score(y_test, lr_yhat)))

#SVM
svm = SVC()
svm.fit(X_train, y_train)
svm_yhat = svm.predict(X_test)

print('Accuracy score of the Support Vector Machines model is {}'.format(accuracy_score(y_test, svm_yhat)))

print('F1 score of the Support Vector Machines model is {}'.format(f1_score(y_test, svm_yhat)))

#XGBoost

xgb = xgb.XGBClassifier(max_depth = 4)
xgb.fit(X_train, y_train)
xgb_yhat = xgb.predict(X_test)

print('Accuracy score of the XGBoost model is {}'.format(accuracy_score(y_test, xgb_yhat)))

print('F1 score of the XGBoost model is {}'.format(f1_score(y_test, xgb_yhat)))

