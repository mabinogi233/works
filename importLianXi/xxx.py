import numpy as np
a=np.matrix([[9/2,-21/4],[-21/4,25/4]])
b=a.I
c=np.matrix([3,-17/4])
d=b*(c.T)
print(d)
