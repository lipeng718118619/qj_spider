# -*- coding: utf-8 -*-

# Scrapy settings for qj_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qj_spider'

SPIDER_MODULES = ['qj_spider.spiders']
NEWSPIDER_MODULE = 'qj_spider.spiders'

# LOG CONFIG
LOG_LEVEL = 'INFO'
LOG_FILE = "/data/wwwlogs/qj_spider.log"

# picture download path
# /www/wwwroot/default/uploads/allimg
DOWNLOAD_PATH = "/www/wwwroot/default/uploads/allimg"
DOMAIN_NAME = 'http://demo.txjmw.com.cn'

# DataBase Config
DB_USER = 'root'
DB_PASSWORD = 'kevinygn@163.com'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'txjm'

# Redis 增量爬取
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 9379
# REDIS_PARAMS = {
#     'password': 'Dsorg2018'
# }

# LOG_LEVEL = 'INFO'
# LOG_FILE = "/Users/honddy/PycharmProjects/log/qj_spider.log"
#
#
# # picture download path
# DOWNLOAD_PATH = "/Users/honddy/PycharmProjects/allimg"
# DOMAIN_NAME = 'http://demo.txjmw.com.cn'
#
# # DataBase Config
# DB_USER = 'root'
# DB_PASSWORD = 'root'
# DB_HOST = '10.211.55.3'
# DB_PORT = 3306
# DB_NAME = 'test'
#
# # Redis 增量爬取
# REDIS_HOST = '10.211.55.3'
# REDIS_PORT = 6379
# # REDIS_PARAMS = {
# #     'password': 'Dsorg2018'
# # }

# 代理服务器
# PROXY_SERVER = ""
# 代理隧道验证信息
# PROXY_USER = ""
# PROXY_PASS = ""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'qj_spider (+http://www.yourdomain.com)'
# 爬取1000条关闭
CLOSESPIDER_ITEMCOUNT = 10000

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 5
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

SCHEDULER_PERSIST = True
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'qj_spider.middlewares.QjSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'qj_spider.middlewares.SeleniumMiddleware': 1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 200,
    'qj_spider.pipelines.DBDataIsExist': 250,
    'qj_spider.pipelines.RegularProcessingPipeline': 300,
    'qj_spider.pipelines.IndustryTransferPipeline': 400,
    'qj_spider.pipelines.InvestmentAmountPipeline': 500,
    'qj_spider.pipelines.CityTransferPipeline': 600,
    'qj_spider.pipelines.ProjectTypeTransfer': 650,
    'qj_spider.pipelines.DownloadPicturePipeline': 700,
    'qj_spider.pipelines.QjSpiderPipeline': 1000

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]

