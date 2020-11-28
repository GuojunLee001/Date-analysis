---
title: 如何使用Python操作Excel
date: 2020-11-27 07:36:26
categories: 
tags: [数据分析, python]
toc: true # 是否启用内容索引
---

在进行操作前，我们先熟悉一下excel表格的基本术语：

- 工作簿：workbook。包含多个工作表的。
- 表单：worksheet。指一个工作簿里面的每个表单。
- 行：row
- 列：column
- 单元格：cell

这里我们使用openpyxl读取数据。

### 查看工作簿/工作表的内容

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')

# 从工作簿查看工作表
print(wb.sheetnames)
```

也可以通过循环的形式打开工作表

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')

# 从工作簿查看工作表
for sheet in wb:
  print(sheet.title)
```

假如要想增加工作表，可以通过下面的程序实现

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')

# 增加表单
Mysheet = wb.create_sheet("保育猪成本")
Mysheet2 = wb.create_sheet("育肥猪成本")

print(wb.sheetnames)
```

读取某个单元格内容

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')

ws = wb.active

# 读取表单对象
print(ws['A1'])

# 读取单元格的内容
print(ws['A1'].value)
```

上面的程序未表示出行列坐标，如果想表示“第X行X列是X”，使用下面方法

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')

ws = wb.active

c = ws['A1']

# 读取单元格的第一种方法
print('row {} column {} is {}'.format(c.row, c.column, c.value))

# 读取单元格的第一种方法
print(ws.cell(row=1, column=3).value)

# 读取一行多个单元格
for i in range(1,8):
  print(ws.cell(row=i, column=3).value)
```

遍历某行或者某列的内容

通过下面的程序可以读取工作表中第五列的所有内容

```python
mport openpyxl

wb = openpyxl.load_workbook('examble.xlsx')
ws = wb.get_sheet_by_name("原始数据")

for i in range(5, ws.max_row+1):
    name = ws.cell(row=i, column=5).value

    print(name)
```

总结：

```python
[1] import openyxl
[2] wb = openpyxl.load_wookbook("文件名")
[3] ws = wb.active or  ws = wb.get_sheet_by_name(sheettitle)
[4] ws = ['A1'] or ws.cell(row=3, column=2)
```

### 新工作表的创建及保存

工作表和工作簿的创建比较简单。

```python
import openpyxl

# 创建工作簿
ws = openpyxl.Workbook()
sheet = ws.active

# 给工作表命名
sheet.title = "first"

# 保存工作表
ws.save("examble2.xlsx")
```

当然也可以在原有文件的基础上创建工作表，注意最后保存文件时，使用另外一个名字，防止覆盖原文件的内容。

如果想要创建新的工作表，则使用`create_sheet(index=0, title='名称')`，index代表表单的位置，title表示表单的名称，如果不填写表单的名称，会默认为sheet。

```python
import openpyxl

# 创建工作簿
ws = openpyxl.Wookbook()

sheet = ws.active

ws.create_sheet(index=3, title='second')

# 保存工作表
ws.save("examble2.xlsx")
```

表单的删除使用如下程序

```python
ws.remove_sheet(wb.get_sheet_by_name('second'))
```

### 向单元格写内容

最简单的是手工往里面填，这个用得少

```python
sheet['A1'] = "填写单元格的内容"
```

向单元格批量填写如下：

```python
import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

# 创建工作表
ws = wb.create_sheet("First")

for row in range(1,1000):
    ws.append(range(1, 100, 2))

wb.save("excamble5.xlsx")
```

### 单元格内容的批量改写

基本方法是使用for循环对单元格进行遍历，当查找到需要改写的内容时，直接改写

遍历的程序如下：

```python
import openpyxl

wb = openpyxl.load_workbook('examble.xlsx')
ws = wb.get_sheet_by_name("原始数据")

# 遍历第4列
for i in range(5, ws.max_row+1):
    name = ws.cell(row=i, column=5).value

    print(name)
```

### 参考资料

[用Python处理Excel数据，中文全基础系列教程](https://www.bilibili.com/video/BV1m4411K7Tc?p=3)

[用Python处理Excel数据，中文全基础系列教程](https://www.bilibili.com/video/BV1m4411K7Tc?p=3)

[openpyxl官方文档](https://openpyxl.readthedocs.io/en/stable/)

