# CityWander

### Streetview_Spider用法：

一、打开shapefile_reader.py

1、“#基本路径设置”中修改city_name

2、可以先运行shapefile_reader.py，设置stop_cnt变量为Total Points数量，北京应为60000。

3、修改后再运行一次shapefile_reader.py

二、打开main.py

1、“#基本路径设置”中修改city_name

2、直接运行main.py即可。



意外情况：

1、main.py执行过程中出现中断，可以直接继续运行，数据不会丢失，会接着上一次的进度爬取。

2、若想完全重新爬取，需要删除目录“Streetview_Spider/Cache/”下的所有文件，同时删除目录“Streetview_Spider/Catched_data/”中对应城市文件夹中的所有文件。