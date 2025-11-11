import numpy as np
import matplotlib.pyplot as plt
import os
def plot_vectors(vectors,color,label):
    #creates an 6*6 inch square plot
    plt.figure(figsize=(10, 10))
    #gets the current axis (used later for text and scaling).
    ax=plt.gca()

    for i,v in enumerate(vectors):
        #plt.quiver = Draw arrows (vectors)
        plt.quiver(0,0,v[0],v[1],angles='xy',scale_units='xy',scale=1,color=color[i])
        #Adds text slightly offset from the arrow tip, so the label (like “v1”) doesn’t overlap the arrow.
        ax.text(v[0]+0.2, v[1]+0.2,label[i],fontsize=12,color=color[i])
    
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.grid(True)
    #Adds horizontal and vertical black lines at x=0 and y=0, representing the coordinate axes.
    plt.axhline(0,color='black',linewidth=1)
    #Ensures that 1 unit on the X-axis equals 1 unit on the Y-axis (so arrows don’t look stretched).
    plt.gca().set_aspect('equal')
    if not os.path.exists('data'):
        os.makedirs('data')
    plt.savefig('data/vector-chart.png')
    plt.show()
    





v1= np.array([3,2])
v2 =np.array([1,5])

plot_vectors([v1,v2],["red","blue"],['v1','v2'])


