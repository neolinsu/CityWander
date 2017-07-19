import shapefile

#基本路径设置
city_name="Guangzhou"
root_path="/Users/mac/Desktop/CityWander/"
spider_path=root_path+"Streetview_Spider/"
picture_path=root_path+"Streetview_Pictures/"

shapes_temp = shapefile.Reader(root_path+"City_Shapefile/"+city_name+"_Points.shp")
shapes = shapes_temp.shapes() #shp中的所有点存在这里，用point方法访问
j = 0

file=open(spider_path+"Cache/"+city_name+"_Points.txt","w")

print(city_name+" Total Points:%d"%len(shapes))

for i in shapes:
    j+=1
    lng = i.points[0][0]
    lat = i.points[0][1]
    if(j>100): continue
    file.write(str(lat) +','+ str(lng)+"\n")
