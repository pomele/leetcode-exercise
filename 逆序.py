import numpy as np

x = np.array([(0, 1, 2), (3, 4, 5)], dtype='i2, f4, i8')
print(x)
x = np.array(np.arange(6).reshape((2, 3)), dtype='i2, f4, i8')
print(x)
x = np.array([(1, 2), (3, 4)], dtype=[('foo', 'i8'), ('bar', 'f4')])
print(x)
print(x['foo'])
print(x['bar'])
y = x['foo']
y[...] = 0
print(x)
print(y.strides)