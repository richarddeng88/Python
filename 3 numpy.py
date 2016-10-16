import numpy as np

# from list to np array
a = [1.2, 1.1, 2.3, 4.4, 5.3]
a = np.array(a)
b = [7, 6, 5, 4, 3]
b = np.array(b)
bmp = b/a**2
print bmp[bmp<1] # print these less than 1


# distribution mean, std, number of samples
height = np.round(np.random.normal(140,20,5000),2)
weight = np.round(np.random.normal(80,15,5000),2)
result = np.column_stack((height,weight))
print result