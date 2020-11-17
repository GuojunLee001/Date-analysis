# -*- coding:utf-8 -*-

# 代码参考链接：https://blog.csdn.net/Q_M_X_D_D_/article/details/104662721

import urllib.request
import json
import time
import xlwt
 
# 爬取评论信息
 
page = int(input('请输入爬取的结束页码:'))
for i in range(0,page):
    print('第%s页开始爬取'%(i+1))
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=5461917&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    url = url.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Referer': 'https://item.jd.com/'
    }
 
    request = urllib.request.Request(url=url,headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    content = content.strip('fetchJSON_comment98vv385();')
    obj = json.loads(content)
    comments = obj['comments']
    fp = open('京东.text','a',encoding='utf8')
    for comment in comments:
        #评论时间
        # creationTime = comment['creationTime']
        #评论人
        # nickname = comment['nickname']
        #评论内容
        contents = comment['content']
        item = {
            # '评论时间': creationTime,
            # '用户': nickname,
            '评论内容': contents,
        }
        string = str(item)
        fp.write(string + '\n')
    print('第%s页完成' %(i+1))
    time.sleep(2)
    fp.close()