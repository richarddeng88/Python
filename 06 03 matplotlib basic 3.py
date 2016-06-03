import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

fig = plt.figure()

def create():
    xs=[]
    ys=[]
    for i in range(10):
        x = i
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs, ys

# add subplot syntax
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(212)

ax1= plt.subplot2grid((6,1),(0,0), rowspan=1, colspan=1)
ax2= plt.subplot2grid((6,1),(2,0), rowspan=1, colspan=1)
ax3= plt.subplot2grid((6,1),(4,0), rowspan=1, colspan=1)

x,y = create()
ax1.plot(x,y)
x,y = create()
ax2.plot(x,y)
x,y = create()
ax3.plot(x,y)

plt.title("have a good day")
plt.xlabel("x lay")
plt.ylabel("y lay")
plt.show()

