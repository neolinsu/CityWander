import os
import NetWork
import json

city_name="Guangzhou"
root_path="/Users/mac/Desktop/CityWander/"
spider_path=root_path+"Streetview_Spider/"
picture_path=root_path+"Streetview_Pictures/"
cache_path=spider_path+"Cache/"
catched_data_path=spider_path+"Catched_data/"


def clear_cache():
    os.remove(cache_path+city_name+"_catchlog_file.txt")
    os.remove(cache_path+city_name+"_Points.txt")

def clear_catched_data():
    os.remove(catched_data_path + city_name+"/"+city_name+"_img_name_file.txt")
    os.remove(catched_data_path + city_name+"/"+city_name+"_Points.txt")

#def init_keys():


try:
    clear_cache()
except:
    pass

try:
    clear_catched_data()
except:
    pass