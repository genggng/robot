# robot
一个高度定制化的QQ个人助理。

# 安装配置
## 安装必要的依赖包
1. 安装jdk>11

```shell
sudo apt install openjdk-11-jdk
```
2. 安装Mirai Console Loader用于安装mirai-api-http
```shell
mkdir mcl
cd mcl
wget https://github.com/iTXTech/mirai-console-loader/releases/download/v2.1.2/mcl-2.1.2.zip
unzip mcl-2.1.2.zip
chmod +x mcl
./mcl
```
3. 安装mirai-api-http
```shell
./mcl --update-package net.mamoe:mirai-api-http --channel stable-v2 --type plugin
./mcl -u
```

4. 安装Redis数据库
```shell
sudo apt intall redis-server
```

5. 安装ariadne等python包  
这里假设你使用conda管理python虚拟环境（python>3.8 建议==3.9）
```shell
conda create -n bot python=3.9
conda activate bot
pip install graia-ariadne
pip install graia-saya
pip install redis 
```




## 配置mirai-api-http运行信息
编辑./mcl/config/net.mamoe.mirai-api-http/setting.yml配置文件 (没有则自行创建)
```yml
## 启用的 adapter, 内置有 http, ws, reverse-ws, webhook
adapters:
  - http
  - ws

## 是否开启认证流程, 若为 true 则建立连接时需要验证 verifyKey
enableVerify: true
verifyKey: ServiceVerifyKey  #这个请记一下自己写得啥

## 开启一些调试信息
debug: false

## 是否开启单 session 模式, 不建议开启
singleMode: false

## 历史消息的缓存大小
## 同时，也是 http adapter 的消息队列容量
cacheSize: 4096

## adapter 的单独配置，键名与 adapters 项配置相同
## 注意: 如果 mirai 读取配置时出错可以尝试删除并重新写入
adapterSettings:
  ## HTTP 服务的主机, 端口和跨域设置
  http:
    host: localhost
    port: 8080
    cors: ["*"]

  ## Websocket 服务的主机, 端口和事件同步ID设置
  ws:
    host: localhost
    port: 8080
    reservedSyncId: -1

```
## 配置QQ账号信息  
启动mcl，进入他的终端
```shell
./mcl
```
在mcl终端内，输入如下命令，添加你的QQ信息
```shell
/autoLogin add <你的QQ号> <你的QQ密码>
```
这里默认是使用安卓手机QQ登录，可以在./config/Console/AutoLogin.yml内修改模拟登录的设备(注意看清楚账号，修改的是自己的信息)
```yml
accounts: 
  - # 账号, 现只支持 QQ 数字账号
    account: 123456
    password: 
      # 密码种类, 可选 PLAIN 或 MD5
      kind: PLAIN
      # 密码内容, PLAIN 时为密码文本, MD5 时为 16 进制
      value: pwd
    # 账号配置. 可用配置列表 (注意大小写):
    # "protocol": "ANDROID_PHONE" / "ANDROID_PAD" / "ANDROID_WATCH" / "MACOS" / "IPAD"
    # "device": "device.json"
    # "enable": true
    # "heartbeatStrategy": "STAT_HB" / "REGISTER" / "NONE"
    configuration: 
      protocol: ANDROID_PHONE   #修改你的模拟登录设备 比如 IPAD
      device: device.json
      enable: true
      heartbeatStrategy: STAT_HB
```
执行`./mcl`启动终端服务，此时会自动登录你的QQ。  
如果不出意外的话，出现`Event: BotOnlineEvent(bot=Bot(<你的QQ号>))` 信息。  
那么恭喜你, 你的QQ机器人已经调教好了，请享用。  
但是，如果出现弹窗，请参考这个教程[`3.登录QQ`](https://graia.readthedocs.io/ariadne/appendix/mah-install/)部分解决。

# 如何使用
1. `启动redis服务`(如果设置服务自启动，请忽略)  
    查看redis是否启动。
    ```shell
    redis-cli
    ```
    如果出现`Could not connect to Redis at 127.0.0.1:6379: Connection refused`，证明没开启redis服务，使用下面的程序开启服务
    ```shell
    redis-server &
    ```
2. 启动`mirai-api-http`
    ```shell
    ./mcl
    ```
3. 启动`ariadne`服务程序
    ```shell
    python server.py
    ```
    注意2和3需要开启两个shell窗口，你可以使用`tmux`等实现端口复用。

## 功能介绍
TODO


