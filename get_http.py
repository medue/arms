#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File get_http.py
# Date 2019-05-30 15:23
# Author Medue

import sys
import os
import string
from urllib import request
from urllib.parse import quote


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class GetHttp:
    def __init__(self, url, headers=None, charset='utf8'):
        if headers is None:
            headers = self._get_headers()
        self._response = ''
        try:
            self._response = request.urlopen(request.Request(url=quote(url, safe=string.printable), headers=headers))
        except Exception as e:
            exit(e)
        self._c = charset

    @staticmethod
    def _get_headers():
        return {'Cookie': 'AD_RS_COOKIE=20080917', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
             Kit/537.36 (KHTML, like Gecko) ''Chrome/58.0.3029.110 Safari/537.36'}

    @property
    def text(self):
        try:
            return self._response.read().decode(self._c)
        except Exception as e:
            exit(e)
