import re
import json
import random
import requests
from hashlib import md5
from urllib.parse import urlencode

APPID = '20190913000334110' #你的appid
SECRETKEY = 'FqMjEsfJxLw2yea6u1kv' #你的密钥


def long2short(long_url,token="b1c8f57cf7f818f7d071788d0f2f95e6"):   
    host = 'https://dwz.cn'
    path = '/admin/v2/create'
    url = host + path
    method = 'POST'
    content_type = 'application/json'
     
    # TODO：设置待创建的长网址
    bodys = {'Url':long_url,'TermOfValidity':"1-year"}
    
    # 配置headers
    headers = {'Content-Type':content_type, 'Token':token}
    
    # 发起请求
    response = requests.post(url=url, data=json.dumps(bodys), headers=headers,verify=False)
    
    # 读取响应
    print(response.text)
    # print(resp.text)
    short_url = json.loads(response.text)['ShortUrl']
    return short_url


def translate(q,fr='zh',to='en'):
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = APPID+q+str(salt)+SECRETKEY
    sign = get_md5(sign)
    url = url+'?appid='+APPID+'&'+urlencode({'q':q})+'&from='+fr+'&to='+to+'&salt='+str(salt)+'&sign='+sign
    try:
        response = requests.get(url)
        # print(response)
        res = json.loads(response.text)
        # print(res)
        trans_result = res['trans_result'][0]['dst']
        return trans_result
    except Exception as e:
        print(e)


def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()


def slugify(value):
    value = str(value)
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

# a = slugify("How to u'se pyt'hon, Django to generate SEO-friendly URLs")
# print(a)
from itertools import permutations
alpha = 'acemnorstuvwxz'

table=''.maketrans('0123456789abcdef','acemnorstuvwxzid')

def trans_id(value,alpha_list=alpha,length=4):
    value = 16777215 - value
    s = hex(value)[2:]
    r = s.translate(table)
    print(r)

if __name__ == '__main__':
    trans_id(24)
