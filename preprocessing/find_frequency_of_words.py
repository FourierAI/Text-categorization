#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: find_frequency_of_words.py
# @time: 2020-03-26 14:42
# @desc:

#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: Invertedindex.py
# @time: 2020-03-25 14:34
# @desc:
import os
import word as wd

if __name__ == '__main__':

    stemming_train_path = '../data/stemming/20news-bydate-train/'
    category_dir_list = os.listdir(stemming_train_path)

    word_set = set()
    with open('../data/inverted_index/high_frequency_words') as file:
        for line in file:
            word_set.add(line.strip())
    print('word set has been loaded')
    # read document into memory to avoid large read in disk
    document_dic = {}
    for catefory_dir in category_dir_list:
        category_path = stemming_train_path + catefory_dir
        file_list = os.listdir(category_path)

        for file_name in file_list:
            file_full_path = category_path + '/' + file_name
            with open(file_full_path) as file:
                file_content = file.read()
                document_dic[catefory_dir+'/'+file_name] = file_content
    print('document dic has processed')

    word_frequency = {}
    word_list = []
    for word in word_set:
        wd_instance = wd.Word()
        wd_instance.word_key = word
        category_frequency = {}
        word_count = 0
        for document_index,document_content in document_dic.items():
            category = document_index.split('/')[0]
            if word in document_content:
                word_count +=1
                if word not in word_frequency:
                    word_frequency[word] = 1
                elif word in word_frequency:
                    word_frequency[word] +=1

                # count conditional frequency
                if category not in category_frequency:
                    category_frequency[category] = 1
                elif category in category_frequency:
                    category_frequency[category] += 1

        wd_instance.count = word_count
        wd_instance.category_frequency = category_frequency
        word_list.append(wd_instance)

    with open('../data/inverted_index/words_frequency','a') as file:
        for word in word_frequency:
            file.write(word+'\t'+str(word_frequency[word])+'\n')
    print('word frequency has been processed')

    with open('../data/inverted_index/word_instance','a') as file:
        for word in word_list:
            file.write(str(word)+'\n')
    print('word intances have been processed')


