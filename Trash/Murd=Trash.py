from matplotlib import pyplot as plt
import numpy as np

x =  np.arange(0,2.1,.1)
y_1 = np.asarray([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1,1,1,1,1,1,1,1,1,1])
y_2 = np.asarray([0,0.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
plt.plot(x,y_2,"r--",x,y_1,"go")
plt.title("Impossibility Index vs. Time per Task")
plt.xlabel("Impossibility Index(%)")
plt.ylabel("Time per Task(person-hour/task)")
plt.ylim(0,2.5)
plt.xlim(0,2.5)
plt.show()

#find minimum point
# x = np.arange(0,10,.5)
# try:
#     X = 1/(1+x)
# except ZeroDivisionError:
#     print("Dumb Bitch")
# y_1 = 40
# y_2 = 38
# y_3 = 36
# print(y_1*X)
# print(y_2*X)
# print(y_3*X)
# # plt.plot(X,y_1*X,'ro')
# # plt.xlabel("hello")
# # print(y_1*X)
# # plt.show()