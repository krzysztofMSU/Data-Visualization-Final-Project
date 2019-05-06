# Example of animation of pyplot patches
# This example grows and shrinks a Rectangle
# Written by Aaron Gordon, Feb. 2019
#
# See https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
# for (a possibly dated??) discussion and other examples

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.animation as animation

# Reading data from file (in this same directory with exercise_3.py)
filename = 'food_imports.csv'                           # Defines the full name of the file
data = pd.read_csv(filename, index_col=0).T             # 'T' to transpose data (columns to rows)
years = data.index.to_list()                            # 'years' are Years
valuex = data.to_numpy().T.tolist()                     # 'values' for each list in 1 row of each year
foods = data.columns.to_numpy().tolist()                # 'foods' names


FRAME_DELTA = 100       # milliseconds
fig, ax = plt.subplots()
rwidth = .2              # rectangle's width
rheight = 5             # rectangle's height

# values = [7, 12, 14, 18, 24, 25, 21, 19, 13, 6, 5, 6, 4, 5]
# values = pd.DataFrame(np.random.rand(10, 50))
# rect = Rectangle((3, 0), rwidth, rheight)
# print(values, rect)
values = pd.DataFrame(np.random.rand(10, 50))
rect1 = Rectangle((1, 0), rwidth, rheight)
rect2 = Rectangle((2, 0), rwidth, rheight)
rect3 = Rectangle((3, 0), rwidth, rheight)
rect4 = Rectangle((4, 0), rwidth, rheight)
rect5 = Rectangle((5, 0), rwidth, rheight)
rect6 = Rectangle((6, 0), rwidth, rheight)
rect7 = Rectangle((7, 0), rwidth, rheight)
rect8 = Rectangle((8, 0), rwidth, rheight)
rect9 = Rectangle((9, 0), rwidth, rheight)
rect10 = Rectangle((10, 0), rwidth, rheight)

print(values)

for index in range(len(values)):
    print('index in for loop', index)
#     rect = Rectangle((0, 0), rwidth, rheight)


def init():                     # init function for the animation
    top_y = max(values)
    ax.set_xlim(0.0, 11.0)
    ax.set_ylim(0.0, 50.0)
    rect1.set_height(0)
    rect1.set_color('lawngreen')
    rect2.set_color('r')
    rect3.set_color('orchid')
    rect4.set_color('teal')
    rect5.set_color('salmon')
    rect6.set_color('grey')
    rect7.set_color('y')
    rect8.set_color('royalblue')
    rect9.set_color('gold')
    rect10.set_color('lightcoral')
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    ax.add_patch(rect4)
    ax.add_patch(rect5)
    ax.add_patch(rect6)
    ax.add_patch(rect7)
    ax.add_patch(rect8)
    ax.add_patch(rect9)
    ax.add_patch(rect10)
    return rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10


def animate(num):           # called each frame with rectangle height
    rect1.set_height(num)    # rect has to be global so not garbage collected
    rect2.set_height(num)
    rect3.set_height(num)
    rect4.set_height(num)
    rect5.set_height(num)
    rect6.set_height(num)
    rect7.set_height(num)
    rect8.set_height(num)
    rect9.set_height(num)
    rect10.set_height(num)
    return rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10 # return a sequence of patches to draw


ani = animation.FuncAnimation(fig, animate, frames=FRAME_DELTA, init_func=init,
                              interval=FRAME_DELTA, repeat=True, blit=True)
plt.show()
