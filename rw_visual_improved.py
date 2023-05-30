import matplotlib.pyplot as plt
from random_walk_improved import RandomWalk_Improved

while True:
    rw = RandomWalk_Improved(50000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # highlight startpoint and endpoint
    plt.scatter(0, 0, s=100, c='green', edgecolors='none')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red', edgecolors='none')
    
    # set axes invisible
    #plt.axes().get_xaxis().set_visible(True)
    #plt.axes().get_yaxis().set_visible(True)
    
    # set figure size
    # plt.figure(figsize=(10,6))
    
    plt.show()
    keep_running = input("Keep Running? (y/n)")
    if keep_running == 'n':
        break;