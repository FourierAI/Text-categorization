#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: inforgaintop1000.py
# @time: 2020-03-26 17:43
# @desc:
import os
import word as wd
import json
import math

if __name__ == "__main__":

    # load str into memory
    word_list = []
    total_words_count = 0
    with open('../data/inverted_index/word_instance') as file:
        for line in file:
            word = wd.Word()
            segments = line.split('\t')
            word_key = segments[0]
            category_count = segments[1].replace('\'','\"')
            category_frequency = json.loads(category_count)
            word_count = int(segments[2])
            total_words_count += word_count

            word.word_key = word_key
            word.category_frequency = category_frequency
            word.count = word_count
            word_list.append(word)

    # entropy of category
    data_path = '../data/raw/20news-bydate-train/'
    category_dir_list = os.listdir(data_path)
    total_category_frequency = {}
    total_file_count = 0
    for category_dir in category_dir_list:
        file_count = len(os.listdir(data_path+category_dir))
        total_category_frequency[category_dir] = file_count
        total_file_count += file_count


    # compute HC entropy
    HC_entropy = 0
    pc = {}
    for category_dir in total_category_frequency:
        possibility = total_category_frequency[category_dir]/total_file_count
        pc[category_dir] = possibility
        HC_entropy += possibility*math.log(1/possibility)

    # compute HC_W
    for word in word_list:
        # pw
        word_possibility = word.count/total_words_count

        # pw_
        word_possibility_bar = 1 - word_possibility

        # sum p(c|w)log(1/p(c|w))
        summation_pw = 0
        summation_pw_bar = 0
        for category in word.category_frequency:
            ct_possibility = pc.get(category)

            wd_ct_frequency = word.category_frequency[category]
            wd_ct_possibility = wd_ct_frequency/word.count

            summation_pw += wd_ct_possibility*math.log(1/wd_ct_possibility)

            # p(c) = p(w~)p(c|w~) + p(w)p(c|w)
            # p(c|w~) = [p(c) - p(w)p(c|w)]/p(w~)

            wd_ct_complement_possibility = (ct_possibility - word_possibility*wd_ct_possibility)/word_possibility_bar
            summation_pw_bar += wd_ct_complement_possibility*math.log(1/wd_ct_complement_possibility)

        # computer H(C|w)
        HC_W_entropy = word_possibility*summation_pw+word_possibility_bar*summation_pw_bar

        # I(w) information gain = H(c) - H(c|x)
        I_W_gain = HC_entropy - HC_W_entropy

        word.info_gain = I_W_gain

    word_list.sort(key=lambda word:word.info_gain,reverse=True)

    with open('../data/inverted_index/information_gain','a') as file:
        for word in word_list:
            file.write(word.word_key+'\t'+str(word.info_gain)+'\n')