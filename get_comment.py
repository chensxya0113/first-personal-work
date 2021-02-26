#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import lxml.html
import re


# In[2]:


url="https://mfm.video.qq.com/danmu?&target_id=5967468201%26vid%3Du0034zxdhdi&timestamp=15"
header={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}


# In[3]:


def get_after_id():
    url="https://v.qq.com/x/cover/mzc00200jg5gfcq/u0034zxdhdi.html"
    header={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    res3=requests.get(url,headers=header,verify=False)
    html=lxml.html.fromstring(res3.text)
    param=html.xpath('//span[@class="item"]/@id')
    num1=url.rsplit("/")[-1].split(".")[0]
    param.append(num1)
#     print(param)
    return param


# In[4]:


def get_all_id(params):
    res=[]
    header={
        "referer":"https://v.qq.com/x/cover/mzc00200jg5gfcq/v0034njmyyt.html",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    reurl="https://access.video.qq.com/danmu_manage/regist?vappid=97767206&vsecret=c0bdcbae120669fff425d0ef853674614aa659c605a613a4&raw=1"
    for i in params:
        data={
            "wRegistType":2,
                "vecIdList":[i],
                "wSpeSource":0,
                "bIsGetUserCfg":1,
                "mapExtData":{
                    i:{
                        "strCid": "mzc00200jg5gfcq",
                        "strLid":""
                    }
                }
        }
        response=requests.post(url=reurl,headers=header,json=data,verify=False)
        result=response.json()["data"]["stMap"][i]["strDanMuKey"]
        res.append(result.split("=",4)[-1])
    return res


# In[10]:


import requests
import lxml.html
import re
import time
def get_comment(res):
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:!eNULL:!MD5'

    header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    for i in res:
        for j in range(15,2500,30):
            url='https://mfm.video.qq.com/danmu?&target_id=%s&timestamp=%s'%(i,j)
            url_1=url.replace('&vid=','%26vid%Dv')
            print(url_1)
            res=requests.get(url_1,headers=header,verify=False)
            res2=res.json()
            time.sleep(3)
            for i in res2['comments']:
                danmu=i["content"]
            with open('danmu.txt','w+',encoding='utf-8')as f:
                f.write(danmu+'\n')
            time.sleep(1)


# In[11]:


def main():
    param=get_after_id()
    res=get_all_id(param)
    get_danmu(res)


# In[ ]:




