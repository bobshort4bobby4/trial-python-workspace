#from matplotlib import pyplot as plo
#import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.use('Agg')
print("trial for matplotlib")
x  = [1, 2, 3, 4, 5]
y =   [2, 4, 6, 8, 10]
print(x)
print(mpl.__version__)

plt.plot(x, y)
plt.show()


# import plotext as plt

# plt.plot(x,y)
# plt.title("Line Plot")
# plt.show()