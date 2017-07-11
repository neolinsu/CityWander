from GPSTrans import *
from KeyModule import *
from random import *
import time;
if __name__=="__main__":
    #此行导入数据，请勿删除
    key.mainKeySet = keySet(keyFile);

    '''
    p1 = point("北京航空航天大学");
    p2 = p1.getNearestPoint(includemyself=False);
    print(p1.roadDistance(p2));
    print(p2.getAddress());
    print(p2.getBlockDescription());
    print(p2.getDescription());
    print(p2.getNearbyPoint("小学",10000).getDescription());
    q=p2.getPano();
    print(p1);
    print(p2);
    print(q);
    for i in range(0,361,20):
        q.heading = i;
        print(q.heading,"" if q.saveView("pic%s.jpg"%(q.heading)) else "Error!!!");
    '''

    #input_path

    coordinate_file=open("/Users/mac/Desktop/Guangzhou/Guangzhou_point.txt",'r')

    a=[]
    total=0
    last_catch=0
    last_total=0
    catch_time=0

    img_name_file=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/img_name_file.txt",'a+')
    img_info_file=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/img_info_file.txt",'a+')

    catchlog_file_write = open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/catchlog_file.txt", "a")
    catchlog_file_read=open("/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/catchlog_file.txt","r")

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

    print("++++++++"+str(last_catch)+"&&"+str(last_total))

    total=last_total

    for i in coordinate_file.readlines():

        now_point+=1
        if(now_point<=last_catch): continue
        catchlog_file_write.write("catchtime: " + str(catch_time) + "  try: " + str(now_point-1) + "  catch: " + str(total) + "\n")

        print("Now_point:",now_point)
        print("Total:",total)

        #catchlog_file_write.write("catchtime:"+str(catch_time)+" "+str(last_catch)+" "+str(last_total)+"\n")

        a=i.split(',')
        b=point(round(float(a[0]),6),round(float(a[1]),6))


        if(b.getPano() != None):

            print("Points:")
            print(b)

            total+=1

            try:
                d=b.getPano()
                print(d.pano)
            except:
                continue

            address=b.getAddress()
            description=b.getDescription()

            print(address+" "+description)

            c=randint(0,360)
            for j in range(4):
                d.heading = (c+j*90)%360;

                path="/Users/mac/Desktop/城市漫游/代码/Tecent_Experiment/Guangzhou_Pano/"

                img_info=d.pano+"_"+str(b.lat)+"_"+str(b.lng)+"_"+str(d.heading)+"_"+address +"_" +description
                img_name=d.pano+"_"+str(d.heading)+".jpg"

                img_info_file.write(img_info+"\n")
                img_name_file.write(img_name+"\n")

                d.saveView(path+img_name)

            key.mainKeySet.export(keyFile);
        else:
            print("No pano!")

    catchlog_file_write.write("catchtime: " + str(catch_time) + "  try: " + str(now_point) + "  catch: " + str(total) + "\n")

    print("****************")
    print("Total:",total)
    print("****************")


    img_name_file.close()
    img_info_file.close()
    coordinate_file.close()
    catchlog_file_read.close()
    catchlog_file_write.close()


    key.mainKeySet.getOverView();


    #此行请勿删除，请务必在程序结尾保存数据
    key.mainKeySet.export(keyFile);
