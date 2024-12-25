import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b,c):
    return a*x**2+b*x+c
xlist = np.linspace(-10, 10, num=1000)
ylist = np.arange(-10, 10.1, 0.1)
a = 4
b = 3
c = 7
ylist = f(xlist, a, b, c)
plt.figure(num=0, dpi=120)
plt.plot(xlist, ylist, label = "f(x)")
plt.plot(xlist, ylist**0.5, '--g', label = "f(x)**0.5")
plt.title("Plotting Example : ")
plt.xlabel("Time / s")
plt.ylabel("Distance / m")
x = [1,2,3,4,5,6,7]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
plt.plot(x, y)
plt.savefig('td.png', dpi=120)



x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.savefig('sine.png', dpi=120)



squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)
plt.savefig('square.png', dpi=120)