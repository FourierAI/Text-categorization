#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: Invertedindex.py
# @time: 2020-03-25 14:34
# @desc:
import os

if __name__ == '__main__':

    stemming_train_path = '../data/stemming/20news-bydate-train/'
    category_dir_list = os.listdir(stemming_train_path)

    word_set = set()
    for catefory_dir in category_dir_list:

        category_path = stemming_train_path+catefory_dir
        file_list = os.listdir(category_path)

        for file_name in file_list:
            file_full_path = category_path +'/'+file_name
            with open(file_full_path) as file:
                for line in file:
                    word_set.add(line.strip())
    with open('../data/inverted_index/words_list','a') as file:
        for word in word_set:
            file.write(word+'\n')
    print('word set has processed')
    # read document into memory to avoid large read in disk
    document_dic = {}
    for catefory_dir in category_dir_list:
        category_path = stemming_train_path + catefory_dir
        file_list = os.listdir(category_path)

        for file_name in file_list:
            file_full_path = category_path + '/' + file_name
            with open(file_full_path) as file:
                file_content = file.read()
                document_dic[file_full_path] = file_content
    print('document dic has processed')
    word_dict = {}
    for word in word_set:
        for document_index,document_content in document_dic.items():
            if word in document_content and word not in word_dict:
                word_dict[word] = 1
            elif word in document_content and word in word_dict:
                word_dict[word] +=1

    with open('../data/inverted_index/words_position','a') as file:
        for word in word_dict:
            file.write(word+'\t'+str(word_dict[word])+'\n')
    print('word dic has processed')
