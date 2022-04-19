import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0, 2 * np.pi, 200)
#y = np.sin(x)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()

##plot 1:
xpoints = np.array([0,6])
ypoints = np.array([0,100])
#
plt.subplot(1,2,1)
plt.plot(xpoints,ypoints)
plt.title("plot 1")
#
##plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
#
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("plot 2")
#
plt.suptitle("RUNOOB subplot Test")
plt.show()

#x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
#sizes = np.array([20,50,100,200,500,1000,60,90])
#plt.scatter(x, y, s=sizes)
#plt.show()