#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File get_http.py
# Date 2019-05-30 15:23
# Author Medue

import sys
import os
import string
import json
import pathlib
import requests
from urllib import request
from urllib.parse import quote


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class GetHttp:
    def __init__(self, url, headers=None, charset='utf8'):
        """
        :param url: 要请求的URL
        :param headers: header
        :param charset: 编码
        """
        self._url = url
        self._headers = headers
        if headers is None:
            self._headers = self._get_headers()
        self._response = ''
        self._c = charset

    @staticmethod
    def _get_headers():
        return {'Cookie': 'AD_RS_COOKIE=20080917', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
             Kit/537.36 (KHTML, like Gecko) ''Chrome/58.0.3029.110 Safari/537.36'}

    @property
    def text_content(self):
        """
        获取text内容
        :return: string|text
        """
        self._response = request.urlopen(request.Request(
            url=quote(self._url, safe=string.printable), headers=self._headers)
        )
        try:
            return self._response.read().decode(self._c)
        except Exception as e:
            exit(e)

    @property
    def json_content(self):
        """
        获取json内容
        :return: string|json
        """
        res = requests.get(self._url)
        return json.loads(res.content.decode())

    def unload_img(self, uuid):
        """
        下载图片
        :param uuid: 图片uuid
        :return: string 图片路径
        """
        dir_name = './images'
        if not pathlib.Path(dir_name).is_dir():
            os.mkdir(dir_name)
        file_name = dir_name+'/%s.png' % uuid
        request.urlretrieve(self._url, file_name)
        return file_name
