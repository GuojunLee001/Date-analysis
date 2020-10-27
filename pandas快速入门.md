## 1.初识Pandas

**Pandas** 是“Python的核心数据分析支持库，提供了快速、灵活、明确的数据结构，旨在简单、直观地处理关系型、标记型数据”，主要数据结构是 Series（一维数据）与 DataFrame（二维数据），这两种数据结构可以处理金融、统计、社会科学、工程等领域里的大多数典型用例。

## 2.数据结构

### 2.1 Series数据结构

```python
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

d = pd.Series([1, 3, 5, 7], index=['a', '1', 'c', 3])
print(d)
```

输出结果为：

```python
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
  
a    1
1    3
c    5
3    7
dtype: int64
```

数据结构为Series([1, 3, 5, 6], index=['a', 'b', 'c', 'd'])。index默认结构为0、1、2、3……

从上面的运行结果可以看出，index后面的文本型结构'a'，必须加引号，否则会报错，而数字是否加引号虽不影响，单加不加引号，数据类型完全不同。

除了采用index外，还可以采用字典形式，如下：

```python
import pandas as pd
from pandas import Series,DataFrame

d = {'a':1, 'b':2, 'c':3, 'd':4}

x1 = Series(d)

print(x1)
```

输出结果为：

```python
a    1
b    2
c    3
d    4
dtype: int64
```

### 2.2 DataFrame 数据结构

DataFrame可以理解为两个Series构成的数组结构，在语法上完全相同。

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'列1':[1, 2, 3, 4], '列2':[5, 6, 7, 8], '列3':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['列1', '列2', '列3'])

print(df2)
```

输出结果为：

```python
       列1  列2  列3
one     1   5   0
two     2   6   9
three   3   7   6
four    4   8   8
```

### 2.3 导入和导出

Pandas 可以从xlsx, csv中导入数据，也可以输出数据为xlsx, csv。

```python
# 写入csv
df.to_csv('foo.csv')

# 读取csv
pd.read_csv('foo.csv')
```

## 3.数据清洗

### 3.1 删除

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'列1':[1, 2, 3, 4], '列2':[5, 6, 7, 8], '列3':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['列1', '列2', '列3'])

# 数据删除使用drop()
df2 = df2.drop(columns=['列1'])
df2 = df2.drop(index=['one'])

print(df2)
```

### 3.2 去除重复的值

```python
df = df.drop_duplicates() #去除重复行
```

### 3.3 重命名

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'列1':[1, 2, 3, 4], '列2':[5, 6, 7, 8], '列3':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['列1', '列2', '列3'])

# 重命名使用rename(columns=new_names, inplace=True) 函数
df2.rename(index={'one':'第1', 'two':'第2'}, inplace=True)

print(df2)
```

### 3.4 格式相关

**使用astype转换格式**

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'列1':[1, 2, 3, 4], '列2':[5, 6, 7, 8], '列3':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['列1', '列2', '列3'])

df2['列1'].astype('str')
df2['列1'].astype(np.int64)
```

**去除数据之间的空格strip**

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'列1':[1, 2, 3, 4], '列2':[5, 6, 7, 8], '列3':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['列1', '列2', '列3'])

# 删除左右两边的空格
df2['one'] = df2['one'].map(str.strip)

# 删除左边的空格
df2['one'] = df2['one'].map(str.lstrip)

# 删除右边的空格
df2['one'] = df2['one'].map.(str.rstrip)

# 删除特殊的字符
df2['one']=df2['one'].str.strip('$')
```

**大小写转换**

```python
import pandas as pd
from pandas import Series,DataFrame

data = {'chinese':[1, 2, 3, 4], 'math':[5, 6, 7, 8], 'English':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['chinese', 'math', 'English'])

# 全部大写
df2.columns = df2.columns.str.upper()

# 全部小写
df2.columns = df2.columns.str.lower()

# 首字母大写
df2.columns = df2.columns.str.title()

