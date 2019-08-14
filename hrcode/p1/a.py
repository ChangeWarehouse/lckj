#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'http://www.bluecore.com.cn/'
res = requests.get(url=url).text

with open('./index.html', 'w', encoding='utf-8') as f:
    f.write(res)

