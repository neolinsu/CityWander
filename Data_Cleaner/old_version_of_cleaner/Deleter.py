import os

city_name="Guangzhou"
a=open("/Users/mac/Desktop/"+city_name+"_img_err_file.txt","r").read().split("\n")
path="/Users/mac/Desktop/CityWander/Streetview_Pictures/"+city_name+"/"

for i in a:
	if(i!=""):
		print("rm "+path+i)
		os.system("rm "+path+i)