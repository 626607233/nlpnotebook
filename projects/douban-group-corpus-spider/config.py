
# coding: utf8

"""
配置
"""

# 响应头
HEADERS = {
'PC' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
'GalaxyS5' : "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
}

# 豆瓣小组URL
GROUP_DICT = {
	'相互表扬小组': "https://www.douban.com/group/kuakua/"
	# '互相表扬': "https://www.douban.com/group/haogaoxiao/"
}

# 抓取哪些页
PAGE = [0,200]

# 爬虫时间间隔
SPIDER_INTERVAL = 5

# 输出保存路径
OUTPUT_PATH = './static/'

# 数据库配置
SQL_DICT = {
	'user' : 'root',
	'password' : 'biosan#17',
	'ip' : '172.16.0.34',
	'database' : 'corpus_spider'
}

# 代理池地址
# redis
# PROXY_POOL_URL = 'http://localhost:5555/random'
# 芝麻代理 隧道IP
PROXY_POOL_URL = 'http://http.tiqu.alicdns.com/getip3?num=1&type=3&pro=0&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='

# 代理访问重试次数
MAX_GET_RETRY = 20

"""
运行
"""

# 后台运行
# nohup python spider.py --proxy 1 > spider.log 2>&1 &
# 修改config.py
# vi config.py
# 退出vi
# ESC + shift: + wq!
