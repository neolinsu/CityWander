import os
import sys

def fil(x):
	return list(filter(lambda x:x!="",x))

class DataCleaner:
	def __init__(self,city_name_in,city_wander_dir_in):
		self.city_name=city_name_in
		self.city_wander_dir=city_wander_dir_in
		self.data_clean_cache_dir=self.city_wander_dir+"Data_Cleaner/data_clean_cache/"

		#self.pic_dir=
		#dir_format:/Users/mac/Desktop/CityWander/

	def get_file_name(self):
		print("*****In function get_file_name*****")

		def getListFiles(path):
		    ret = [] 
		    for root, dirs, files in os.walk(path):  
		        for filespath in files: 
		            ret.append(os.path.join(root,filespath)) 
		    return ret

		ret = getListFiles(self.city_wander_dir+"Streetview_Pictures/"+self.city_name)
		#for each in ret:
		#	print(each) 

		img_name_file_filtered=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"
					+self.city_name+"/"+self.city_name+"_img_name_file_filtered.txt","w")
		#check_dict=open("/Users/mac/Desktop/"+city_name+"_filename.txt","w")
		#/Users/mac/Desktop/CityWander/Streetview_Spider/Catched_data/Beijing 

		output_str=""
		for i in ret:
			tmp1=i.split("/")
			tmp2=tmp1[len(tmp1)-1]
			output_str+=tmp2+"\n"

		output_str_name=output_str.split("\n")
		output_str_name=fil(output_str_name)

		print("Total files:",len(ret))
		print("Heading 10 files:")
		for i in output_str_name[0:10]:
			print(i)
		print("Other kinds of files:")
		for i in output_str_name:
			if(i.split(".")[1]!="jpg"):
				print(i)

		img_name_file_filtered.write(output_str)

	def error_point_name(self):

		print("*****In function error_point_name*****")

		filtered_name_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"
					+self.city_name+"/"+self.city_name+"_img_name_file_filtered.txt","r")
		filtered_name=filtered_name_file.read().split("\n")
		filtered_name=fil(filtered_name)

		check_dict={}

		error=[]
		for i in range(len(filtered_name)):
			tmp=filtered_name[i].split("_")
			c1=str(tmp[0])
			c2=tmp[1].split(".")[0]
			c2=int(c2)
			if(c1 in check_dict):
				if(c2%90==check_dict[c1][0]):
					check_dict[c1][1]+=1
				else:
					error.append(c1)
					#print(c1)
			else:
				check_dict.setdefault(c1,[c2%90,1])

		for i in check_dict:
			if(check_dict[i][1]!=4):
				error.append(i)

		error=list(set(error))
		error.sort()


		error_name=[]
		error_file=open(self.data_clean_cache_dir+self.city_name+"_img_error_file_name.txt","w")


		for i in error:
			for j in filtered_name:
				tmp=j.split("_")
				c1=str(tmp[0])
				if(i==c1):
					error_name.append(j+"\n")		
			print(i,check_dict[i][1])


		error_file.writelines(error_name)
		print("Total error points using name:",len(error))


	def deleter_name(self):
		print("*****In function deleter_name*****")
		#Be careful!!!!!!!!!!
		error_file=open(self.data_clean_cache_dir+self.city_name+"_img_error_file_name.txt","r").read().split("\n")
		path=self.city_wander_dir+"Streetview_Pictures/"+self.city_name+"/"

		flag=1
		for i in error_file:
			if(i!=""):
				print("rm "+path+i)
				os.system("rm "+path+i)
				flag=0
		if(flag):
			print("Nothing to delete!")


	def get_info(self):

		print("*****In function get_info*****")

		ori_info_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"+
			self.city_name+"/"+self.city_name+"_img_info_file.txt","r")

		ori_info=ori_info_file.read().split("\n")
		ori_info=fil(ori_info)

		filtered_name_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"
			+self.city_name+"/"+self.city_name+"_img_name_file_filtered.txt","r")

		filtered_name=filtered_name_file.read().split("\n")
		filtered_name=fil(filtered_name)

		filtered_pano=[]
		output_str=0
		for i in filtered_name:
			d=i.split("_")
			output_str=d[0]+d[1].split(".")[0]
			filtered_pano.append(d[0]+d[1].split(".")[0])

		print(output_str)

		filtered_pano_set=set(filtered_pano)

		print(len(filtered_pano_set))

		filtered_info=[]
		for i in ori_info:
			dpano=i.split("_")[0]+i.split("_")[1]
			#dpano=
			#print(dpano)
			if(dpano in filtered_pano_set):
				filtered_info.append(i)


		output_str=""
		filtered_info_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"+
			self.city_name+"/"+self.city_name+"_img_info_file_filtered.txt","w")
		
		filtered_info=list(set(filtered_info))

		for i in filtered_info:
			output_str+=i+"\n"

		filtered_info_set=set(filtered_info)

		print("Origin info:",len(ori_info))
		print("Filtered info:",len(filtered_info))
		print("Filtered info set:",len(filtered_info_set))
		filtered_info_file.write(output_str)

	def error_point_info(self):

		print("*****In function error_point_info*****")

		filtered_info_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"
			+self.city_name+"/"+self.city_name+"_img_info_file_filtered.txt","r")

		filtered_info=filtered_info_file.read().split("\n")
		filtered_info=fil(filtered_info)


		check_dict={}

		#len_filtered_name=len(filtered_name)
		error=[]
		for i in filtered_info:
			c=i.split("_")
			c1=str(c[0])
			c2=c[1]
			c2=int(c2)
			if(c1 in check_dict):
				if(c2%90==check_dict[c1][0]):
					check_dict[c1][1]+=1
				else:
					error.append(c1)
					#print(c1)
			else:
				check_dict.setdefault(c1,[c2%90,1])

		for i in check_dict:
			if(check_dict[i][1]!=4):
				error.append(i)

		error=list(set(error))
		error.sort()


		err_name=[]
		err_file=open(self.data_clean_cache_dir+self.city_name+"_img_info_error_file.txt","w")


		for i in error:
			for j in filtered_info:
				c=j.split("_")
				c1=str(c[0])
				if(i==c1):
					err_name.append(c[0]+"_"+c[1]+".jpg\n")		
			print(i,check_dict[i][1])


		err_file.writelines(err_name)
		print("Total error points using info:",len(error))


	def deleter_info(self):

		print("*****In function deleter_info*****")

		error_file=open(self.data_clean_cache_dir+self.city_name+"_img_info_error_file.txt","r").read().split("\n")
		path=self.city_wander_dir+"Streetview_Pictures/"+self.city_name+"/"

		flag=1
		for i in error_file:
			if(i!=""):
				print("rm "+path+i)
				os.system("rm "+path+i)
				flag=0
		if(flag):
			print("Nothing to delete!")

		#delete redundant files


	def error_info_to_name(self):
		print("*****In function error_info_to_name*****")

		filtered_info_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"+
			self.city_name+"/"+self.city_name+"_img_info_file_filtered.txt","r")

		filtered_info=filtered_info_file.read().split("\n")
		filtered_info=fil(filtered_info)

		filtered_name_file=open(self.city_wander_dir+"Streetview_Spider/Catched_data/"
			+self.city_name+"/"+self.city_name+"_img_name_file_filtered.txt","r")

		filtered_name=filtered_name_file.read().split("\n")
		filtered_name=fil(filtered_name)

		filtered_info_to_name=[]

		for i in filtered_info:
			d=i.split("_")
			filtered_info_to_name.append(d[0]+"_"+d[1]+".jpg")


		filtered_info_to_name_set=set(filtered_info_to_name)


		output_str=""
		error_info_to_name=[]
		for i in filtered_name:
			if(i in filtered_info_to_name_set):
				pass
			else:
				output_str+=i+"\n"
				error_info_to_name.append(i)
		#print(output_str)
		print("Total error points using info to name:",len(error_info_to_name))

		error_info_to_name_file=open(self.data_clean_cache_dir+self.city_name+"_img_error_info_to_name_file.txt","w")
		error_info_to_name_file.write(output_str)
	def deleter_info_to_name(self):
		print("*****In function deleter_info_to_name*****")
		error_file=open(self.data_clean_cache_dir+self.city_name+"_img_error_info_to_name_file.txt","r").read().split("\n")
		path=self.city_wander_dir+"Streetview_Pictures/"+self.city_name+"/"

		flag=1
		for i in error_file:
			if(i!=""):
				print("rm "+path+i)
				os.system("rm "+path+i)
				flag=0
		if(flag):
			print("Nothing to delete!")




