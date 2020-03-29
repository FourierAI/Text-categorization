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
            # if frequency>0:
            #     print('word:{},document_name:{},frequency{} '.format(word,document_name,frequency))
            fik.append(frequency)
        fik_document.append(fik)

    fik_document_np = np.array(fik_document)
    word_vec_frame = pd.DataFrame(fik_document_np, index=document_name_index,columns=word_list)

    word_vec_frame.to_csv('../data/word2vec/td.csv')

    word_times = {}

    for word in word_list:
        times = 0
        for document_name,document_content in document_dict.items():
            if word in document_content:
                times += 1
        word_times[word] = times

    numberofdocument = len(document_dict)

    row, column = word_vec_frame.shape
    for i in range(column):
        word = word_vec_frame.iloc[:,i].name
        numberoftimesword = word_times.get(word)
        idf = np.log(numberofdocument / numberoftimesword)
        word_vec_frame.iloc[:,i] = word_vec_frame.iloc[:,i]*idf

    # normalize
    normalization = word_vec_frame.apply(lambda x: (x ** 2).sum(), axis=1)
    for i in range(row):
        if normalization[i] != 0:
            print('At {}th row, normailization:{}'.format(i, normalization[i]))
            word_vec_frame.iloc[i,:] = word_vec_frame.iloc[i,:]/normalization[i]

    word_vec_frame.to_csv('../data/word2vec/td-idf.csv')