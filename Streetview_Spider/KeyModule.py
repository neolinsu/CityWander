import NetWork;
import json;

#key的保存文件，请按照json格式配置好（具体格式详见key类的toJson()方法导出的格式）
global keyFile;
keyFile = "keys.txt";


#keySet类 ： key列表的存储类，支持自动分配等功能
class keySet:
    #keySet初始化（两种模式：文件名模式和List/Tuple模式）
    def __init__(self,lst=[]):
        self.__lst = [];
        if (isinstance(lst, list) or isinstance(lst, tuple)):
            for i in lst:
                if (isinstance(i, key)):
                    self.__lst.append(i);
        elif (isinstance(lst, str)):
            self.__lst = key.importKeys(lst);

    #keySet中key的总数
    def count(self):
        return len(self.__lst);

    #keySet中可用key的总数
    def availableCount(self):
        t = 0;
        for i in self.__lst:
            if bool(i):
                t += 1;
        return t;

    #返回key列表
    def keys(self):
        return self.__lst;

    #输出所有key的状态统计表（注意：直接输出，不是返回值）
    def getOverView(self):
        t = self.availableCount();
        for i in self.__lst:
            print("%s %s %s" % (i["key"], (" " if bool(i) else "X"), i["time"]));
        print("%s keys in total. %s available. %s unavailable." % (self.count(), t, self.count() - t));

    #获取一个仍然可用的key（如果没有返回None）
    def getAvailableKey(self):
        for i in self.__lst:
            if bool(i):
                return i;
        return None;

    #将keySet导出到指定目录
    def export(self, path):
        try:
            return key.exportKeys(path, self.__lst);
        except:
            return False;


#key类 ： key的存储类，存储内容包含：
#key : key值
#time : 剩余次数
class key:
    #mainKeySet : 整个程序的主key库
    mainKeySet = keySet();

    #key的使用下限阈值
    __alert = 5500;

    #key初始化
    def __init__(self, text, time=10000):
        if (time < 0):
            raise Exception("Time must be positive!");
        self.__text = str(text);
        self.__time = int(time);

    #str类型转换，用于输出key
    def __str__(self):
        return self.__text;

    #int类型转换，用于输出次数
    def __int__(self):
        return self.__time;

    #bool类型转换，用于输出是否允许继续使用（剩余次数小于alert即禁止使用）
    def __bool__(self):
        return self.__time > key.__alert;

    #[]属性支持
    def __getitem__(self, item):
        if (item == "key"):
            return self.__text;
        elif (item == "time"):
            return self.__time;

    #json导入导出支持
    def toJson(self):
        dic = {};
        dic["time"] = self["time"];
        dic["key"] = self["key"];
        return json.dumps(dic);
    @staticmethod
    def fromJson(js):
        try:
            dic = json.loads(js);
            return key(dic["key"], dic["time"]);
        except:
            return None;

    #用此key获取json
    def getUrlJson(self, url):
        try:
            data = NetWork.getdatafromurl(url.replace("$key$", str(self)));
            self.__time -= 1;
            return json.loads(data.decode());
        except Exception as e:
            return None;

    #用此key获取bytes数据
    def getUrlData(self, url):
        try:
            data = NetWork.getdatafromurl(url.replace("$key$", str(self)));
            self.__time -= 1;
            return data;
        except Exception as e:
            return None;

    #用此key获取图片数据
    def getUrlPic(self, url):
        try:
            data = NetWork.getdatafromurl(url.replace("$key$", str(self)));
            print(url.replace("$key$", str(self)));
            self.__time -= 1;
            try:
                obj = json.loads(data.decode());
                return None;
            except:
                return data;
        except Exception as e:
            return None;

    #key列表的导入导出
    @staticmethod
    def importKeys(path):
        try:
            lst = [];
            f = open(path, "r");
            try:
                for i in f.readlines():
                    k = key.fromJson(i);
                    if (k != None):
                        lst.append(k);
                f.close();
                return lst;
            except:
                f.close();
                return[];
        except:
            return [];
    @staticmethod
    def exportKeys(path, lst):
        try:
            f = open(path, "w");
            try:
                for i in lst:
                    if (isinstance(i, key)):
                        f.write(i.toJson() + "\n");
                f.close();
                return True;
            except:
                f.close();
                return False;
        except:
            return False;

