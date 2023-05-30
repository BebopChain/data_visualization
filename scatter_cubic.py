import matplotlib.pyplot as plt

x_values = list(range(0,5000))
y_values = [x**3 for x in x_values]


plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)

plt.title("Cubic Scatter", fontsize=20)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Cubic of Value", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.axis([0, 5100, 0, 5100**3])
plt.savefig('cubic_plt.png', bbox_inches='tight')


plt.show()
