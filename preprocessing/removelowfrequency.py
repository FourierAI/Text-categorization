#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: removelowfrequency.py
# @time: 2020-03-25 23:28
# @desc:

if __name__ == '__main__':

    high_frequency_words = set()
    with open('../data/inverted_index/words_position') as file:
        for line in file:
            if line != '':
                segments = line.split('\t')
                if int(segments[1]) >=5:
                    high_frequency_words.add(segments[0])

    with open('../data/inverted_index/high_doc_frequency_words','a') as file:
        for word in high_frequency_words:
            file.write(word+'\n')