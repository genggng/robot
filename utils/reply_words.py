
def drew_picture_usage():
    info = "嘿嘿，被你发现了我的新技能!\n"
    info += "我现在能根据你的描述画一张好看的（涩）图\n"
    info += "如果你想让我画图，请这样说： \n"
    info += "我想画： 想要的特点 # 不要想要特点\n "
    info += "比如，你可以这样对我说： \n 我想画：solo,young girls,dynamic angle #  missing fingers, low quality  \n"
    info +=  "想画出精美的画并不容易，可以参阅这本秘籍 https://docs.qq.com/doc/DWHl3am5Zb05QbGVs \n"
    info +=  "目前只支持英文啦，下面是一个复杂的demo，考验一下你的英语那么样。"

    demo = "我想画:(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow,detailed ice,beautiful detailed water,(beautiful detailed eyes),expressionless,(floating palaces),azure hair,disheveled hair,long bangs, hairs between eyes,(skyblue dress),black ribbon,white bowties,midriff,{{{half closed eyes}}},big forhead,blank stare,flower,large top sleeves # "
    demo += "owres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,missing fingers,bad hands,missing arms,large breasts # 7.0 # 36 "
    return {"info":info,"demo":demo}
# for x in drew_picture_usage().values():
#     print(x)