### 使用python爬取b站排行榜

```python
import requests
url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)

# 打印返回的文本
print(response.text)
```

#### 解析文本结构

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 打印返回的文本
print(response.text)
print(soup.title.text)
```

#### 提取列表

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 提取列表
items = soup.findAll('li',{'class':'rank-item'}) # rank-item是其具体属性
print(len(items))
```

#### 提取标题

```python
# 输入模块
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 提取列表
items = soup.findAll('li',{'class':'rank-item'}) # rank-item是其具体属性

for itm in items:
  title = itm.find('a', {'class':'title'}).text
  print(title)
```

#### 提取其他字段

```python
# 输入模块
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 提取列表
items = soup.findAll('li',{'class':'rank-item'}) # rank-item是其具体属性

for itm in items:
  title = itm.find('a', {'class':'title'}).text
  rank = itm.find('div', {'class':'num'}).text
  score = itm.find('div', {'class':'pts'}).text
  url = itm.find('a',{'class':'title'}).get('href') # 需要用get得到属性
  print(f'{title}.{rank}.{score}.{name}')
```

#### 创建提取数据的列表

```python
# 输入模块
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 创建用来储存信息的列表
class Videos:
  def __init__(self, title, rank, score, url):
    self.title = title
    self.rank = rank
    self.score = score
    self.url = url
    
# 提取列表
items = soup.findAll('li',{'class':'rank-item'}) # rank-item是其具体属性
videos = []

for itm in items:
  title = itm.find('a', {'class':'title'}).text
  rank = itm.find('div', {'class':'num'}).text
  score = itm.find('div', {'class':'pts'}).text
  url = itm.find('a',{'class':'title'}).get('href') # 需要用get得到属性
  v = Videos(title, rank, score, url)
  videos.append(v)
  
print(len(videos))
```

#### 保存数据

```python
# 输入模块
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 创建用来储存信息的列表
class Videos:
  def __init__(self, title, rank, score, url):
    self.title = title
    self.rank = rank
    self.score = score
    self.url = url
    
  def to_csv(self):
    return[self.title, self.rank, self.score, self.url]
  
  def csv_title():
    return(['标题', '排名', '分数', 'URL'])
    
# 提取列表
items = soup.findAll('li',{'class':'rank-item'}) # rank-item是其具体属性
videos = []

for itm in items:
  title = itm.find('a', {'class':'title'}).text
  rank = itm.find('div', {'class':'num'}).text
  score = itm.find('div', {'class':'pts'}).text
  url = itm.find('a',{'class':'title'}).get('href') # 需要用get得到属性
  v = Videos(title, rank, score, url)
  videos.append(v)
  
file_name = 'Top100.csv'
with open(file_name, 'w', newline='') as f:
  pen = csv.writer(f)
  pen.writerow(Videos.csv_title())
  for v in videos:
    pen.writerow(v.to_csv())
```

### ChangeLog

20200902 python实战