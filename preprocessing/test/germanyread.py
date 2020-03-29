#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: germanyread.py
# @time: 2020-03-29 18:46
# @desc:

import codecs


f = codecs.open('../../data/raw/20news-bydate-train/sci.crypt/14831','r',encoding='Latin1')

lines = f.readlines()
print(lines)

f.close()