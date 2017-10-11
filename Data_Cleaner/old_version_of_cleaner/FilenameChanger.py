import os
import sys

path = "/Users/mac/Desktop/CityWander/Streetview_Pictures/Shanghai/"

#path="/Users/mac/Desktop/test/"

for (path,dirs,files) in os.walk(path):
    for filename in files:
    	print(filename)
    	a = filename.split("-")
    	if(len(a)>=2):
	    	newname=a[0]+"_"+a[1]
	    	os.rename(path+filename , path+newname)