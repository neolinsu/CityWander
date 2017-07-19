import os
from GPSTrans import *

#基本路径设置
city_name="Guangzhou"
root_path="/Users/mac/Desktop/CityWander/"
spider_path=root_path+"Streetview_Spider/"
picture_path=root_path+"Streetview_Pictures/"

os.system("ls /Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/Guangzhou_Pano > /Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/catched_img_name.txt") #获取文件目录


catched_img_name=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/catched_img_name.txt","r")
checking=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/checking.txt","w")
img_name_file=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/img_name_file.txt","r")
checked_img_name=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/checked_img_name.txt","w")
img_info_file = open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/img_info_file.txt", 'r')
checked_img_info=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/checked_img_info.txt",'w')
panos=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/panos.txt",'w')


#思路就是两个部分取交集 用文件名+角度作为唯一取交标准


#两个部分都是4的倍数
#1 文件名筛选

name_dict={} #pano,(time,filename)

for i in catched_img_name.readlines():
    d=i.split('_')



#取交

#更新txt 删除图片

panos.close()
catched_img_name.close()
checking.close()
img_name_file.close()
img_info_file.close()
checked_img_name.close()


