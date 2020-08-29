## python基础语法

### 输入输出

```python
name = input("What's is your name?")
a = 1 + 1
print('hello, %s' %name)
print('a = %d' %a)
```

输出结果为：

```

What's your name?y
hello,y
a = 2
```

### 判断语句

```python
score = int(input("What's your score?"))
if score>= 90:
       print('Excellent')
else:
       if score < 60:
           print('Fail')
       else:
           print('Good Job')
```

### 循环语句：for … in

```python
sum = 0
for number in range(11):
    sum = sum + number
print(sum)
```

输出结果为；

```python
55
```

### 循环语句: while

```python
sum = 1
number = 2
while number <=100:
  sum = sum + number
  number = number + 1
print(sum)
print(number)
```

输出结果为：

```
5050
101
```

### 数据类型：列表、元组、字典、集合

#### 列表[]

```python
lists = ['a','b','c']
lists.append('d')
print(lists)
print(len(lists))
lists.insert(0,'mm')
lists.pop()
print(lists)
```

输出结果为：

```
['a', 'b', 'c', 'd']
4
['nm', a', 'b', 'c']
```

增：append() 在尾部添加元素、使用 insert() 在列表中插入元素

删：使用 pop() 删除尾部的元素

查：len() 函数获得 lists 中元素的个数

#### 元组 (tuple)

```python
tuples = ('tupleA','tupleB')
print(tuples[0])
print(tuples[1])
print(tuples[-1])
```

输出结果为：

```python
tupleA
tupleB
tupleB
```

元组和列表相同，但是初始化后不能够增加和删除元素。

#### 字典 {dictionary}

```python
# -*- coding: utf-8 -*
#定义一个dictionary
score = {'guanyu':95,'zhangfei':96}
#添加一个元素
score['zhaoyun'] = 98
print(score)
#删除一个元素
score.pop('zhangfei')
#查看key是否存在
print('guanyu' in score)
#查看一个key对应的值
print(score.get('guanyu'))
print(score.get('yase',99))
```

输出结果为：

```python
{'guanyu': 95, 'zhangfei': 96, 'zhaoyun': 98}
True
95
99
```

增：score['zhaoyun'] = 98

删：score.pop()

查：是否存在用print('guanyu' in score)、对应值用print(score.get('guanyu'))

### 集合：set

```python
s = set(['a', 'b', 'c'])
# 增加某个元素
s.add('d')
# 移除某个元素
s.remove('b')
print(s)
# 查找某个元素
print('c' in s)
```

输出结果为：

```
{'d', 'a', 'c'}
True
```

增： add

删：remove

查：使用 in

### 函数：def

```python
def addone(score):
   return score + 1
print(addone(99))
```

输出结果为：

```python
100
```

### 注释

使用`# -- coding: utf-8 -`，单行注释使用`#`，多行注释可以使用三个单引号

### 引用模块 / 包：import

引用直接使用`import module_name`调动即可，import本质上是路径的搜索。

针对package，可以采用`from … import …`，这实际是从一个目录中引用模块

### 参考资料

《数据分析实战45讲》陈旸