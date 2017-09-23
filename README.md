# CityWander

### Streetview_Spider用法：

#### 一、打开shapefile_reader.py

1、“#基本路径设置”中修改city_name

2、可以先运行shapefile_reader.py，设置stop_cnt变量为Total Points数量，北京应为60000。

3、修改后再运行一次shapefile_reader.py

#### 二、打开key.txt

将所有的time设为10000，当time值小于key_module.py中的alert值时，爬虫将停止。

#### 三、打开main.py

1、“#基本路径设置”中修改city_name

2、直接运行main.py即可。



### 意外情况：

1、main.py执行过程中出现中断，此时请正常结束main.py的运行，如在shell中使用“ctrl+C”，此时main.py会更改key.txt。之后可以重新运行main.py，数据不会丢失，会接着上一次的进度爬取。

2、若想完全重新爬取，需要删除目录“Streetview_Spider/Cache/”下的所有文件，同时删除目录“Streetview_Spider/Catched_data/”中对应城市文件夹中的所有文件。

3、连续出现大量“No pano！”，很可能是因为当天腾讯街景key的额度已经达到上限，此时应该停止爬取，并在下一次爬取前，将key.txt中值设为10000。此时，应查看Cache文件中的Cityname_catchlog_file.txt，并找到最后一条有街景点的记录，将其后的记录内容删除，即可继续上一次的爬取。

