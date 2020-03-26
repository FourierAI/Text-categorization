#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: removestopwords.py
# @time: 2020-03-24 21:25
# @desc:
import os
import traceback
import re

def read_stopwords():

    stop_words_file = '../data/filter_rule/stopwords'
    stop_words_set = set()

    with open(stop_words_file) as file:
        for line in file:
            if line != '':
                stop_words_set.add(line.strip())

    return stop_words_set



if __name__ == '__main__':

    stop_words_set = read_stopwords()

    raw_train_path = '../data/raw/20news-bydate-train/'

    category_dir_list = os.listdir(raw_train_path)

    for category_dir in category_dir_list:

        category_file_path = raw_train_path+category_dir

        file_list = os.listdir(category_file_path)

        for file_name in file_list:

            file_path = category_file_path + '/' + file_name
            with open(file_path) as file:

                file_words = []
                # Because of special characters, I use try except to solve
                # this problem to avoid utf-8 exception
                try:
                    for line in file:
                        # convert words into lowercase and find words
                        words_list = re.findall('[a-zA-Z]{1,}',line.lower())
                        words_list = [word for word in words_list if word not in stop_words_set]
                        file_words.extend(words_list)
                except:
                    traceback.print_exc()

                file_content = '\n'.join(file_words)

                # write file content into other folder to save pre-processed data
                pre_processed_path = '../data/removestopwords/20news-bydate-train/'
                target_path = pre_processed_path+category_dir+'/'
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                with open(target_path+file_name,'w') as file:
                    file.write(file_content)