INDUSTRY = {
    "1": {
        "aid": "1",
        "title": "餐饮",
        "parentid": "0",
        "pinyin": "cyxm",
        "sort": "16"
    },
    "2": {
        "aid": "2",
        "title": "教育",
        "parentid": "0",
        "pinyin": "jyxm",
        "sort": "15"
    },
    "3": {
        "aid": "3",
        "title": "母婴",
        "parentid": "0",
        "pinyin": "myxm",
        "sort": "14"
    },
    "4": {
        "aid": "4",
        "title": "家纺",
        "parentid": "0",
        "pinyin": "jfxm",
        "sort": "13"
    },
    "5": {
        "aid": "5",
        "title": "美容",
        "parentid": "0",
        "pinyin": "mrxm",
        "sort": "12"
    },
    "6": {
        "aid": "6",
        "title": "建材",
        "parentid": "0",
        "pinyin": "jcxm",
        "sort": "11"
    },
    "7": {
        "aid": "7",
        "title": "家居",
        "parentid": "0",
        "pinyin": "jjxm",
        "sort": "10"
    },
    "8": {
        "aid": "8",
        "title": "汽车",
        "parentid": "0",
        "pinyin": "qcxm",
        "sort": "9"
    },
    "9": {
        "aid": "9",
        "title": "环保",
        "parentid": "0",
        "pinyin": "hbxm",
        "sort": "8"
    },
    "10": {
        "aid": "10",
        "title": "干洗",
        "parentid": "0",
        "pinyin": "gxxm",
        "sort": "7"
    },
    "11": {
        "aid": "11",
        "title": "珠宝饰品",
        "parentid": "0",
        "pinyin": "zbspxm",
        "sort": "6"
    },
    "12": {
        "aid": "12",
        "title": "服装配饰",
        "parentid": "0",
        "pinyin": "fzpsxm",
        "sort": "5"
    },
    "13": {
        "aid": "13",
        "title": "医药保健",
        "parentid": "0",
        "pinyin": "yybjxm",
        "sort": "4"
    },
    "14": {
        "aid": "14",
        "title": "零食酒水",
        "parentid": "0",
        "pinyin": "lsjsxm",
        "sort": "3"
    },
    "15": {
        "aid": "15",
        "title": "移动互联网",
        "parentid": "0",
        "pinyin": "ydhlwxm",
        "sort": "2"
    },
    "16": {
        "aid": "16",
        "title": "零售服务",
        "parentid": "0",
        "pinyin": "lsfwxm",
        "sort": "1"
    },
    "17": {
        "aid": "17",
        "title": "火锅",
        "parentid": "1",
        "pinyin": "hgxm",
        "sort": "0"
    },
    "18": {
        "aid": "18",
        "title": "冰淇淋",
        "parentid": "1",
        "pinyin": "bqlxm",
        "sort": "0"
    },
    "19": {
        "aid": "19",
        "title": "中餐",
        "parentid": "1",
        "pinyin": "zcxm",
        "sort": "0"
    },
    "20": {
        "aid": "20",
        "title": "甜品",
        "parentid": "1",
        "pinyin": "tpxm",
        "sort": "0"
    },
    "21": {
        "aid": "21",
        "title": "小吃",
        "parentid": "1",
        "pinyin": "xchxm",
        "sort": "0"
    },
    "22": {
        "aid": "22",
        "title": "快餐",
        "parentid": "1",
        "pinyin": "kcxm",
        "sort": "0"
    },
    "23": {
        "aid": "23",
        "title": "饮品",
        "parentid": "1",
        "pinyin": "ypxm",
        "sort": "0"
    },
    "24": {
        "aid": "24",
        "title": "咖啡",
        "parentid": "1",
        "pinyin": "kfxm",
        "sort": "0"
    },
    "25": {
        "aid": "25",
        "title": "西餐",
        "parentid": "1",
        "pinyin": "xcxm",
        "sort": "0"
    },
    "26": {
        "aid": "26",
        "title": "烘焙",
        "parentid": "1",
        "pinyin": "hbeixm",
        "sort": "0"
    },
    "27": {
        "aid": "27",
        "title": "茶叶",
        "parentid": "1",
        "pinyin": "cyexm",
        "sort": "0"
    },
    "28": {
        "aid": "28",
        "title": "熟食",
        "parentid": "1",
        "pinyin": "ssxm",
        "sort": "0"
    },
    "29": {
        "aid": "29",
        "title": "料理",
        "parentid": "1",
        "pinyin": "llxm",
        "sort": "0"
    },
    "30": {
        "aid": "30",
        "title": "面馆",
        "parentid": "1",
        "pinyin": "mgxm",
        "sort": "0"
    },
    "31": {
        "aid": "31",
        "title": "鸡排",
        "parentid": "1",
        "pinyin": "jpxm",
        "sort": "0"
    },
    "32": {
        "aid": "32",
        "title": "酒店",
        "parentid": "1",
        "pinyin": "jdxm",
        "sort": "0"
    },
    "33": {
        "aid": "33",
        "title": "早教",
        "parentid": "2",
        "pinyin": "zjxm",
        "sort": "0"
    },
    "34": {
        "aid": "34",
        "title": "英语",
        "parentid": "2",
        "pinyin": "yyxm",
        "sort": "0"
    },
    "35": {
        "aid": "35",
        "title": "潜能开发",
        "parentid": "2",
        "pinyin": "qnxm",
        "sort": "0"
    },
    "36": {
        "aid": "36",
        "title": "1对1辅导",
        "parentid": "2",
        "pinyin": "1d1xm",
        "sort": "0"
    },
    "37": {
        "aid": "37",
        "title": "培训",
        "parentid": "2",
        "pinyin": "pxxm",
        "sort": "0"
    },
    "38": {
        "aid": "38",
        "title": "作文",
        "parentid": "2",
        "pinyin": "zwxm",
        "sort": "0"
    },
    "39": {
        "aid": "39",
        "title": "公务员培训",
        "parentid": "2",
        "pinyin": "gwyxm",
        "sort": "0"
    },
    "40": {
        "aid": "40",
        "title": "留学",
        "parentid": "2",
        "pinyin": "lxxm",
        "sort": "0"
    },
    "41": {
        "aid": "41",
        "title": "IT培训",
        "parentid": "2",
        "pinyin": "itjyxm",
        "sort": "0"
    },
    "42": {
        "aid": "42",
        "title": "机器人教育",
        "parentid": "2",
        "pinyin": "jqrxm",
        "sort": "0"
    },
    "43": {
        "aid": "43",
        "title": "在线教育",
        "parentid": "2",
        "pinyin": "zxjyxm",
        "sort": "0"
    },
    "44": {
        "aid": "44",
        "title": "母婴用品",
        "parentid": "3",
        "pinyin": "myypxm",
        "sort": "0"
    },
    "45": {
        "aid": "45",
        "title": "婴儿游泳",
        "parentid": "3",
        "pinyin": "yeyyxm",
        "sort": "0"
    },
    "46": {
        "aid": "46",
        "title": "儿童乐园",
        "parentid": "3",
        "pinyin": "etlyxm",
        "sort": "0"
    },
    "47": {
        "aid": "47",
        "title": "儿童玩具",
        "parentid": "3",
        "pinyin": "etwjxm",
        "sort": "0"
    },
    "48": {
        "aid": "48",
        "title": "月子中心",
        "parentid": "3",
        "pinyin": "yzzxxm",
        "sort": "0"
    },
    "49": {
        "aid": "49",
        "title": "幼儿园",
        "parentid": "3",
        "pinyin": "yeyxm",
        "sort": "0"
    },
    "50": {
        "aid": "50",
        "title": "床上用品",
        "parentid": "4",
        "pinyin": "csypxm",
        "sort": "0"
    },
    "51": {
        "aid": "51",
        "title": "家居布艺",
        "parentid": "4",
        "pinyin": "jjbyxm",
        "sort": "0"
    },
    "52": {
        "aid": "52",
        "title": "窗帘",
        "parentid": "4",
        "pinyin": "clxm",
        "sort": "0"
    },
    "53": {
        "aid": "53",
        "title": "毛浴巾",
        "parentid": "4",
        "pinyin": "myjxm",
        "sort": "0"
    },
    "54": {
        "aid": "54",
        "title": "地毯",
        "parentid": "4",
        "pinyin": "dtxm",
        "sort": "0"
    },
    "55": {
        "aid": "55",
        "title": "竹纤维",
        "parentid": "4",
        "pinyin": "zxwxm",
        "sort": "0"
    },
    "56": {
        "aid": "56",
        "title": "美体瘦身",
        "parentid": "5",
        "pinyin": "mtssxm",
        "sort": "0"
    },
    "57": {
        "aid": "57",
        "title": "化妆品",
        "parentid": "5",
        "pinyin": "hzpxm",
        "sort": "0"
    },
    "58": {
        "aid": "58",
        "title": "美容院",
        "parentid": "5",
        "pinyin": "mryxm",
        "sort": "0"
    },
    "59": {
        "aid": "59",
        "title": "产后恢复",
        "parentid": "5",
        "pinyin": "chhfxm",
        "sort": "0"
    },
    "60": {
        "aid": "60",
        "title": "足疗汗蒸",
        "parentid": "5",
        "pinyin": "zlhzxm",
        "sort": "0"
    },
    "61": {
        "aid": "61",
        "title": "美发美甲",
        "parentid": "5",
        "pinyin": "mfmjxm",
        "sort": "0"
    },
    "62": {
        "aid": "62",
        "title": "香水",
        "parentid": "5",
        "pinyin": "xsxm",
        "sort": "0"
    },
    "63": {
        "aid": "63",
        "title": "门窗",
        "parentid": "6",
        "pinyin": "mcxm",
        "sort": "0"
    },
    "64": {
        "aid": "64",
        "title": "灯饰",
        "parentid": "6",
        "pinyin": "dsxm",
        "sort": "0"
    },
    "65": {
        "aid": "65",
        "title": "地板",
        "parentid": "6",
        "pinyin": "dbxm",
        "sort": "0"
    },
    "66": {
        "aid": "66",
        "title": "五金",
        "parentid": "6",
        "pinyin": "wjxm",
        "sort": "0"
    },
    "67": {
        "aid": "67",
        "title": "吊顶",
        "parentid": "6",
        "pinyin": "ddxm",
        "sort": "0"
    },
    "68": {
        "aid": "68",
        "title": "硅藻泥",
        "parentid": "6",
        "pinyin": "gznxm",
        "sort": "0"
    },
    "69": {
        "aid": "69",
        "title": "瓷砖",
        "parentid": "6",
        "pinyin": "czpp",
        "sort": "0"
    },
    "70": {
        "aid": "70",
        "title": "橱柜",
        "parentid": "7",
        "pinyin": "cgxm",
        "sort": "0"
    },
    "71": {
        "aid": "71",
        "title": "集成灶",
        "parentid": "7",
        "pinyin": "jczjmpp",
        "sort": "0"
    },
    "72": {
        "aid": "72",
        "title": "衣柜",
        "parentid": "7",
        "pinyin": "ygjmpp",
        "sort": "0"
    },
    "73": {
        "aid": "73",
        "title": "电器",
        "parentid": "7",
        "pinyin": "cwdqxm",
        "sort": "0"
    },
    "74": {
        "aid": "74",
        "title": "卫浴",
        "parentid": "7",
        "pinyin": "wyjmpp",
        "sort": "0"
    },
    "75": {
        "aid": "75",
        "title": "新能源汽车",
        "parentid": "8",
        "pinyin": "xnyqcpp",
        "sort": "0"
    },
    "76": {
        "aid": "76",
        "title": "充电桩",
        "parentid": "8",
        "pinyin": "cdzpp",
        "sort": "0"
    },
    "77": {
        "aid": "77",
        "title": "汽车美容",
        "parentid": "8",
        "pinyin": "qcmrxm",
        "sort": "0"
    },
    "78": {
        "aid": "78",
        "title": "智能洗车",
        "parentid": "8",
        "pinyin": "znxcsbxm",
        "sort": "0"
    },
    "79": {
        "aid": "79",
        "title": "车饰",
        "parentid": "8",
        "pinyin": "csxm",
        "sort": "0"
    },
    "80": {
        "aid": "80",
        "title": "养护用品",
        "parentid": "8",
        "pinyin": "qcyhypxm",
        "sort": "0"
    },
    "81": {
        "aid": "81",
        "title": "空气净化",
        "parentid": "9",
        "pinyin": "kqjhxm",
        "sort": "0"
    },
    "82": {
        "aid": "82",
        "title": "污水处理",
        "parentid": "9",
        "pinyin": "wsclxm",
        "sort": "0"
    },
    "83": {
        "aid": "83",
        "title": "固废处理",
        "parentid": "9",
        "pinyin": "gfclxm",
        "sort": "0"
    },
    "84": {
        "aid": "84",
        "title": "洗衣干洗",
        "parentid": "10",
        "pinyin": "xygxxm",
        "sort": "0"
    },
    "85": {
        "aid": "85",
        "title": "皮革护理",
        "parentid": "10",
        "pinyin": "pghlxm",
        "sort": "0"
    },
    "86": {
        "aid": "86",
        "title": "洗衣设备",
        "parentid": "10",
        "pinyin": "gxsbxm",
        "sort": "0"
    },
    "87": {
        "aid": "87",
        "title": "自助洗衣店",
        "parentid": "10",
        "pinyin": "zzxydxm",
        "sort": "0"
    },
    "88": {
        "aid": "88",
        "title": "珠宝",
        "parentid": "11",
        "pinyin": "zbxm",
        "sort": "0"
    },
    "89": {
        "aid": "89",
        "title": "饰品",
        "parentid": "11",
        "pinyin": "spxm",
        "sort": "0"
    },
    "90": {
        "aid": "90",
        "title": "礼品",
        "parentid": "11",
        "pinyin": "lpxm",
        "sort": "0"
    },
    "91": {
        "aid": "91",
        "title": "服装",
        "parentid": "12",
        "pinyin": "fzpp",
        "sort": "0"
    },
    "92": {
        "aid": "92",
        "title": "视力保健",
        "parentid": "13",
        "pinyin": "slbjxm",
        "sort": "0"
    },
    "93": {
        "aid": "93",
        "title": "*屏蔽的关键字*",
        "parentid": "13",
        "pinyin": "crypxm",
        "sort": "0"
    },
    "94": {
        "aid": "94",
        "title": "保健食品",
        "parentid": "13",
        "pinyin": "bjspxm",
        "sort": "0"
    },
    "95": {
        "aid": "95",
        "title": "连锁药店",
        "parentid": "13",
        "pinyin": "lsydxm",
        "sort": "0"
    },
    "96": {
        "aid": "96",
        "title": "保健用品",
        "parentid": "13",
        "pinyin": "bjypxm",
        "sort": "0"
    },
    "97": {
        "aid": "97",
        "title": "大健康",
        "parentid": "13",
        "pinyin": "djkxm",
        "sort": "0"
    },
    "98": {
        "aid": "98",
        "title": "家政服务",
        "parentid": "13",
        "pinyin": "jzfwxm",
        "sort": "0"
    },
    "99": {
        "aid": "99",
        "title": "养老院",
        "parentid": "13",
        "pinyin": "ylyxm",
        "sort": "0"
    },
    "100": {
        "aid": "100",
        "title": "月嫂",
        "parentid": "13",
        "pinyin": "ysxm",
        "sort": "0"
    },
    "101": {
        "aid": "101",
        "title": "白酒",
        "parentid": "14",
        "pinyin": "bjxm",
        "sort": "0"
    },
    "102": {
        "aid": "102",
        "title": "红酒",
        "parentid": "14",
        "pinyin": "hjxm",
        "sort": "0"
    },
    "103": {
        "aid": "103",
        "title": "便利店",
        "parentid": "14",
        "pinyin": "bldxm",
        "sort": "0"
    },
    "104": {
        "aid": "104",
        "title": "进口食品",
        "parentid": "14",
        "pinyin": "jkspxm",
        "sort": "0"
    },
    "105": {
        "aid": "105",
        "title": "互联网金融",
        "parentid": "15",
        "pinyin": "jrxm",
        "sort": "0"
    },
    "106": {
        "aid": "106",
        "title": "互联网医疗",
        "parentid": "15",
        "pinyin": "ylxm",
        "sort": "0"
    },
    "107": {
        "aid": "107",
        "title": "智能制造",
        "parentid": "15",
        "pinyin": "znzzxm",
        "sort": "0"
    },
    "108": {
        "aid": "108",
        "title": "无人技术",
        "parentid": "15",
        "pinyin": "wrjxm",
        "sort": "0"
    },
    "109": {
        "aid": "109",
        "title": "区块链",
        "parentid": "15",
        "pinyin": "qklxm",
        "sort": "0"
    },
    "110": {
        "aid": "110",
        "title": "SaaS",
        "parentid": "15",
        "pinyin": "saasxm",
        "sort": "0"
    },
    "111": {
        "aid": "111",
        "title": "生鲜超市",
        "parentid": "16",
        "pinyin": "sxcsxm",
        "sort": "0"
    },
    "112": {
        "aid": "112",
        "title": "无人超市",
        "parentid": "16",
        "pinyin": "wrcsxm",
        "sort": "0"
    },
    "191": {
        "aid": "191",
        "title": "素质教育",
        "parentid": "2",
        "pinyin": "szjyxm",
        "sort": "0"
    },
    "192": {
        "aid": "192",
        "title": "特色行业",
        "parentid": "0",
        "pinyin": "tsxm",
        "sort": "0"
    },
    "193": {
        "aid": "193",
        "title": "ktv",
        "parentid": "192",
        "pinyin": "ktvxm",
        "sort": "0"
    },
    "194": {
        "aid": "194",
        "title": "潮流",
        "parentid": "192",
        "pinyin": "chlxm",
        "sort": "0"
    },
    "195": {
        "aid": "195",
        "title": "基因检测",
        "parentid": "192",
        "pinyin": "jyjcxm",
        "sort": "0"
    },
    "196": {
        "aid": "196",
        "title": "数码",
        "parentid": "192",
        "pinyin": "smxm",
        "sort": "0"
    },
    "197": {
        "aid": "197",
        "title": "宠物店",
        "parentid": "192",
        "pinyin": "cwdxm",
        "sort": "0"
    },
    "198": {
        "aid": "198",
        "title": "微商",
        "parentid": "192",
        "pinyin": "wsxm",
        "sort": "0"
    },
    "199": {
        "aid": "199",
        "title": "影像",
        "parentid": "192",
        "pinyin": "yxxm",
        "sort": "0"
    },
    "200": {
        "aid": "200",
        "title": "其他",
        "parentid": "0",
        "pinyin": "qtxm",
        "sort": "0"
    },
    "2470": {
        "aid": "2470",
        "title": "外卖",
        "parentid": "1",
        "pinyin": "wmxm",
        "sort": "0"
    },
    "2487": {
        "aid": "2487",
        "title": "新零售",
        "parentid": "16",
        "pinyin": "xlsxm",
        "sort": "0"
    },
    "2488": {
        "aid": "2488",
        "title": "物流",
        "parentid": "192",
        "pinyin": "wlxm",
        "sort": "0"
    },
    "2552": {
        "aid": "2552",
        "title": "女装",
        "parentid": "12",
        "pinyin": "nvzpp",
        "sort": "0"
    },
    "2553": {
        "aid": "2553",
        "title": "内衣",
        "parentid": "12",
        "pinyin": "nypp",
        "sort": "0"
    },
    "2554": {
        "aid": "2554",
        "title": "童装",
        "parentid": "12",
        "pinyin": "tzpp",
        "sort": "0"
    },
    "2555": {
        "aid": "2555",
        "title": "男装",
        "parentid": "12",
        "pinyin": "nanzpp",
        "sort": "0"
    },
    "2556": {
        "aid": "2556",
        "title": "户外",
        "parentid": "12",
        "pinyin": "hwpp",
        "sort": "0"
    },
    "2557": {
        "aid": "2557",
        "title": "运动",
        "parentid": "12",
        "pinyin": "ydpp",
        "sort": "0"
    },
    "2558": {
        "aid": "2558",
        "title": "休闲",
        "parentid": "12",
        "pinyin": "xxpp",
        "sort": "0"
    },
    "2559": {
        "aid": "2559",
        "title": "孕妇装",
        "parentid": "12",
        "pinyin": "yfzpp",
        "sort": "0"
    },
    "2560": {
        "aid": "2560",
        "title": "鞋帽",
        "parentid": "12",
        "pinyin": "xmpp",
        "sort": "0"
    },
    "2561": {
        "aid": "2561",
        "title": "箱包",
        "parentid": "12",
        "pinyin": "xbpp",
        "sort": "0"
    },
    "2562": {
        "aid": "2562",
        "title": "皮具",
        "parentid": "12",
        "pinyin": "pjpp",
        "sort": "0"
    },
    "2563": {
        "aid": "2563",
        "title": "配饰其他",
        "parentid": "12",
        "pinyin": "pspp",
        "sort": "0"
    },
    "2865": {
        "aid": "2865",
        "title": "休闲食品",
        "parentid": "16",
        "pinyin": "xxspxm",
        "sort": "0"
    },
    "2876": {
        "aid": "2876",
        "title": "烧烤",
        "parentid": "1",
        "pinyin": "skxm",
        "sort": "0"
    },
    "2877": {
        "aid": "2877",
        "title": "麻辣烫",
        "parentid": "1",
        "pinyin": "mltxm",
        "sort": "0"
    },
    "2878": {
        "aid": "2878",
        "title": "奶茶",
        "parentid": "1",
        "pinyin": "ncxm",
        "sort": "0"
    },
    "2879": {
        "aid": "2879",
        "title": "少儿英语",
        "parentid": "2",
        "pinyin": "sryyxm",
        "sort": "0"
    }
}

