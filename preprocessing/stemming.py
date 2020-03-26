#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: stemming.py
# @time: 2020-03-25 00:26
# @desc:
from nltk.stem.porter import *
import os

if __name__ == '__main__':

    stemmer = PorterStemmer()
    stopwords_train_path = '../data/removestopwords/20news-bydate-train/'
    category_dir_list = os.listdir(stopwords_train_path)

    for category_dir in category_dir_list:
        category_path = stopwords_train_path+category_dir
        file_list = os.listdir(category_path)

        for file_name in file_list:
            file_full_path = category_path+'/'+file_name
            plurals = []
            with open(file_full_path) as file:
                for line in file:
                    plurals.append(line.strip())
            singles = [stemmer.stem(plural) for plural in plurals]

            file_content = '\n'.join(singles)

            # write file content into other folder to save pre-processed data
            stemming_processed_path = '../data/stemming/20news-bydate-train/'
            target_path = stemming_processed_path + category_dir + '/'
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            with open(target_path + file_name, 'w') as file:
                file.write(file_content)