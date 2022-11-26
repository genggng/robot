import sys
sys.path.append("/home/geng/robot/utils") #加入工具链

import random
import time
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Friend
from graia.ariadne.message.element import Image as botImage


from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

from utils import *


db = Know_DB() #知识库

channel = Channel.current()

key_api = {
   "网易云":wyy_words,
   "谈感情":emotion_words,
   "社会人":social_words,
   "来一句":one_word,
   "喝鸡汤":heart_hen_soup,
   "安慰一下":anwei_words,
   "名人名言":famous_words,
  
}
advance_feature = {
 "画涩图":drew_picture_usage
}

key_system = {
   "主机IP":extract_ip
}

admin_id = 1536967497
host_id = {1536967497,1975597445}  #主人的qq号

guest_feature = "\n".join(list(key_api.keys())+list(advance_feature.keys()))
admin_feature = "\n".join(list(key_api.keys())+list(advance_feature.keys()))

random_reply = [
   "小猫听不懂哦~",
   "这个真不知道啦！",
   "我最近学会了新本领，要不然看看我会啥。问我 技能 ",
   "呵呵，你还挺可爱的（傻萌",
   "老子不听你的啦"
]

@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def setu(app: Ariadne, friend: Friend, message: MessageChain):
   if friend.id in host_id:  #是主人提供服务   
      query = str(message)
      if query == "技能":   #展示技能
         reply = admin_feature if friend.id == admin_id else guest_feature
      elif query in key_api.keys():
         r = key_api[query]()
         if r["status_code"] < 400:
            reply = r["text"]
         else:
            reply = f"出现API错误啦，错误状态码为{r['status_code']},快去请耿耿哥哥解决！"
      elif query in advance_feature.keys():
         r = advance_feature[query]()
         await app.send_message(friend,MessageChain(r["info"])) #高级功能的介绍
         time.sleep(2)  #等待两秒
         reply = r["demo"]  #使用demo
      elif query in key_system.keys() and friend.id == admin_id :
         reply = key_system[query]()
      else:
         #  语句解析
         if "是" in query:  #确定为一个知识增广语句
            k,v = query.split("是")
            db.set_know(k,v)
            reply = "小猫知道啦！"
         elif query[:3] == "我想画":
            begin_drew_reply = "好的呀，让我想想怎么画呢。请给我30秒时间(大概)"
            await app.send_message(friend,MessageChain(begin_drew_reply))
            args = query[3:].lstrip(":").lstrip("：").split("#")
            if len(args) > 4:
               args = args[:4]
            r = txt2img(*args)
            if r["status_code"] < 400:
               reply = botImage(data_bytes=r["image"]) #这里重命名为bot的Image，与PIL区分
            elif r["status_code"] >900:
               reply = "哎呀，你给我的重要性系数或者采样步数不是数字呢~"
            else:
               reply = f"出现API错误啦，错误状态码为{r['status_code']},快去请耿耿哥哥解决！"
         
         elif "涩" in query: #粗鄙之言
            reply = "哒唛！不可以涩涩！"

         else:  #看看数据库里有没有吧
            res = db.get_know(query)
            reply = f"我知道！{query}是"+res if res else random.choice(random_reply)
         
      await app.send_message(friend,MessageChain(reply))
   else:
      return