print(df2)
```

```python
# 下面这两行代码也可以一行代码
data = {'chinese':[1, 2, 3, 4], 'math':[5, 6, 7, 8], 'English':[0, 9, 6, 8]}
df2 = DataFrame(data, index=['one', 'two', 'three', 'four'], columns=['chinese', 'math', 'English'])


df2 = pd.DataFrame({'chinese':[1, 2, 3, 4], 
                     'math':[5, 6, 7, 8],
                    'English':[0, 9, 6, 8]},index=['one', 'two', 'three', 'four'] )
```

**查找空值**

查找空值使用

```python
df.isnull()
```

### 3.5 apply 函数对数据进行清洗

@todo

## 4.数据分析

Pandas常用的统计函数用法和NumPy类似（资料来源极课时间｜数据分析实战45讲），如下：

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gk43eo27nnj30u01hcts7.jpg" alt="img" style="zoom: 50%;" />

使用describe()函数可以输出所有的统计指标

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})

print(df1.describe())
```

输出结果如下：

```python
   data1
count  5.000000
mean   2.000000
std    1.581139
min    0.000000
25%    1.000000
50%    2.000000
75%    3.000000
max    4.000000
```

## 5.数据表合并

比如下面两个数据表需要合并，使用的是merge()函数。

```python
df1 = DataFrame({'name':['One', 'two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['one', 'Two', 'A', 'B', 'C'], 'data2':range(5)})
```

### 5.1 基于指定列进行连接

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['One', 'Two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['One', 'Two', 'A', 'B', 'C'], 'data2':range(5)})

df3 = pd.merge(df1, df2, on='name')

print(df3)
```

输出结果

```python
name  data1  data2
0  One      0      0
1  Two      1      1
```

### 5.2 inner内链接

相当于求两个DataFrame的交集。

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['One', 'Two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['One', 'Two', 'A', 'B', 'C'], 'data2':range(5)})

df3 = pd.merge(df1, df2, how='inner')

print(df3)
```

输出结果为

```python
  name  data1  data2
0  One      0      0
1  Two      1      1
```

### 5.3 outer外链接

相当于求两个 DataFrame 的并集

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['One', 'Two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['One', 'Two', 'A', 'B', 'C'], 'data2':range(5)})

df3 = pd.merge(df1, df2, how='outer')

print(df3)
```

输出结果为：

```python
 name  data1  data2
0  One    0.0    0.0
1  Two    1.0    1.0
2    a    2.0    NaN
3    b    3.0    NaN
4    c    4.0    NaN
5    A    NaN    2.0
6    B    NaN    3.0
7    C    NaN    4.0
```

### 5.4 left左链接

第一个 DataFrame 为主进行的连接，第二个 DataFrame 作为补充

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['One', 'Two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['One', 'Two', 'A', 'B', 'C'], 'data2':range(5)})

df3 = pd.merge(df1, df2, how='left')

print(df3)
```

输出结果为：

```python
name  data1  data2
0  One      0    0.0
1  Two      1    1.0
2    a      2    NaN
3    b      3    NaN
4    c      4    NaN
```

### 5.5 right右链接

第二个 DataFrame 为主进行的连接，第一个 DataFrame 作为补充

```python
import pandas as pd
from pandas import Series,DataFrame

df1 = DataFrame({'name':['One', 'Two', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['One', 'Two', 'A', 'B', 'C'], 'data2':range(5)})

df3 = pd.merge(df1, df2, how='right')

print(df3)
```

输出结果为：

```python
 name  data1  data2
0  One    0.0      0
1  Two    1.0      1
2    A    NaN      2
3    B    NaN      3
4    C    NaN      4
```

### 参考资料

[Pandas中文网](https://www.pypandas.cn/docs/)

极课时间｜数据分析实战45讲-陈旸

### ChangeLog

20201026 完成1-3.4

20201027 完成3.5-5