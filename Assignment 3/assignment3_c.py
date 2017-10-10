import sklearn
from sklearn import svm
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

#Loading the dataset
breastcancer_data=datasets.load_breast_cancer()

#getting the data and response of the dataset
x=breastcancer_data.data
y=breastcancer_data.target


clf=svm.SVC(kernel='rbf',C=1.0)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model= clf.fit(x_train,y_train)

print(model.score(x_test,y_test))
