import numpy as np

# numpy.arange 创建数值同时返回ndarray对象
x1 = np.arange(5)
print(x1)

# numpy.linespace 创建一个一维数组，数组是一个等差数列构成的
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) 其中num表示对应的等步长的数目
a = np.linspace(1,10,5)
print(a)

# nunpy.logspace 创建一个于等比数列 !!!!
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
b = np.logspace(1,2,num=10)
print(b)



