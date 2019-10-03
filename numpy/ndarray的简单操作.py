import numpy as np

# 单一维度
a = np.array([1,2,3])
print(a)

# 多个维度
b = np.array([[1,2,3],[2,3,4]])
print(b)

# dtype参数
c = np.array([1,2,3],dtype= complex)
print(c)

# arange函数
d = np.arange(6)
print("d:",d,d.ndim)
d.shape = (3,2)
print("d:",d)

# 返回存储的内存信息
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
