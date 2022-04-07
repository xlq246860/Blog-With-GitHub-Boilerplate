# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Taotie-Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": "xlq246860/Taotie-Blog@gh-pages"
}

# 站点设置
site_name = "Taotie's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2018-12-18T16:51+08:00"
author = "Taotie"
email = "204567450@qq.com"
# author_homepage = "https://www.imalan.cn"
description = "一个人。"
# key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
# external_links = [
#     {
#         "name": "Maverick",
#         "url": "https://github.com/xlq246860",
#         "brief": "🏄‍ Go My Own Way."
#     },
#     {
#         "name": "三無計劃",
#         "url": "https://www.imalan.cn",
#         "brief": "熊猫小A的主页。"
#     }
# ]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
#     {
#         "name": "Twitter",
#         "url": "",
#         "icon": "gi gi-twitter"
#     },
    {
        "name": "GitHub",
        "url": "https://github.com/xlq246860",
        "icon": "gi gi-github"
    }
#     {
#         "name": "Weibo",
#         "url": "",
#         "icon": "gi gi-weibo"
#     }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
