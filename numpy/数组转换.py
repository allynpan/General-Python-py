import numpy as np

# empty的用法
x1 = np.empty([3,2],dtype=int)
print(x1)

# zero的用法
x2 = np.zeros(5)
print(x2)
y1 = np.zeros((5,),dtype=int)
print(y1)

# one的用法，填充
x3 = np.ones((6,),dtype=int)
print("x3:",x3)