#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import jieba
import jieba.analyse
jieba.load_userdict("dict_.txt")
txt = open("last_danmu-2.txt", "r", encoding='utf-8').read()
words = jieba.cut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(100):
    word, count = items[i]
    with open("last.txt","a+",encoding="utf-8")as f:
        f.write("{0:<5}{1:>5}".format(word, count)+'\n')
#     print("{0:<5}{1:>5}".format(word, count))

