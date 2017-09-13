from requests import post
import random
import time
import hashlib
import json


base_url = 'https://vcloud.163.com'


AppKey = 'f56158399fc03a62afa3fda8588c494c'
AppSecret = '5c35af8c0ed9'
Nonce = ''.join([str(random.randint(0,9)) for i in range(0,4)])
CurTime = str(int(time.time()))


def CheckSum(appSecret, nonce, curTime):
    hash = hashlib.sha1()
    tmp_str = appSecret+nonce+curTime
    hash.update(tmp_str.encode('utf-8'))
    return hash.hexdigest()


headers = {
    'AppKey':AppKey,
    'Nonce':Nonce,
    'CurTime':CurTime,
    'CheckSum':CheckSum(AppSecret,Nonce,CurTime),
    'Content-Type':'application/json;charset=utf-8'
}


#1.创建频道
def app_channel_create(name,type=0):
    url = 'https://vcloud.163.com/app/channel/create'
    data = {'name':name,'type':type}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

#print(app_channel_create('可爱山妹子',0))


#2.修改频道
def app_channel_update(name, cid, type=0):
    url = 'https://vcloud.163.com/app/channel/update'
    data = {'name':name, 'cid':cid, 'type':type}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# res = app_channel_update('花果山','31859d4251934d3483fb4764f5afc51e')
# print(res)


#3.删除频道
def app_channel_delete(cid):
    url = 'https://vcloud.163.com/app/channel/delete'
    data = {'cid':cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# res = app_channel_delete('c0648ecb30bb4a7e8a7837a5eba5cc68')
# print(res)


#4.获取频道状态
def app_channelstats(cid):
    url = 'https://vcloud.163.com/app/channelstats'
    data = {'cid': cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# res = app_channelstats('11612de819414a5b82603048b2b2e636')
# print(res)


#5.获取频道列表
def app_channellist(records=10,pnum=1,ofield='ctime',sort=0):
    url = 'https://vcloud.163.com/app/channellist'
    data = {'records': records, 'pnum':pnum, 'ofield':ofield, 'sort':sort}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_channellist())


#6.重新获取推流地址
def app_address(cid):
    url = 'https://vcloud.163.com/app/address'
    data = {'cid': cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# res = app_address('11612de819414a5b82603048b2b2e636')
# print(res)


#7.设置频道为录制状态
def app_channel_setAlwaysRecord(cid,needRecord=1,format=1,duration=5):
    url = 'https://vcloud.163.com/app/channel/setAlwaysRecord'
    data = {'cid':cid, 'needRecord':needRecord, 'format':format, 'duration':duration}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# res = app_channel_setAlwaysRecord('11612de819414a5b82603048b2b2e636')
# print(res)


#8.禁用频道
def app_channel_pause(cid):
    url = 'https://vcloud.163.com/app/channel/pause'
    data = {'cid':cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_channel_pause('11612de819414a5b82603048b2b2e636'))


#9.批量禁用频道
def app_channellist_pause(cidList):
    url = 'https://vcloud.163.com/app/channellist/pause'
    data = {'cidList':cidList}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# lis = ['4eefce0910e04bc0bde9262a46265cab','746b24b8a4f24f398f52c92e7c9ff776']
# res = app_channellist_pause(lis)
# print(res)


#10.恢复频道
def app_channel_resume(cid):
    url = 'https://vcloud.163.com/app/channel/resume'
    data = {'cid': cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_channel_resume('11612de819414a5b82603048b2b2e636'))


#11.批量恢复频道
def app_channellist_resume(cidList):
    url = 'https://vcloud.163.com/app/channellist/resume'
    data = {'cidList': cidList}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# lis = ['4eefce0910e04bc0bde9262a46265cab','746b24b8a4f24f398f52c92e7c9ff776']
# res = app_channellist_resume(lis)
# print(res)


#12.获取录制视频文件列表
def app_videolist(cid,records=10,pnum=1):
    url = 'https://vcloud.163.com/app/videolist'
    data = {'cid':cid, 'records':records, 'pnum':pnum}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_videolist('746b24b8a4f24f398f52c92e7c9ff776'))


#13.获取某一时间范围的录制视频文件列表
def app_vodvideolist(cid, beginTime, endTime, sort=0):
    url = 'https://vcloud.163.com/app/vodvideolist'
    data = {'cid':cid, 'beginTime':beginTime, 'endTime':endTime, 'sort':sort}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# starttime = time.mktime(time.strptime('2016-05-05 20:28:54', "%Y-%m-%d %H:%M:%S"))
# res = app_vodvideolist('11612de819414a5b82603048b2b2e636',starttime, time.time())
# print(res)


#14.设置视频录制回调地址
def app_record_setcallback(httpRecordClk):
    url = 'https://vcloud.163.com/app/record/setcallback'
    data = {'recordClk':httpRecordClk}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')


#15.设置回调的加签秘钥
def app_callback_setSignkey(signKey):
    url = 'https://vcloud.163.com/app/callback/setSignKey'
    data = {'signKey':signKey}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')


#16.录制文件合并
def app_video_merge(outputName,vidList):
    url = 'https://vcloud.163.com/app/video/merge'
    data = {'outputName':outputName, 'vidList':vidList}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')


#17.录制重置
def app_channel_resetRecord(cid):
    url = 'https://vcloud.163.com/app/channel/resetRecord'
    data = {'cid':cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_channel_resetRecord('11612de819414a5b82603048b2b2e636'))


#18.直播实时转码地址
def app_transcodeAddress(cid):
    url = 'https://vcloud.163.com/app/transcodeAddress'
    data = {'cid':cid}
    res = post(url, json.dumps(data), headers=headers)
    return res.content.decode('utf-8')

# print(app_transcodeAddress('11612de819414a5b82603048b2b2e636'))