#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: choosetop1000.py
# @time: 2020-03-26 22:50
# @desc:

if __name__ == "__main__":

    word_list = []
    with open('../data/inverted_index/information_gain') as file:
        for line in file:
            word_list.append(line)

    with open('../data/word2vec/informationgaintop1000','a') as file:
        for word in word_list[:1000]:
            file.write(word)