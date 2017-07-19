from GPSTrans import *
from KeyModule import *
from random import *
import time;

#基本路径设置
city_name="Guangzhou"
root_path="/Users/mac/Desktop/CityWander/"
spider_path=root_path+"Streetview_Spider/"
picture_path=root_path+"Streetview_Pictures/"

if __name__=="__main__":
    #此行导入数据，请勿删除
    key.mainKeySet = keySet(keyFile);

    #input_path

    coordinate_file=open(spider_path+"Cache/"+city_name+"_Points.txt",'r')

    coordinate=[]
    total=0

    #用于读取上次爬取记录
    last_catch=0
    last_total=0
    catch_time=0

    #这个目录需要手动建立一下
    img_name_file=open(spider_path+"Catched_data/"+city_name+"/"+city_name+"_img_name_file.txt",'a+')
    img_info_file=open(spider_path+"Catched_data/"+city_name+"/"+city_name+"_img_info_file.txt",'a+')

    catchlog_file_write = open(spider_path+"Cache/"+city_name+"_catchlog_file.txt", "a")
    catchlog_file_read = open(spider_path+"Cache/"+city_name+"_catchlog_file.txt", "r")
    catchlog=catchlog_file_read.readlines()
    if(len(catchlog)<1):
        last_catch = 0
        last_total = 0
        catch_time = 1
    else:
        clen=len(catchlog)
        catch_time, last_catch, last_total = list(filter(lambda x:x.isdigit(),catchlog[clen - 1].split()))
        '''
        catch_time = catchlog[clen - 1].lstrip("catchtime:")
        last_catch = catchlog[clen - 1].lstrip("try:")
        last_total = catchlog[clen - 1].lstrip("catch:")
        '''
        catch_time=int(catch_time)+1
        last_catch=int(last_catch)
        last_total=int(last_total)


    now_point=0

    print("++++++++  Last catched points："+str(last_catch)+" && Last total points: "+str(last_total)+"  ++++++++")

    total=last_total

    for i in coordinate_file.readlines():

        now_point+=1
        if(now_point<=last_catch): continue
        catchlog_file_write.write("catchtime: " + str(catch_time) + "  try: " + str(now_point-1) + "  catch: " + str(total) + "\n")

        print(city_name+" Now_point:",now_point)
        print(city_name+" Total:",total)

        #catchlog_file_write.write("catchtime:"+str(catch_time)+" "+str(last_catch)+" "+str(last_total)+"\n")

        coordinate=i.split(',')
        street_point=point(round(float(coordinate[0]),6),round(float(coordinate[1]),6))


        if(street_point.getPano() != None):

            print("Points:")
            print(street_point)

            total+=1

            try:
                img=street_point.getPano() #img为街景对象
                print(img.pano)
            except:
                continue

            address=street_point.getAddress()
            description=street_point.getDescription()

            if address == None :
                continue

            print(address+" "+description)

            start_heading=0
            for j in range(4):
                img.heading = (start_heading+j*90)%360;

                path=picture_path+city_name+"/"

                img_info=img.pano+"_"+str(img.heading)+"_"+str(street_point.lat)+"_"+str(street_point.lng)+"_"+address +"_" +description+".jpg"
                img_name=img.pano+"_"+str(img.heading)+"_"+str(street_point.lat)+"_"+str(street_point.lng)+".jpg"

                img_info_file.write(img_info+"\n")
                img_name_file.write(img_name+"\n")

                img.saveView(path+img_name)

            key.mainKeySet.export(keyFile);
        else:
            print("No pano!")

    catchlog_file_write.write("Catchtime: " + str(catch_time) + "  Try: " + str(now_point) + "  Catched: " + str(total) + "\n")

    print("****************")
    print(city_name+" Total Catched Points:",total)
    print("****************")


    img_name_file.close()
    img_info_file.close()
    coordinate_file.close()
    catchlog_file_read.close()
    catchlog_file_write.close()


    key.mainKeySet.getOverView();


    #此行请勿删除，请务必在程序结尾保存数据
    key.mainKeySet.export(keyFile);
