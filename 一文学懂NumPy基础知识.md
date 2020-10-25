## NumPy可以用来干什么？

在python里面已经有了列表list，为什么还要使用NumPy？

这和list与NumPy在数据储存和运算速度有关。提升内存和计算资源的利用效率。

NumPy最重要的知识包括：

- ndarray（N-dimensional array object），解决多维数组问题，
- ufunc（universal function object），解决对数组进行处理的函数。

## ndarray

array表示数据，ndarray代表多维数组。

### 创建数组

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 1, 2], [2, 3, 5], [3, 4, 5]])
b[1, 1]=10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)
```

输出结果为

```python
(3,)
(3, 3)
int64
[[ 1  1  2]
 [ 2 10  5]
 [ 3  4  5]]
```

总结：

- shape用于获取数组的大小；
- dtype用于获取数组的属性；
- b[1, 1]表示对数组进行修改，从零开始计数，上面代码把b中的每个数组看成一个整体，当成一个数。

### 结构数组

创建储存每个数字单元的表格。

```python
import numpy as np
# 定义数组结构
persontype = np.dtype({
  'names':['name', 'age', 'chinese', 'math', 'English'],
  'formats':['S32', 'i', 'i', 'i', 'f']})

peoples = np.array([('A', 1, 2, 3, 4), 
                    ('B', 4, 6, 7, 8),
                    ('C', 0, 8, 8, 5),
                    ('D', 3, 7, 8, 1)],
                   dtype = persontype)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
Englishs = peoples[:]['English']

# 计算平均值
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(Englishs))
```

输出结果为：

```python
2.0
5.75
6.5
4.5
```

## ufunc

universal function的缩写。

### 创建连续数组

```python
import numpy as np
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9 ,5)

print(x1)
print(x2)
```

输出结果为：

```python
[1 3 5 7 9]
[1. 3. 5. 7. 9.]
```

arange是range的内置函数，arange(1, 11, 2)分别代表初始值、终值、步长

linspaces是linear space的缩写，代表线性等分向量。linespace(1, 9,5)分别代表初始值，重值（含），元素个数。

## 运算

### 基本运算

可以进行加、剪、乘、除、n次方，取余数等运算

```python
import numpy as np
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9 ,5)

print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
```

输出结果为：

```python
[ 2.  6. 10. 14. 18.]
[0. 0. 0. 0. 0.]
[ 1.  9. 25. 49. 81.]
[1. 1. 1. 1. 1.]
[1.00000000e+00 2.70000000e+01 3.12500000e+03 8.23543000e+05
 3.87420489e+08]
[0. 0. 0. 0. 0.]
```

在进行计算时，需要保证数组的秩相同，即每个列表的元素个数相同，方可进行运算。

### 统计学相关的运算

```python
# -*- coding:utf-8 -*-

import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print(np.amin(a)) # 最小值
print(np.amin(a, 0)) # 每一列中的的最小值
print(np.amin(a, 1)) # 每一行中的最小值
print(np.amax(a)) # 最大值
print(np.amax(a, 0)) # 每一列中的最大值
print(np.amax(a, 1)) # 每一行的最小值

# 统计最大值与最小值之差
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# 求中位数与平均数
print(np.median(a)) # 整体列表中位数
print(np.median(a, axis=0)) # 求每一列的中位数
print(np.median(a, axis=1)) # 求每一行的中位数
print(np.mean(a)) # 求整体列表的平均数
print(np.mean(a, axis=0)) # 求每一列的平均数
print(np.mean(a, axis=1)) # 求每一行的平均数

# 求加权平均数
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a)) # 默认权重相同
print(np.average(a, weights=wgt)) # 赋予不同权重 （1*1=2*2+3*3+4*4）/（1+2+3+4）

# 求标准差方差
print(np.std(a)) # 标注差
print(np.var(a)) # 方差
```

输出结果为：

```python
1
[1 2 3]
[1 4 7]
9
[7 8 9]
[3 6 9]

8
[6 6 6]
[2 2 2]

5.0
[4. 5. 6.]
[2. 5. 8.]
5.0
[4. 5. 6.]
[2. 5. 8.]

2.5
3.0

1.118033988749895
1.25
```

从行列式角度理解，axis=0表示列，axis=1表示行。

## NumPy进行排序

排序在数据分析中使用频率很高，一般排序语句结构为：

```python
sort(a, axis=-1, kind=‘quicksort’, order=None)
```

默认情况下axis=-1，表示对内部列表分别排序。当axis=None时，表示把所有数字按照一个列表排序。

Kind包含三种结构：quicksort、mergesort、heapsort ，分别代表快速排序、合并排序、堆排序。默认情况下，使用的是quicksort排序。

```python
import numpy as np

a = np.array([[14, 55, 9], [45, 56, 87], [90, 3, 45]])

print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
```

输出结果为：

```python
[[ 9 14 55]
 [45 56 87]
 [ 3 45 90]]
[ 3  9 14 45 45 55 56 87 90]
[[14  3  9]
 [45 55 45]
 [90 56 87]]
[[ 9 14 55]
 [45 56 87]
 [ 3 45 90]]
```

### 参考资料

《数据分析实战45讲》-极课时间  陈旸

### ChangeLog

20201025 完成基本内容

