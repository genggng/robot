import sys
sys.path.append("/home/geng/robot/utils") #加入工具链

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Friend


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

key_system = {
   "主机IP":extract_ip
}

admin_id = 1536967497
host_id = {1536967497,1975597445}  #主人的qq号

guest_feature = "\n".join(key_api.keys())
admin_feature = "\n".join(list(key_api.keys())+list(key_system.keys()))



@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def setu(app: Ariadne, friend: Friend, message: MessageChain):
   if friend.id in host_id:  #提供服务   
      query = str(message)
      if query == "技能":
         reply = admin_feature if friend.id == admin_id else guest_feature
      elif query in key_api.keys():
         r = key_api[query]()
         if r["status_code"] < 400:
            reply = r["text"]
         else:
            reply = f"出现API错误啦，错误状态码为{r['status_code']},快去请耿耿哥哥解决！"

      elif query in key_system.keys() and friend.id == admin_id :
         reply = key_system[query]()
      else:
         #  语句解析
         if "是" in query:  #确定为一个知识增广语句
            k,v = query.split("是")
            db.set_know(k,v)
            reply = "小猫知道啦！"
         else:  #不是一个增广语句
            res = db.get_know(query)
            reply = f"我知道！{query}是"+res if res else "小猫听不懂哦~"
      await app.send_message(friend,MessageChain(reply))
   else:
      return
