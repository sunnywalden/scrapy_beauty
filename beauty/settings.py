# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler

# Scrapy settings for beauty project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'beauty'

SPIDER_MODULES = ['beauty.spiders']
NEWSPIDER_MODULE = 'beauty.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'beauty.middlewares.BeautySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    'beauty.middlewares.BeautyDownloaderMiddleware': 543,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':None,
#    'beauty.middlewares.BeautySpiderMiddleware':125,
#    'beauty.middlewares.ProxyMiddleWare':125,
#    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'beauty.pipelines.BeautyItemPipeline': 300,
    'beauty.pipelines.FileDownloadPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MEDIA_ALLOW_REDIRECTS = True
FILES_STORE = '/Users/sunnywalden/beauty_images' # 保存图片的路径，请修改
FILES_EXPIRES = 90
LOG_FILE = "beauty/logs/beauty.log"
LOG_ENCODING = "UTF-8"
LOG_ENABLED = True
LOG_LEVEL = logging.INFO
LOG_MAX_BYTES = 2 * 1024 * 1024  # 2MB
LOG_BACKUP_COUNT = 3  # Number of backup files to keep

handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
logging.basicConfig(level=LOG_LEVEL, handlers=[handler])

DOWNLOAD_FAIL_ON_DATALOSS = False
DOWNLOAD_TIMEOUT = 15
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#RETRY_HTTP_CODECS = "500,502,503,504,408"
PROXY_LIST = '/tmp/proxies_beauty.txt'
PROXY_MODE = 0

#IMAGES_THUMBS = {
#    'small': (50, 50),
#    'big': (270, 270),
#}

MYSQL_HOST = '192.168.0.1' # 数据库IP，请修改
MYSQL_DBNAME = 'beauty'         #数据库名字，请修改
MYSQL_USER = 'user'             #数据库账号，请修改
MYSQL_PASSWD = 'yourPassword'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
