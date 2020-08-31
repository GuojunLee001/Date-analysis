## NumPY

### NumPy是什么

NumPy是python的扩展程序，用于高阶大量的维度数组与矩阵计算。

NumPy 和python的list有所不同：NumPy储存的数组在一个统一结构中，list的分散在不同区域，NnmPy多线程的方式，调动起来节省CPU资源。

### 基本语法及运用

#### 安装

如果安装了anoconda可以在终端输入`conda install NumPy`进行安装.

如果没有安装anaconda，可以在终端输入`pip3 install Numpy`进行安装。

#### 基本语法

```python
# -*- coding:utf-8 -*-
# 包导入数组的输出,array为数组的意思
import numpy as np
x = np.array([1, 2, 3, 4])
# 可以把多个数组作为一个元素
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
print(y)
# 获取数组的大小
print(x.shape)
print(y.shape)
# 获取元素的属性
print(y.dtype)

# 基本运算
b = np.array([1, 3, 5, 7, 9])
d= b**2
print(d)

# 数组元素的修改
y[1, 1] = 100
print(y)
```

输出结果为：

```python
[1 2 3 4]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
(4,)
(3, 3)
int64
[ 1  9 25 49 81]
[[  1   2   3]
 [  4 100   6]
 [  7   8   9]]
```

#### 数组创建及计算

```python
# 下面两种方式都是创建等差数组
x1 = np.arange(1,11,2) # 代表初始值、终值、步长
x2 = np.linspace(1,9,5) # 代表初始值、终值、元素个数

# 加减乘除等运算
# 加法运算
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(x1**2)
print(np.power(x1, x2))
print(np.remainder(x1, x2))
```



#### 统计函数

**最大最小值计算**

```python
# -*- coding:utf-8 -*-
# 最大最小值的计算
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 全部元素的最小值
print(np.amin(a))
# axis轴为0的最小值
print(np.amin(a, 0))
# 沿着axis轴为1的最小值
print(np.amin(a, 1))

# 全部元素的最大值
print(np.amax(a))
# axis轴为0的最大值
print(np.amax(a, 0))
# 沿着axis轴为1的最大值
print(np.amax(a, 1)) 

# 统计最大值最小值之差
print(np.ptp(a)) 
print(np.ptp(a, 0))
print(np.ptp(a, 1))
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
```

怎么理解此处的axis = 0 ,axis=1?axis = 0表示列表元素列之间的比较，axis=1表示列表元素行之间的比较。

**统计数组百分位数、中位数 median()、平均数 mean()**

```python
# -*- coding:utf-8 -*-
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 统计所有数组的百分数
print(np.pencentile(a, 50))
# 统计列之间的的百分数
print(np.percentile(a, 50, axis=0))
# 统计行之间的百分数
print(np.percentile(a, 50, axis=1))

# 统计数组中的中位数 median()、平均数 mean()
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
pirnt(np.mean(a, axis=1))

# 加权平均值计算
b = np.array([1, 2, 3, 4])
wts = np.array(1,2, 3, 4) #指定权重
print(np.average(b)) # 平均权重
print(np.average(b, weights=wts))

# 方差、标准差
print(np.std(b))
print(np.var(b))
```

输出结果为

```python

```

#### 结构数组

```python
# -*- coding:utf-8 -*-
import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))
```

输出结果为

```python
28.25
77.5
93.25
93.75
```

#### 排序

```python
a = np.array([[4, 3,2], [2, 4, 1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a , axis = 0))
print(np.sort(a, axis = 1))
```

输出结果为

```python
[[2 3 4]
 [1 2 4]]
[1 2 2 3 4 4]
[[2 3 1]
 [4 4 2]]
[[2 3 4]
 [1 2 4]]
```

### ChangeLog

20200830 NumPy学习1 

20200831 NumPy学习1 ，报错'numpy' has no attribute 'pencentile'待解决