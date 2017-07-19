from math import *;
from KeyModule import *;
import json;
global key, near, mainKeySet;

#key : 此处key值请勿改动
#near : 所有附近的距离限制
ky = "$key$";
near = 2000;

#坐标点对象
class point:
    #对象初始化，提供两种初始化方式
    def __init__(self, lat, lng=0):
        if (isinstance(lat,str)): #直接输入地名的情况
            s = "http://apis.map.qq.com/ws/geocoder/v1/?address=%s&key=%s";
            s = s % (NetWork.urlencode(lat), ky);
            obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
            if (obj["status"] != 0):
                return;
            p_lat = obj["result"]["location"]["lat"];
            p_lng = obj["result"]["location"]["lng"];

        elif (isinstance(lat,int) or isinstance(lat,float)) and (isinstance(lng,int) or isinstance(lng,float)):
            #输入经纬坐标的情况
            p_lat = lat;
            p_lng = lng;
        else:
            return;

        self.lat = p_lat;
        self.lng = p_lng;

    #[]属性支持
    def __getitem__(self, item):
        if (item == "lat"):
            return self.lat;
        elif (item == "lng"):
            return self.lng;
    def __setitem__(self, key, value):
        if (key == "lat"):
            self.lat = value;
        elif (key == "lng"):
            self.lng = value;

    #json导入导出支持
    def toJson(self):
        dic = {};
        dic["lat"] = self["lat"];
        dic["lng"] = self["lng"];
        return dic;
    @staticmethod
    def fromJson(js):
        try:
            dic = json.loads(js);
            pnt = point(dic["lat"], dic["lng"]);
            return pnt;
        except:
            return None;

    #转换为boolean，用于检验该对象是否正常，正常为True，异常为False
    def __bool__(self):
        return not(self.__str__()=="No Information");
    #转换为字符串，一般用于直接print
    def __str__(self):
        try:
            return "lat=%.8f lng=%.8f" % (self.lat, self.lng);
        except:
            return "No Information";

    #坐标的加法
    def __add__(self, other):
        if (not (isinstance(other, point))):
            raise Exception("point类无法和其他类型进行加法");
        return point(self.lat + other.lat, self.lng + other.lng);
    #坐标的减法
    def __sub__(self, other):
        if (not (isinstance(other, point))):
            raise Exception("point类无法和其他类型进行减法")
        return self+(-other);
    #坐标前缀+
    def __pos__(self):
        return point(self.lat, self.lng);
    #坐标前缀-
    def __neg__(self):
        return point(-self.lat, -self.lng);
    #相等判断
    def __eq__(self, other):
        if (other==None) and (self.__bool__()==False):
            return True;
        else:
            if (self.__bool__()==False):
                return False;
            if (isinstance(other,point)):
                return (abs(other.lat - self.lat) <= 1e-10) and (abs(other.lng - self.lng) <= 1e-10);

    #计算道路距离（官方接口限制：直线距离不得超过10km)
    def roadDistance(self, pnt):
        if not(self):
            return None;
        if not(isinstance(pnt,point)):
            return None;
        s = "http://apis.map.qq.com/ws/distance/v1/?mode=driving&from=%s,%s&to=%s,%s&key=%s"
        s = s % (self.lat, self.lng, pnt.lat, pnt.lng, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
        if (obj["status"] != 0):
            return None;
        obj = obj["result"]["elements"];
        if (len(obj)==0):
            return None;
        return obj[0]["distance"];

    #计算直线距离
    def straightDistance(self, pnt):
        if not(self):
            return None;
        if not(isinstance(pnt,point)):
            return None;
        try:
            ra = 6378140;  # 赤道半径 (m)
            rb = 6356755;  # 极半径 (m)
            flatten = (ra - rb) / ra;  # 地球扁率
            rad_lat_A = radians(self.lat);
            rad_lng_A = radians(self.lng);
            rad_lat_B = radians(pnt.lat);
            rad_lng_B = radians(pnt.lng);
            pA = atan(rb / ra * tan(rad_lat_A));
            pB = atan(rb / ra * tan(rad_lat_B));
            xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B));
            c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2;
            c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2;
            dr = flatten / 8 * (c1 - c2);
            distance = ra * (xx + dr);
            return distance;
        except ZeroDivisionError:
            return 0;

    #获取当前点的最近点
    #includemyself : 是否包含自身,默认为True
    def getNearestPoint(self, radius=near, includemyself=True):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/place/v1/search?boundary=nearby(%f,%f,%d)&orderby=_distance&key=%s";
        s = s % (self.lat, self.lng, radius, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
        if obj["status"] != 0:
            return None;
        if (len(obj["data"])<1):
            return None;
        lng = obj["data"][0]["location"]["lng"];
        lat = obj["data"][0]["location"]["lat"];
        if (includemyself):
            return point(lat, lng);
        else:
            x = 0;
            while (x < len(obj["data"])):
                lng = obj["data"][x]["location"]["lng"];
                lat = obj["data"][x]["location"]["lat"];
                if not(point(lat,lng)==self):
                    return point(lat, lng);
                x += 1;
            return None;

    #获取当前点的最近Pano点
    def getPano(self):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/streetview/v1/getpano?location=%s,%s&radius=%s&key=%s";
        s = s % (self.lat, self.lng, 200, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
        if obj==None:
            return None
        if obj["status"] != 0:
            return None;
        try:
            if (len(obj["detail"]) < 1):
                return None;
            pn = pano(obj["detail"]["id"]);
            inn = ["heading","pitch","zoom"];
            for i in inn:
                if (i in obj["detail"].keys()):
                    pn[i]=obj["detail"][i];
            return pn;
        except:
            return None;

    #获取当前点的地址
    def getAddress(self):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/geocoder/v1/?location=%s,%s&key=%s";
        s = s % (self.lat, self.lng, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);

        if(obj == None):
            return None

        if not(obj["status"] == 0):
            return None;
        return obj["result"]["address"];

    #获取当前点的描述
    def getDescription(self):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/geocoder/v1/?location=%s,%s&key=%s";
        s = s % (self.lat, self.lng, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);

        if obj==None:
            return None

        if not(obj["status"] == 0):
            return None;
        return obj["result"]["formatted_addresses"]["recommend"];

    #获取当前点行政区描述
    def getBlockDescription(self):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/geocoder/v1/?location=%s,%s&key=%s";
        s = s % (self.lat, self.lng, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);

        if obj==None:
            return None

        if not(obj["status"] == 0):
            return None;
        obj = obj["result"]["address_component"];
        return obj["nation"] + obj["province"] + obj["city"] + obj["district"] + obj["street"] + obj["street_number"];

    #以当前点为中心按照关键词搜索点
    def getNearbyPoint(self, keyword, radius=near):
        if not(self):
            return None;
        s = "http://apis.map.qq.com/ws/place/v1/search?boundary=nearby(%f,%f,%d)&keyword=%s&orderby=_distance&key=%s";
        s = s % (self.lat, self.lng, radius, NetWork.urlencode(keyword), ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
        if obj["status"] != 0:
            return None;
        if (len(obj["data"])<1):
            return None;
        lng = obj["data"][0]["location"]["lng"];
        lat = obj["data"][0]["location"]["lat"];
        return point(lat, lng);

#街景点对象
class pano:
    #初始化pano对象
    def __init__(self, pano):
        self.pano = str(pano);
        self.heading = 0;
        self.pitch = 0;
        self.zoom = 1;
        self.width = 960;
        self.height = 640;

    #[]支持
    def __getitem__(self, item):
        if (item == "pano"):
            return self.pano;
        elif (item == "heading"):
            return self.heading;
        elif (item == "pitch"):
            return self.pitch;
        elif (item == "zoom"):
            return self.zoom;
        elif (item == "height"):
            return self.height;
        elif (item == "width"):
            return self.width;
    def __setitem__(self, key, value):
        if (key == "pano"):
            self.pano = value;
        elif (key == "heading"):
            self.heading = value;
        elif (key == "pitch"):
            self.pitch = value;
        elif (key == "zoom"):
            self.zoom = value;
        elif (key == "height"):
            self.height = value;
        elif (key == "width"):
            self.width = value;

    #json导入导出支持
    def toJson(self):
        dic = {};
        dic["pano"] = self["pano"];
        dic["heading"] = self["heading"];
        dic["pitch"] = self["pitch"];
        dic["zoom"] = self["zoom"];
        dic["height"] = self["height"];
        dic["width"] = self["width"];
        return json.dumps(dic);
    @staticmethod
    def fromJson(js):
        try:
            dic = json.loads(js);
            pn = pano(dic["pano"]);
            pn["heading"] = dic["heading"];
            pn["pitch"] = dic["pitch"];
            pn["zoom"] = dic["zoom"];
            pn["height"] = dic["height"];
            pn["width"] = dic["width"];
            return pn;
        except:
            return None;

    #转化为字符串，主要用于print
    def __str__(self):
        return "Pano = " + self.pano;

    #通过pano求出point
    def getPoint(self):
        s = "http://apis.map.qq.com/ws/streetview/v1/getpano?id=%s&key=%s";
        s = s % (self.pano, ky);
        obj = key.mainKeySet.getAvailableKey().getUrlJson(s);
        if (obj["status"] != 0):
            return None;
        obj = obj["detail"]["location"];
        return point(obj["lat"],obj["lng"]);

    #保存街景图像，成功返回True，失败返回False
    def saveView(self, path):
        try:
            s = "http://apis.map.qq.com/ws/streetview/v1/image?size=%sx%s&pano=%s&zoom=%s&pitch=%s&heading=%s&key=%s";
            s = s % (self.width, self.height, self.pano, self.zoom, self.pitch, self.heading, ky);
            data = key.mainKeySet.getAvailableKey().getUrlPic(s);
            if (data == None):
                return False;
            else:
                f = open(path, "wb");
                f.write(data);
                f.close();
                return True;
        except:
            return False;