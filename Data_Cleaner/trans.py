import os

def fil(x):
	return list(filter(lambda x:x!="",x))

name=open("/Users/mac/Desktop/CityWander/Streetview_Spider/Catched_data/Shanghai/Shanghai_img_name_file_filtered.txt","r")
name=fil(name.read().split("\n"))

info_db=open("/Users/mac/Desktop/shanghai_info.txt","r")
info_db=fil(info_db.read().split("\n"))

info=open("/Users/mac/Desktop/CityWander/Streetview_Spider/Catched_data/Shanghai/Shanghai_img_info_file.txt","w")

for i in range(len(info_db)):
	d=info_db[i]
	d=d.strip()
	info_db[i]=d.replace("\t","_")

print(info_db)

ss=""
se=set()

for i in name:
	d=i.split("_")
	c1=d[0]
	c2=d[1].split(".")[0]
	if(c1 in se):
		continue
	for j in info_db:
		e=j.split("_")
		f1=e[0]

		if(c1==f1):
			se.add(c1)
			c2=int(c2)
			dd=e[1]+"_"+e[2]+"_"+e[3]+"_"+e[4]+"\n"

			ss+=c1+"_"+str(c2)+"_"+dd

			print(c1+"_"+str(c2)+"_"+dd)

			ss+=c1+"_"+str((c2+90)%360)+"_"+dd
			ss+=c1+"_"+str((c2+180)%360)+"_"+dd
			ss+=c1+"_"+str((c2+270)%360)+"_"+dd


info.write(ss)