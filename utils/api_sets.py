import requests
import json



def send_wx(msg,device=None):
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=307d8ea5-2c7a-4346-833f-9e2c700e8b4b"
    headers = {'content-type': 'application/json'}
    device_info = f"\nThis msg is from {device}" if device else ""
    data = {
        "msgtype": "text",
        "text": {
                "content": f"{msg} {device_info}"
            }
    }
    
    return requests.post(webhook, data=json.dumps(data), headers=headers)

def query_epidemic():
    # 查询新冠疫情
    # 返回json格式
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf"
    return requests.get(url)

def social_words():
    # 低级社会语录
    # 返回json
    url = "https://api.oick.cn/yulu/api.php"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()}

def one_word():
    # 每日一言
    url = "https://v.api.aa1.cn/api/yiyan/index.php"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.text[3:-4]}

def heart_hen_soup():
    # 心灵鸡汤
    url = "https://apis.juhe.cn/fapig/soup/query?key=b6bf6efbeaaf8014b9ad5ffbf7a2f25f"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()["result"]["text"]}

def anwei_words():
    # 安慰文案
    url = "https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()["anwei"]}

def famous_words():
    # 名人名言
    url = "https://v.api.aa1.cn/api/api-wenan-mingrenmingyan/index.php?aa1=json"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()[0]["mingrenmingyan"]}

def emotion_words():
    # 情感一言
    url = "https://v.api.aa1.cn/api/api-wenan-qg/index.php?aa1=json"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()[0]["qinggan"]}

def wyy_words():
    # 情感一言
    url = "https://v.api.aa1.cn/api/api-wenan-wangyiyunreping/index.php?aa1=json"
    r = requests.get(url)
    return {"status_code":r.status_code,"text":r.json()[0]["wangyiyunreping"]}

# print(social_words())
# print(one_word())
# print(heart_hen_soup())
# print(anwei_words())
# print(famous_words())
# print(emotion_words())
# print(wyy_words())

