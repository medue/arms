#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File run.py
# Date 2019-06-19 10:06
# Author Medue

import yaml
from get_http import *
from common import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 获取武器列表
source_file = open('weapons.yaml', encoding="utf-8")
weapons = yaml.full_load(source_file)

# 获取预设武器属性列表
setup_file = open('setup.yaml', encoding="utf-8")
setups = yaml.full_load(setup_file)

# 获取属性列表
attr_file = open('attr.yaml', encoding="utf-8")
attrs = yaml.full_load(attr_file)

query_weapons = {}

# 取出要查询的武器
for weapon in weapons:
    if weapons[weapon]['query'] is True:
        query_weapons[weapon] = weapons[weapon]

if not query_weapons or not setups:
    exit('query list is null')

# 查询结果
result = {}

for weapons_name in setups:
    weapons_price = 0

    # 取出预设价格
    if 'price' in setups[weapons_name]:
        weapons_price = int(setups[weapons_name]['price'])
        del setups[weapons_name]['price']

    # 检查武器是否存在预设属性
    if setups[weapons_name] and weapons[weapons_name]:

        # 检查武器属性是否存在并合法
        check_res = check_attr(attrs=attrs, weapon_type=weapons[weapons_name]['type'], setup=setups[weapons_name])
        if not isinstance(check_res, bool):
            exit(weapons_name+' no attribute '+str(check_res))
    else:
        continue
    # 获取属性ID
    ids = get_attr_id(attrs=attrs, weapon_type=weapons[weapons_name]['type'], setup=setups[weapons_name])
    # 获取uuid请求url
    uuid_url = get_uuid_url(weapon_id=weapons[weapons_name]['id'], ids=ids)

    # 请求紫卡uuid列表并强转list
    uuid_list = GetHttp(url=uuid_url).json_content

    if not uuid_list:
        continue

    for riven_uuid in uuid_list:

        # 过滤没有价格的紫卡
        if not riven_uuid['price']:
            continue

        # 价格超出预设时不处理该卡
        if weapons_price and int(riven_uuid['price']) > weapons_price:
            continue

        # 检查图片是否存在
        image_path = get_img_path(riven_uuid['guid'])
        if not os.path.isfile(image_path):
            # 获取紫卡图片url
            riven_img_url = get_riven_img_url(riven_uuid['guid'])

            # 下载紫卡图片
            image_path = GetHttp(riven_img_url).unload_img(riven_uuid['guid'])

        # 图文识别紫卡属性
        riven_attr_info = graphic_recognition(image_path)

        # 属性格式化
        result[weapons_name] = conversion_recognition(riven_attr_info, weapons_name, weapons, attrs)

        # 添加价格信息
        result[weapons_name]['price'] = riven_uuid['price']
        result[weapons_name]['preset_price'] = weapons_price
print(result)
pass