INVESTMENT_AMOUNT = {
    "113": {
        "aid": "113",
        "title": "1-10万",
        "parentid": "0",
        "pinyin": "1-10",
        "sort": "0"
    },
    "114": {
        "aid": "114",
        "title": "10-20万",
        "parentid": "0",
        "pinyin": "10-20",
        "sort": "0"
    },
    "115": {
        "aid": "115",
        "title": "20-50万",
        "parentid": "0",
        "pinyin": "20-50",
        "sort": "0"
    },
    "116": {
        "aid": "116",
        "title": "50-100万",
        "parentid": "0",
        "pinyin": "50-100",
        "sort": "0"
    },
    "117": {
        "aid": "117",
        "title": "100万以上",
        "parentid": "0",
        "pinyin": "100",
        "sort": "0"
    }
}

CITY_CODE = {
    "118": {
        "aid": "118",
        "title": "北京",
        "parentid": "0",
        "pinyin": "beijing",
        "sort": "0"
    },
    "119": {
        "aid": "119",
        "title": "天津",
        "parentid": "0",
        "pinyin": "tianjin",
        "sort": "0"
    },
    "120": {
        "aid": "120",
        "title": "河北",
        "parentid": "0",
        "pinyin": "hebei",
        "sort": "0"
    },
    "121": {
        "aid": "121",
        "title": "山西",
        "parentid": "0",
        "pinyin": "shanxi",
        "sort": "0"
    },
    "122": {
        "aid": "122",
        "title": "内蒙古",
        "parentid": "0",
        "pinyin": "neimenggu",
        "sort": "0"
    },
    "123": {
        "aid": "123",
        "title": "辽宁",
        "parentid": "0",
        "pinyin": "liaoning",
        "sort": "0"
    },
    "124": {
        "aid": "124",
        "title": "吉林",
        "parentid": "0",
        "pinyin": "jilin",
        "sort": "0"
    },
    "125": {
        "aid": "125",
        "title": "黑龙江",
        "parentid": "0",
        "pinyin": "heilongjiang",
        "sort": "0"
    },
    "126": {
        "aid": "126",
        "title": "上海",
        "parentid": "0",
        "pinyin": "shanghai",
        "sort": "0"
    },
    "127": {
        "aid": "127",
        "title": "江苏",
        "parentid": "0",
        "pinyin": "jiangsu",
        "sort": "0"
    },
    "128": {
        "aid": "128",
        "title": "浙江",
        "parentid": "0",
        "pinyin": "zhejiang",
        "sort": "0"
    },
    "129": {
        "aid": "129",
        "title": "安徽",
        "parentid": "0",
        "pinyin": "anhui",
        "sort": "0"
    },
    "130": {
        "aid": "130",
        "title": "福建",
        "parentid": "0",
        "pinyin": "fujian",
        "sort": "0"
    },
    "131": {
        "aid": "131",
        "title": "江西",
        "parentid": "0",
        "pinyin": "jiangxi",
        "sort": "0"
    },
    "132": {
        "aid": "132",
        "title": "山东",
        "parentid": "0",
        "pinyin": "shandong",
        "sort": "0"
    },
    "133": {
        "aid": "133",
        "title": "河南",
        "parentid": "0",
        "pinyin": "hebei",
        "sort": "0"
    },
    "134": {
        "aid": "134",
        "title": "湖北",
        "parentid": "0",
        "pinyin": "hubei",
        "sort": "0"
    },
    "135": {
        "aid": "135",
        "title": "湖南",
        "parentid": "0",
        "pinyin": "hunan",
        "sort": "0"
    },
    "136": {
        "aid": "136",
        "title": "广东",
        "parentid": "0",
        "pinyin": "guangdong",
        "sort": "0"
    },
    "137": {
        "aid": "137",
        "title": "广西",
        "parentid": "0",
        "pinyin": "jiangxi",
        "sort": "0"
    },
    "138": {
        "aid": "138",
        "title": "海南",
        "parentid": "0",
        "pinyin": "hainan",
        "sort": "0"
    },
    "139": {
        "aid": "139",
        "title": "重庆",
        "parentid": "0",
        "pinyin": "chongqing",
        "sort": "0"
    },
    "140": {
        "aid": "140",
        "title": "四川",
        "parentid": "0",
        "pinyin": "sichuan",
        "sort": "0"
    },
    "141": {
        "aid": "141",
        "title": "贵州",
        "parentid": "0",
        "pinyin": "guizhong",
        "sort": "0"
    },
    "142": {
        "aid": "142",
        "title": "云南",
        "parentid": "0",
        "pinyin": "yunnan",
        "sort": "0"
    },
    "143": {
        "aid": "143",
        "title": "西藏",
        "parentid": "0",
        "pinyin": "xizhang",
        "sort": "0"
    },
    "144": {
        "aid": "144",
        "title": "陕西",
        "parentid": "0",
        "pinyin": "shaanxi",
        "sort": "0"
    },
    "145": {
        "aid": "145",
        "title": "甘肃",
        "parentid": "0",
        "pinyin": "gansu",
        "sort": "0"
    },
    "146": {
        "aid": "146",
        "title": "青海",
        "parentid": "0",
        "pinyin": "qinghai",
        "sort": "0"
    },
    "147": {
        "aid": "147",
        "title": "宁夏",
        "parentid": "0",
        "pinyin": "ningxia",
        "sort": "0"
    },
    "148": {
        "aid": "148",
        "title": "新疆",
        "parentid": "0",
        "pinyin": "xinjiang",
        "sort": "0"
    },
    "149": {
        "aid": "149",
        "title": "香港",
        "parentid": "0",
        "pinyin": "xianggang",
        "sort": "0"
    },
    "150": {
        "aid": "150",
        "title": "澳门",
        "parentid": "0",
        "pinyin": "aomen",
        "sort": "0"
    },
    "151": {
        "aid": "151",
        "title": "台湾",
        "parentid": "0",
        "pinyin": "taiwan",
        "sort": "0"
    },
    "152": {
        "aid": "152",
        "title": "美国",
        "parentid": "0",
        "pinyin": "meiguo",
        "sort": "0"
    },
    "153": {
        "aid": "153",
        "title": "英国",
        "parentid": "0",
        "pinyin": "yingguo",
        "sort": "0"
    },
    "154": {
        "aid": "154",
        "title": "欧洲",
        "parentid": "0",
        "pinyin": "ouzhou",
        "sort": "0"
    }
}

