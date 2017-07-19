import os
from GPSTrans import *
import shapefile

#基本路径设置
city_name="Guangzhou"
root_path="/Users/mac/Desktop/CityWander/"
spider_path=root_path+"Streetview_Spider/"
picture_path=root_path+"Streetview_Pictures/"


img_info_file = open(spider_path+"Catched_data/"+city_name+"/"+city_name+"_img_info_file.txt", 'r')

#point_shp=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/point_shp",'w')

w = shapefile.Writer()
w.autoBalance = 1
w = shapefile.Writer(shapefile.POINT)



w=shapefile.Writer(shapefile.POINT)
w.autoBalance = 1

dic={}

for i in img_info_file.readlines():
    lat=i.split('_')[1]
    lng=i.split('_')[2]

    dic[(lat,lng)]=1

w.field('FIRST_FLD')
w.field('SECOND_FLD', 'C', '40')  # 'SECOND_FLD'为字段名称，C代表数据类型为字符串，长度为40

for i in dic:
    w.point(float(i[1]),float(i[0]))


    w.record(str(i[0])+','+str(i[1]), 'Point')



w.save(root_path+"City_Shapefile/"+city_name+"/"+city_name+"_Catched_Points")
#point_shp.close()


img_info_file.close()


