import numpy as np
import matplotlib.pyplot as plt

def interpolasi_linear(x0,y0,x1,y1,x):
    return y0 +(y1-y0)/(x1-x0)*(x-x0)

x0 = -1
y0 = 4
x1 = 3
y1 = 6
x = 2

y = interpolasi_linear(x0,y0,x1,y1,x)
print(y)

x_ = np.array([x0,x,x1])
y_ = np.array([y0,y,y1])

plt.scatter(x_,y_,color="black")
plt.plot(x_,y_,color="black")

for i_x, i_y in zip(x_, y_):
    plt.text(i_x + 0.2, i_y, '({}, {})'.format(i_x, i_y))

plt.show()
