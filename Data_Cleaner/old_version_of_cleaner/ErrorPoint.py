import os

city_name="Guangzhou"

a=open("/Users/mac/Desktop/"+city_name+"_filename.txt","r")
a=a.read().split("\n")

def fil(x):
	return list(filter(lambda x:x!="",x))

a=fil(a)

a.sort()

b={}

flag=0
lena=len(a)
err=[]
for i in range(lena):
	c=a[i].split("_")
	c1=str(c[0])
	c2=c[1].split(".")[0]
	c2=int(c2)
	if(c1 in b):
		if(c2%90==b[c1][0]):
			b[c1][1]+=1
		else:
			err.append(c1)
			#print(c1)
	else:
		b.setdefault(c1,[c2%90,1])

for i in b:
	if(b[i][1]!=4):
		err.append(i)

err=list(set(err))
err.sort()


err_name=[]
err_file=open("/Users/mac/Desktop/"+city_name+"_img_err_file.txt","w")


for i in err:
	for j in a:
		c=j.split("_")
		c1=str(c[0])
		if(i==c1):
			err_name.append(j+"\n")		
	print(i,b[i][1])


err_file.writelines(err_name)
print("Error:",len(err))

"""
import os
def getListFiles(path):
    ret = [] 
    for root, dirs, files in os.walk(path):  
        for filespath in files: 
            ret.append(os.path.join(root,filespath)) 
    return ret

ret = getListFiles("/Users/mac/Desktop/CityWander/Streetview_Pictures/Shanghai")
#for each in ret:
#	print(each) 
print(len(ret))
"""



