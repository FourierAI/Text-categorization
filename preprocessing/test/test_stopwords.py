#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: test_stopwords.py
# @time: 2020-03-28 19:47
# @desc:
import traceback
import re

# if __name__ == "__main__":
test = ["Without God, Without Creed is, rather, the intellectual history of the fate","Without God, Without Creed, The Johns Hopkins University Press, Baltimore,"]

file_words = []
# Because of special characters, I use try except to solve
# this problem to avoid utf-8 exception
try:
    for line in test:
        # convert words into lowercase and find words
        words_list = re.findall('[a-zA-Z]{1,}',line.lower())
        # words_list = [word for word in words_list if word not in stop_words_set]
        file_words.extend(words_list)
except:
    traceback.print_exc()

file_content = '\n'.join(file_words)

print(file_content)