## 快速尝试
```
python3 main.py
```
访问 http://127.0.0.1:5000/ 即可。

## 本地启动
1. 开启虚拟环境
```shell
source venv/bin/activate
```

2. 获取数据
```
# 周期性数据爬取，每隔180s重新运行一次爬虫程序
python3 spider/schedule.py

# 单次数据爬取
python3 spider/kuakua.py
```
生成的数据会在spider/data.txt文件中

3. 数据处理
```
python3 spider/process.py
```
数据处理之后的数据会存放在finaldata.txt文件中。

4. 提供服务
```
python3 main.py
```

访问 http://127.0.0.1:5000/ 即可看到效果。


## docker
```shell
docker build -t  kuakua:latest . 
docker container run -d --name kuakua -p 5000:5000 kuakua:latest
```
测试
访问 http://127.0.0.1:5000/ 即可看到效果。
