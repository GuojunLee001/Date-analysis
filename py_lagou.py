# -*- coding:utf-8 -*-

import requests
import pandas as pd
import time
import csv
import json

# 请求页面
for i in range(30):
    url_login='https://www.lagou.com'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?labelWords=&fromSearch=true&suginput=',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
    s = requests.Session()
    s.get(url_login, headers=header, timeout=3) # 请求首页获取cookies
    cookie = s.cookies

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    posts = {'first':'true',
            'pn': int(i+1),
            'kd': '数据分析师',
            'request_id': '689340c0-47d2-4a6f-b0da-1a0b63eb6cc2'
            }

    html = s.post(url=url, headers=header, data=posts, cookies=cookie, timeout=5)
    jb = json.loads(html.text)
    print(jb)

    try:
        for jbj in range(len(jb['content']['positionResult']['result'])):
            data1 = [(jb['content']['positionResult']['result'][jbj]['positionNames'],
                    jb['content']['positionResult']['result'][jbj]['businessZones'],
                    jb['content']['positionResult']['result'][jbj]['companyFullName'],
                    jb['content']['positionResult']['result'][jbj]['companyLabelList'],
                    jb['content']['positionResult']['result'][jbj]['companyShortName'],
                    jb['content']['positionResult']['result'][jbj]['salary'])]
            data2 = pd.DataFrame(data1)
            data2.to_csv('数据分析', header=False, index=False, mode='a+')
        print("page" + str(i+1)+"has done")
    except:
        print("访问异常")
    
    time.sleep(3)