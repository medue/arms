#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File run.py
# Date 2019-06-19 10:06
# Author Medue

import yaml
import sys
import os
import get_http
from bs4 import BeautifulSoup

url = 'https://warframe.huijiwiki.com/wiki/%s'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

source_file = open('arms.yaml', encoding="utf-8")
arms = yaml.full_load(source_file)
riven_query_list = {}
new_arms = {}
for riven_info in arms:
    # if arms[riven_info]['query'] is True:
    #     riven_query_list[riven_info] = arms[riven_info]
    new_arms[riven_info] = arms[riven_info]
    request_url = url % arms[riven_info]['cn']
    html = get_http.GetHttp(url=request_url).text
    # left
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.findAll(attrs={"class": 'right'}):
        if str.strip(i.get_text()) == '步枪':
            new_arms[riven_info]['type'] = 'master'
        elif str.strip(i.get_text()) == '近战':
            new_arms[riven_info]['type'] = 'melee'
        elif str.strip(i.get_text()) == '次要':
            new_arms[riven_info]['type'] = 'vice'
yaml.dump(new_arms, source_file)
