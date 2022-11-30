import sys
sys.path.append("/home/geng/robot")

import requests
import json
import base64
from PIL import Image
import io
from cfg import PC_IP


def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
    

def txt2img(prompt="",negative_prompt="",cfg_scale=7,steps=30,resByte=True):
    if not prompt:
        prompt = "((masterpiece)),(((best quality))),((ultra-detailed)),((illustration)), ((disheveled hair))"
    if not negative_prompt:
        negative_prompt = "longbody, lowres, bad anatomy, bad hands, missing fingers, pubic hair,extra digit, fewer digits, cropped, worst quality, low quality"

    prompt = prompt.replace("{","(").replace("}",")")
    negative_prompt = negative_prompt.replace("{","(").replace("}",")")
    if not is_number(cfg_scale) or not is_number(steps):  #非法的参数
        return {"status_code":999,"image":None,"parameters":None}

    sampler_index="Euler a"
    data = {
        "prompt":prompt,
        "negative_prompt":negative_prompt,
        "sampler_index":sampler_index,
        "cfg_scale":cfg_scale,
        "steps":steps
    }
    url = f"http://{PC_IP}:7860/sdapi/v1/txt2img"
    r = requests.post(url,data=json.dumps(data))
    if r.status_code <400:
        data = json.loads(r.content.decode("utf-8"))
        img_base64 = data["images"][0]
        parameters = data["parameters"]
        img_b64decode = base64.b64decode(img_base64)
        image_io = io.BytesIO(img_b64decode)
        if not resByte:
            img = Image.open(image_io)
        else:
            img =  image_io.getvalue() 
    else:
        img = None
        parameters = None
    return {"status_code":r.status_code,"image":img,"parameters":parameters}

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
# print(txt2img())

