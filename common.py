#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File common.py
# Date 2019-06-29 16:16
# Author Medue

import re
import os
from pytesseract import *

base_url = "https://10o.io"


def check_attr(**params):
    """
    检测属性是否存在
    :param params: 参数组
    :return: string|bool
    """
    for p in {'attrs', 'weapon_type', 'setup'}:
        if p not in params:
            return False
    weapon_type = params.get('weapon_type')
    attrs = params.get('attrs')
    setup = params.get('setup')
    master = params.get('master')
    curse = params.get('curse')
    if weapon_type not in attrs:
        return False

    def __check_attr_set(attr_name):
        """
        检测属性舒服存在
        :param attr_name: 属性名
        :return: string|bool
        """
        if attr_name not in setup:
            return ''
        if isinstance(setup[attr_name], list):
            for attr_num in range(len(setup[attr_name])):
                if setup[attr_name][attr_num] not in attrs[weapon_type]:
                    return setup[attr_name][attr_num]
        elif isinstance(setup[attr_name], dict):
            for attr_num in setup[attr_name]:
                if setup[attr_name][attr_num] not in attrs[weapon_type]:
                    return setup[attr_name][attr_num]
        return True
    if master:
        res = __check_attr_set(attr_name=master)
        if not isinstance(res, bool):
            return res
    if curse:
        res = __check_attr_set(attr_name=curse)
        if not isinstance(res, bool):
            return res
    if isinstance(setup, list) or isinstance(setup, dict):
        for setup_attr in setup:
            res = __check_attr_set(attr_name=setup_attr)
            if not isinstance(res, bool):
                return res
    else:
        res = __check_attr_set(attr_name=setup)
        if not isinstance(res, bool):
            return res
    return True


def get_attr_id(**params):
    """
    获取相关的属性id
    :param params: 参数组
    :return: string|bool|dict
    """
    for p in {'attrs', 'weapon_type', 'setup'}:
        if p not in params:
            return False
    weapon_type = params.get('weapon_type')
    attrs = params.get('attrs')
    setup = params.get('setup')
    check_res = check_attr(weapon_type=weapon_type, attrs=attrs, setup=setup)
    if not isinstance(check_res, bool):
        return check_res
    ids = {}
    for attr_type in setup:
        ids[attr_type] = []
        for attr_t in range(len(setup[attr_type])):
            ids[attr_type].append(attrs[attr_type][setup[attr_type][attr_t]]['id'])
    return ids


def get_uuid_url(weapon_id, ids):
    """
    获取uuid请求url
    :param weapon_id 武器id
    :param ids: 属性ids
    :return: string
    """
    uri = '/killshot/search?rivenType=280'
    # uri = '/killshot/search?rivenType=280'+str(weapon_id)
    for attr_type in ids:
        if attr_type.find('curse') >= 0:
            # 紫卡只允许有一条负属性
            uri = uri+"&curse=%s" % str(ids[attr_type][0])
        else:
            query_params = "&buffs="
            for attr_id_key in range(len(ids[attr_type])):
                query_params = query_params + "%d," % ids[attr_type][attr_id_key]
            uri = uri+query_params[:-1]
    return base_url+uri


def get_riven_img_url(uuid):
    """
    获取紫卡图片url
    :param uuid: 紫卡uuid
    :return: string
    """
    uri = '/rimg/'
    return base_url+uri+uuid


def get_img_path(uuid):
    """
    获取图片路径
    :param uuid: 图片uuid
    :return: string|None
    """
    file = './images/%s.png' % uuid
    return file


def graphic_recognition(img_path):
    """
    图文识别
    :param img_path: 图片路径
    :return: string
    """
    res = image_to_string(img_path)
    return res


def get_attr_cn(attr_name, weapons_name, weapons, attrs, p_and_n='p'):
    """
    获取武器属性中文名
    :param attr_name: 属性名
    :param weapons_name: 武器名
    :param weapons: 武器列表
    :param attrs: 属性列表
    :param p_and_n: 正或负
    :return: None|string
    """
    if 'type' in weapons[weapons_name]:
        weapon_type = weapons[weapons_name]['type']
        if p_and_n == 'p':

            if attr_name in attrs[weapon_type] and 'cn' in attrs[weapon_type][attr_name]:
                return attrs[weapon_type][attr_name]['cn']
        else:
            weapon_type = weapon_type+"_curse"
            if attr_name in attrs[weapon_type] and 'cn' in attrs[weapon_type][attr_name]:
                return attrs[weapon_type][attr_name]['cn']
    return None


def conversion_recognition(res, weapons_name, weapons, attrs):
    """
    处理紫卡属性
    :param res: 紫卡属性字符串
    :param weapons_name: 武器名
    :param weapons: 武器列表
    :param attrs: 属性列表
    :return: dict
    """
    res_list = res.split('\n')
    weapon_type = weapons[weapons_name]['type']
    result = {'weapons_name': weapons[weapons_name]['cn'], 'mr': None, 'attr': {}}
    for info_key in range(len(res_list)):
        if res_list[info_key]:
            riven_attr_info = str.rstrip(res_list[info_key])
            riven_attr_info = riven_attr_info.replace(' ', '')
            if not riven_attr_info:
                continue

            if riven_attr_info.find('MR') and riven_attr_info.find('%') < 0:
                # 处理重置次数
                mr = re.sub(r'\D', "", riven_attr_info)
                if mr:
                    result['mr'] = mr

            elif riven_attr_info.find('%') and riven_attr_info.find('%') > 0:
                attr_value = re.search(r'\d+(\.\d+)?', riven_attr_info).group()
                attr_name = ''.join(re.findall(r'[A-Za-z]', riven_attr_info))

                # 识别属性
                if riven_attr_info.find('+') >= 0 and riven_attr_info.find('WeaponRecoil') < 0:
                    attr_name = '+' + get_attr_cn(attr_name, weapons_name, weapons, attrs, 'p')
                    if weapon_type not in result['attr']:
                        result['attr'][weapon_type] = {}
                    result['attr'][weapon_type][attr_name] = attr_value
                else:
                    if riven_attr_info.find('WeaponRecoil') >= 0:
                        attr_name = '+' + str(get_attr_cn(attr_name, weapons_name, weapons, attrs, 'n'))
                    else:
                        attr_name = '-' + str(get_attr_cn(attr_name, weapons_name, weapons, attrs, 'n'))
                    weapon_type = str('+'+weapon_type)+'_curse'
                    if weapon_type not in result['attr']:

                        result['attr'][weapon_type] = {}
                    result['attr'][weapon_type][attr_name] = attr_value
    return result
