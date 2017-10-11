import os

city_name="Guangzhou"
def getListFiles(path):
    ret = [] 
    for root, dirs, files in os.walk(path):  
        for filespath in files: 
            ret.append(os.path.join(root,filespath)) 
    return ret

ret = getListFiles("/Users/mac/Desktop/CityWander/Streetview_Pictures/"+city_name)
#for each in ret:
#	print(each) 

a=open("/Users/mac/Desktop/CityWander/Streetview_Spider/Catched_data/"
			+city_name+"/"+city_name+"_img_name_file_filtered.txt","w")
b=open("/Users/mac/Desktop/"+city_name+"_filename.txt","w")
#/Users/mac/Desktop/CityWander/Streetview_Spider/Catched_data/Beijing 

ss=""
for i in ret:
	c=i.split("/")
	d=c[len(c)-1]
	if(d[len(d)-1]=="g"):
		ss+=d+"\n"

ss_name=ss.split("\n")
def fil(x):
	return list(filter(lambda x:x!="",x))
ss_name=fil(ss_name)
print(len(ss_name))
for i in ss_name[0:10]:
	print(i)
print("ERROR")
for i in ss_name:
	if(i.split(".")[1]!="jpg"):
		print(i)

a.write(ss)
b.write(ss)