PROJECT_TYPES = {19: "火锅加盟项目",
                 23: "冰淇淋加盟项目",
                 28: "中餐加盟项目",
                 31: "甜品加盟项目",
                 35: "小吃加盟项目",
                 39: "快餐加盟项目",
                 42: "饮品加盟项目",
                 46: "咖啡加盟项目",
                 50: "西餐加盟项目",
                 54: "烘焙加盟项目",
                 57: "茶叶加盟项目",
                 61: "熟食加盟项目",
                 64: "料理加盟项目",
                 68: "面食加盟项目",
                 73: "鸡排店加盟项目",
                 76: "酒店加盟项目",
                 79: "快捷酒店加盟项目",
                 94: "早教加盟项目",
                 97: "英语加盟项目",
                 100: "潜能开发加盟项目",
                 103: "1对1辅导加盟项目",
                 106: "培训加盟项目",
                 109: "作文加盟项目",
                 112: "公务员培训加盟项目",
                 115: "留学加盟项目",
                 118: "IT教育加盟项目",
                 121: "机器人教育加盟项目",
                 124: "在线教育加盟项目",
                 134: "母婴用品加盟项目",
                 137: "婴儿游泳加盟项目",
                 141: "儿童乐园加盟项目",
                 145: "儿童玩具加盟项目",
                 149: "月子中心加盟项目",
                 153: "幼儿园加盟项目",
                 158: "床上用品加盟项目",
                 162: "家居布艺加盟项目",
                 166: "窗帘加盟项目",
                 170: "毛浴巾加盟项目",
                 174: "地毯加盟项目",
                 178: "竹纤维加盟项目",
                 183: "美体瘦身加盟项目",
                 187: "化妆品加盟项目",
                 191: "美容院加盟项目",
                 197: "产后恢复加盟项目",
                 201: "足疗汗蒸加盟项目",
                 205: "美发美甲加盟项目",
                 210: "香水加盟项目",
                 216: "橱柜加盟项目",
                 221: "地板加盟项目",
                 226: "门窗加盟项目",
                 232: "衣柜加盟品牌",
                 237: "卫浴加盟品牌",
                 241: "五金加盟项目",
                 246: "吊顶加盟项目",
                 251: "硅藻泥加盟项目",
                 255: "瓷砖加盟品牌",
                 259: "厨卫电器加盟项目",
                 263: "集成灶加盟品牌",
                 267: "灯饰加盟项目",
                 273: "新能源汽车加盟品牌",
                 277: "充电桩加盟品牌",
                 281: "汽车美容加盟项目",
                 285: "智能洗车设备加盟项目",
                 289: "车饰加盟项目",
                 293: "润滑油加盟品牌",
                 301: "空气净化加盟项目",
                 305: "污水处理加盟项目",
                 309: "固废处理加盟项目",
                 314: "洗衣干洗加盟项目",
                 320: "皮革护理加盟项目",
                 324: "干洗设备加盟项目",
                 328: "自助洗衣店加盟项目",
                 333: "珠宝加盟项目",
                 337: "饰品加盟项目",
                 341: "礼品加盟项目",
                 346: "服装加盟品牌",
                 353: "视健保健加盟项目",
                 357: "成人用品加盟项目",
                 361: "保健食品加盟项目",
                 365: "连锁药店加盟项目",
                 369: "保健用品加盟项目",
                 373: "大健康加盟项目",
                 377: "家政服务加盟项目",
                 381: "养老院加盟项目",
                 385: "月嫂加盟项目",
                 390: "白酒加盟项目",
                 394: "红酒加盟项目",
                 398: "便利店加盟项目",
                 402: "进口食品加盟项目",
                 407: "互联网金融加盟项目",
                 411: "互联网医疗加盟项目",
                 415: "智能制造加盟项目",
                 419: "无人机加盟项目",
                 423: "区块链加盟项目",
                 427: "SaaS软件加盟项目",
                 432: "生鲜超市加盟项目",
                 436: "无人超市加盟项目",
                 498: "素质教育加盟项目",
                 503: "ktv加盟项目",
                 507: "潮流加盟项目",
                 511: "基因检测加盟项目",
                 515: "数码加盟项目",
                 519: "宠物店加盟项目",
                 523: "微商加盟项目",
                 527: "影像加盟项目",
                 531: "外卖加盟项目",
                 536: "新零售加盟项目",
                 540: "物流加盟项目",
                 661: "餐饮加盟项目",
                 601: "内衣加盟品牌",
                 604: "童装加盟品牌",
                 608: "男装加盟品牌",
                 611: "户外加盟品牌",
                 614: "运动加盟品牌",
                 617: "休闲加盟品牌",
                 620: "孕妇装加盟品牌",
                 623: "鞋帽加盟品牌",
                 629: "皮具加盟品牌",
                 632: "配饰其他加盟品牌",
                 635: "箱包加盟品牌",
                 662: "教育加盟项目",
                 663: "母婴加盟项目",
                 664: "家纺加盟项目",
                 665: "美容加盟项目",
                 666: "建材加盟项目",
                 667: "家居加盟项目",
                 668: "汽车加盟项目",
                 669: "环保加盟项目",
                 670: "干洗加盟项目",
                 671: "珠宝饰品加盟项目",
                 673: "服装配饰加盟项目",
                 674: "医药保健加盟项目",
                 675: "零食酒水加盟项目",
                 676: "移动互联网加盟项目",
                 677: "零售服务加盟项目",
                 678: "特色行业加盟项目"
                 }
