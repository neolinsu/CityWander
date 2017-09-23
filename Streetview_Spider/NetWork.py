import urllib.request;
import urllib.parse;
from datetime import *;

#minspan : 最小时间间隔（单位：秒，设为None时无时间间隔）
#lasttime : 最后一次联网时间（勿修改）
#minspan在进行爬虫作业时请务必不要小于0.2，否则访问成功率将无法得到保证（官网上说key的每秒并行最大数量为5）

global minspan, lasttime;
minspan = 0.25;
lasttime = None;

#根据url获取数据 格式：bytes（通用）
def getdatafromurl(url):
    if not (isinstance(url, str)):
        return None;
    global lasttime, minspan;
    if (lasttime != None) and (minspan != None):
        t = 0;
        while (datetime.now() - lasttime).microseconds < (minspan * 1000000):
            t = 1;
    lasttime = datetime.now();

    response = urllib.request.urlopen(url);
    temp = response.read()
    return temp;

def urlencode(url):
    return urllib.parse.quote(string=url, safe='', encoding=None, errors=None);

def urldecode(url):
    return urllib.parse.unquote(string=url, encoding=None, errors=None);
