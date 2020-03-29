#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: word.py
# @time: 2020-03-26 14:52
# @desc:
class Word:
    def __init__(self, word_key='', category_frequency={}, count=0.0, info_gain = 0.0):
        self.word_key = word_key
        self.category_frequency = category_frequency
        self.count = count
        self.info_gain = info_gain


    def __repr__(self):
        return self.word_key + '\t' + str(self.category_frequency) + '\t' + str(self.count)