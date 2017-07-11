import shapefile

sf = shapefile.Reader("/Users/mac/Desktop/Guangzhou/Guangzhou_point.shp")
shapes = sf.shapes()
j = 0

file=open("/Users/mac/Desktop/Guangzhou/Guangzhou_point.txt","w")

for i in shapes:
    j+=1
    lng = i.points[0][0]
    lat = i.points[0][1]
    if(j>30000): continue
    file.write(str(lat) +','+ str(lng)+"\n")
