import matplotlib.pyplot as plt

## Manual calculation
#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]

## auto calculation by python
x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]

#you can set point color by argument c
# can set edgecolor of each point(which is black by default) by argument edgecolor
# can set colormap by setting c to a value list and cm to a kind of color
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=40)

# set title and x,ylabel
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set the size of the tick marks
plt.tick_params(axis='both', which="major", labelsize=14)

#set value range for each axis
plt.axis([0, 1100, 0, 1100000])
plt.savefig('square_plt.png', bbox_inches='tight')
plt.show()