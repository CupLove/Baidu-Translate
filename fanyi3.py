# -*- coding: utf-8 -*-
import time

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5

# 文件的名称
inputfile_name = ".\input.txt"
outputfile_name = ".\output.txt"

# 将需要翻译的语言复制到input.txt  输出结果在output.txt
# 打开文件，读取当中的内容
with open(inputfile_name, "r",encoding='utf8') as file:
    texts = file.read()
with open(outputfile_name, "w",encoding='utf8') as file:
    file.write("")


# Set your own appid/appkey.
# 填写自己的百度appid appkey
appid = ''
appkey = ''
# query = input("请输入翻译内容:")
print("原文：\n%s"%texts)
query = texts
## 拼接url
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path




## 输入内容
# query = print("请输入翻译内容:\n")

statu = 0
text_z = ""
text_e = ""

# 随机翻译包含的语言,可以查官网自己添加
lang0 = ["zh","en","th","kor","el","ru","jp","spa","it","pt","dan","ara","swe","vie","hu","nl","de","slo","fin"]
lang1 = 'zh'
lang2 = 'en'
from_lang = lang1
# range为翻译次数
for i in range(10):
    print("从"+from_lang+"===")
    print("hhh")
    to_lang = random.choice(lang0)

    print("到"+to_lang)

    # Generate salt and sign
    ## 生成签名
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + str(query) + str(salt) + appkey)

    # Build request
    # 建立请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    # 发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    data = json.loads(r.text)
    print(data)
    # 提取翻译结果
    # Show response
    dst_len = len(data["trans_result"])
    for j in range(dst_len):
        result = data["trans_result"][j]["dst"]+"\n"
        with open(outputfile_name, 'a', encoding='utf-8') as file:
            file.write(result)
    # print(len(data["trans_result"]))

    print("第%d遍翻译结果:\n"%(i+1))
    # query = result
    with open(outputfile_name, 'r', encoding='utf-8') as file:
        result = file.read()
    print(result+"\n\n")
    query = result
    from_lang = to_lang
    with open(outputfile_name, "w", encoding='utf8') as file:
        texts = file.write("")
    time.sleep(3)



# 将最后翻译得到的随机语言转换为中文,可以自己更改语言
to_lang = lang1
print("转中")

# Generate salt and sign
## 生成签名
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
salt = random.randint(32768, 65536)
sign = make_md5(appid + str(query) + str(salt) + appkey)
# Build request
# 建立请求
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

# Send request
r = requests.post(url, params=payload, headers=headers)
result = r.json()
print(result)
data = json.loads(r.text)

# 提取翻译结果
# Show response
dst_len = len(data["trans_result"])
for j in range(dst_len):
    result = data["trans_result"][j]["dst"]+"\n"
    with open(outputfile_name, 'a', encoding='utf-8') as file:
        file.write(result)
# print(len(data["trans_result"]))

print("第%d遍翻译结果:\n"%(i+1))
# query = result
with open(outputfile_name, 'r', encoding='utf-8') as file:
    result = file.read()
print(result+"\n\n")

time.sleep(1.5)
