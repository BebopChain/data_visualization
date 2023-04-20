import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
#print(type(squares))
plt.plot( range(1,6,1), squares, linewidth=4)
##set title, x/y label
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()