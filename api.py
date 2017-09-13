import json

import music_spider
import netease
from flask import Flask, request

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False


#1.1 获取音乐类别
@app.route('/cz/api/v1.0/music/categories/', methods=['GET'])
def categories():
    data = music_spider.fetch_json_categories()
    return (json.dumps(data),200,{'Content-Type':'application/json;charset=utf-8'})
    # return Response(
    #     response=data,
    #     mimetype="application/json",
    #     status=200
    # )


#1.2 获取音乐详情
@app.route('/cz/api/v1.0/music/detail/', methods=['POST'])
def music_detail():
    catid = request.form.get('catId',88096)
    pageno = request.form.get('pageno',0)
    pagesize = request.form.get('pagesize',50)
    data = music_spider.fetch_music_detail(catid, pageno, pagesize)
    return (json.dumps(data), 200, {'Content-Type': 'application/json;charset=utf-8'})


#1.3 获取歌词
@app.route('/cz/api/v1.0/music/lyric/<mid>', methods=['GET'])
def lyric(mid):
    data = music_spider.fetch_music_lyric(mid)
    return (json.dumps(data), 200, {'Content-Type': 'application/json;charset=utf-8'})


#2.1 创建频道
@app.route('/cz/api/v1.0/channel/create/', methods=['POST'])
def channel_create():
    name = request.form.get('name', '')
    type = request.form.get('type', 0)
    data = netease.app_channel_create(name, type)
    return (data, 200, {'Content-Type': 'application/json'})


#2.2 修改频道
@app.route('/cc/api/v1.0/channel/update/', methods=['POST'])
def channel_update():
    name = request.form.get('name', '')
    cid = request.form.get('cid','')
    type = request.form.get('type', 0)
    data = netease.app_channel_update(name, cid, type)
    return (data, 200, {'Content-Type': 'application/json'})


#2.3 删除频道
@app.route('/cc/api/v1.0/channel/delete/', methods=['POST'])
def channel_delete():
    cid = request.form.get('cid','')
    data = netease.app_channel_delete(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.4 获取频道状态
@app.route('/cc/api/v1.0/channel/status/', methods=['POST'])
def channel_status():
    cid = request.form.get('cid','')
    data = netease.app_channelstats(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.5 获取频道列表
@app.route('/cc/api/v1.0/channel/list/', methods=['POST'])
def channel_list():
    records = request.form.get('records',10)
    pnum = request.form.get('pnum', 1)
    ofield = request.form.get('ofield','ctime')
    sort = request.form.get('sort',0)
    data = netease.app_channellist(records, pnum, ofield, sort)
    return (data, 200, {'Content-Type': 'application/json'})


#2.6 重新获取推流地址
@app.route('/cc/api/v1.0/channel/address/', methods=['POST'])
def channel_address():
    cid = request.form.get('cid','')
    data = netease.app_address(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.7 设置频道为录制状态
@app.route('/cc/api/v1.0/channel/record/', methods=['POST'])
def channel_setAlwaysRecord():
    cid = request.form.get('cid','')
    needRecord = request.form.get('needRecord',1)
    format = request.form.get('format',1)
    duration = request.form.get('duration',5)
    data = netease.app_channel_setAlwaysRecord(cid, needRecord, format, duration)
    return (data, 200, {'Content-Type': 'application/json'})


#2.8 禁用频道
@app.route('/cc/api/v1.0/channel/pause/', methods=['POST'])
def channel_pause():
    cid = request.form.get('cid', '')
    data = netease.app_channel_pause(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.9 批量禁用频道
@app.route('/cc/api/v1.0/channel/listpause/', methods=['POST'])
def channel_listpause():
    cidList = request.form.get('cidList', '')
    data = netease.app_channellist_pause(cidList)
    return (data, 200, {'Content-Type': 'application/json'})


#2.10 恢复频道
@app.route('/cc/api/v1.0/channel/resume/', methods=['POST'])
def channel_resume():
    cid = request.form.get('cid', '')
    data = netease.app_channel_resume(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.11 批量恢复频道
@app.route('/cc/api/v1.0/channel/listresume/', methods=['POST'])
def channel_listresume():
    cidList = request.form.get('cidList', '')
    data = netease.app_channellist_resume(cidList)
    return (data, 200, {'Content-Type': 'application/json'})


#2.12 获取录制视频文件列表
@app.route('/cc/api/v1.0/channel/videolist/', methods=['POST'])
def channel_videolist():
    cid = request.form.get('cid', '')
    records = request.form.get('records',10)
    pnum = request.form.get('pnum',1)
    data = netease.app_videolist(cid, records, pnum)
    return (data, 200, {'Content-Type': 'application/json'})


#2.13 获取某一时间范围的录制视频文件列表
@app.route('/cc/api/v1.0/channel/vodvideolist/', methods=['POST'])
def channel_vodvideolist():
    cid = request.form.get('cid', '')
    beginTime = request.form.get('beginTime')
    endTime = request.form.get('endTime')
    sort = request.form.get('sort',0)
    data = netease.app_vodvideolist(cid, beginTime, endTime, sort)
    return (data, 200, {'Content-Type': 'application/json'})


#2.14 设置视频录制回调地址
@app.route('/cc/api/v1.0/channel/record_setcallback/', methods=['POST'])
def channel_record_setcallback():
    recordClk = request.form.get('recordClk', '')
    data = netease.app_record_setcallback(recordClk)
    return (data, 200, {'Content-Type': 'application/json'})


#2.15 设置回调的加签秘钥
@app.route('/cc/api/v1.0/channel/callback_setsignkey/', methods=['POST'])
def app_callback_setSignkey():
    signKey = request.form.get('signKey', '')
    data = netease.app_callback_setSignkey(signKey)
    return (data, 200, {'Content-Type': 'application/json'})


#2.16 录制文件合并
@app.route('/cc/api/v1.0/channel/video_merge/', methods=['POST'])
def app_video_merge():
    outputName = request.form.get('outputName')
    vidList = request.form.get('vidList')
    data = netease.app_video_merge(outputName, vidList)
    return (data, 200, {'Content-Type': 'application/json'})


#2.17 录制重置
@app.route('/cc/api/v1.0/channel/reset_record/', methods=['POST'])
def app_resetRecord():
    cid = request.form.get('cid','')
    data = netease.app_channel_resetRecord(cid)
    return (data, 200, {'Content-Type': 'application/json'})


#2.18 直播实时转码地址
@app.route('/cc/api/v1.0/channel/transcode_address/', methods=['POST'])
def app_transcodeAddress():
    cid = request.form.get('cid','')
    data = netease.app_transcodeAddress(cid)
    return (data, 200, {'Content-Type': 'application/json'})


if __name__ == '__main__':
    app.run(debug=True)