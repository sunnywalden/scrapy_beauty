# scrapy_beauty

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](http://github.com/hhyo/archery/blob/master/LICENSE)
[![version](https://img.shields.io/badge/python-3.12.4-blue.svg)](https://www.python.org/downloads/release/python-3124/)

## 一、项目说明

通过scrapy框架，爬虫获取某图片站点美女（仅供交流学习使用，请勿非法获取使用其它站点数据）


## 二、效果图

![预览](./demo/beauty_demo.png)

## 三、部署

### 3.1 部署依赖

请先部署mysql、redis、proxy_pool服务，推荐以docker方式部署
mysql、redis部署，参考官方文档；

proxy_pool部署，参考链接：
https://github.com/jhao104/proxy_pool?tab=readme-ov-file#docker-image

### 3.2 获取代码

```bash
git clone https://github.com/sunnywalden/scrapy_beauty.git
```
### 3.3 安装依赖

```bash
pip install -r requirements.txt
```

### 3.4 运行项目

```bash
scrapy crawl siwa
```


## 四、感谢

代理使用了jhao104的[proxy_pool](https://github.com/jhao104/proxy_pool)项目，在此感谢！

