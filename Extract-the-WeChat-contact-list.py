import pandas as pd
import json
from pywechat.WechatAuto import Contacts
# friends_info=Contacts.get_friends_info()
# friends_info=json.loads(friends_info)
# nicknames=[dic.get('昵称') for dic in friends_info]
# remarks=[dic.get('备注') for dic in friends_info]
# wechatnums=[dic.get('微信号') for dic in friends_info]
# friend_data={'昵称':nicknames,'备注':remarks,'微信号':wechatnums}
# friend_data=pd.DataFrame(friend_data,index=range(1,len(nicknames)+1,1))
#这里的路径换成你自己新建的一个空白excel就行
#详细信息
friends_details = Contacts.get_friends_detail()
friends_details=json.loads(friends_details)
#昵称
nicknames=[dic.get('昵称') for dic in friends_details]
#备注
remarks=[dic.get('备注') for dic in friends_details]
#微信号
wechatnums=[dic.get('微信号') for dic in friends_details]
#地区
areas=[dic.get('地区') for dic in friends_details]
#个性签名
tags=[dic.get('标签') for dic in friends_details]
#共同群聊
groups=[dic.get('共同群聊') for dic in friends_details]
#来源
sources=[dic.get('来源') for dic in friends_details]
friend_data={'昵称':nicknames,'备注':remarks,'微信号':wechatnums,'地区':areas,'标签':tags,'共同群聊':groups,'来源':sources}
friend_data=pd.DataFrame(friend_data,index=range(1,len(nicknames)+1,1))
friend_data.to_excel("好友信息.xlsx",index=False)