#create a linear regression model
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt




x=np.array([0,1,2,3,4,5,6,7,8,9])
len_x=len(x)
y=np.array([1,3,2,5,7,8,8,9,10,12])
z=(x,y)
mean_x=np.mean(x)
mean_y=np.mean(y)
print("mean_x",mean_x)
print("mean_y",mean_y)

                  #b1=sum(sum1)*(sum2) / sum(sum1*sum1)
                  #b0=  mean_y - b1(mean_x)
                
sum1=x-mean_x


print(sum1)

sum2=y-mean_y

print(sum2)

sum3=sum1*sum2
print(sum3)

n=np.sum (sum3)
print("n",n)

sum4=sum1*sum1
print(sum4)

d=np.sum (sum4)
print ("d",d)
b1=n/d
print( "b1",b1)



print(type(b1))
b0=mean_y - b1*(mean_x)
print("b0",b0)


plt.plot(x,y)
plt.show()


#regr=linear_model.LinearRegression()
#regr.fit(mean_x,mean_y)



