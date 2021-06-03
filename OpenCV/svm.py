from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics

cancer_data = datasets.load_breast_cancer()


x_train , x_test, y_train, y_test = train_test_split(cancer_data.data,cancer_data.target, test_size=0.4, random_state=209)


cls = svm.SVC(kernel='linear')

cls.fit(x_train,y_train)

pred = cls.predict(x_test)

#print(pred)
#print(pred)
print("accuracy: ", metrics.accuracy_score(y_test,y_pred=pred))

print("precision:" , metrics.precision_score(y_test,y_pred=pred))

print("recall: ", metrics.recall_score(y_test,y_pred=pred))

print(metrics.classification_report(y_test,y_pred=pred))