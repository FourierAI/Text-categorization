#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: tfidf.py
# @time: 2020-03-26 23:07
# @desc:
import os
import numpy as np
import pandas as pd
pd.set_option('display.width',130)

import math

if __name__ == '__main__':

    word_list = []
    with open('../data/word2vec/informationgaintop1000') as file:
        for line in file:
            segments = line.strip().split('\t')
            word_key = segments[0]
            word_list.append(word_key)

    document_dict = {}
    stemming_train_path = '../data/stemming/20news-bydate-train/'
    category_dir_list = os.listdir(stemming_train_path)
    for category_dir in category_dir_list:
        category_files = os.listdir(stemming_train_path+category_dir)
        for file_name in category_files:
            with open(stemming_train_path+category_dir +'/'+file_name) as file:
                file_content = file.read()
                document_dict[category_dir+file_name] = file_content


    # fik the frequency of word k in document i
    fik_document = []
    document_name_index = []
    for document_name,document_content in document_dict.items():
        document_name_index.append(document_name)
        fik = []
        for word in word_list:
            frequency = document_content.count(word)
            fik.append(frequency)
        fik_document.append(fik)

    fik_document_np = np.array(fik_document)
    word_vec_frame = pd.DataFrame(fik_document_np, index=document_name_index,columns=word_list)
    print('before td-idf:',word_vec_frame)

    word_times = {}

    for word in word_list:
        times = 0
        for document_name,document_content in document_dict.items():
            if word in document_content:
                times += 1
        word_times[word] = times

    numberofdocument = len(document_dict)

    for word, column_vec in word_vec_frame.iteritems():
        numberoftimesword = word_times.get(word)
        np.log(numberofdocument/numberoftimesword)
        # todo multiply
        column_vec.multiply(np.log(numberofdocument/numberoftimesword))

    print('after td-idf:',word_vec_frame)