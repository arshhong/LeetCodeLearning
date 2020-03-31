#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findSubstring.py
@Time    :   2020/03/20 15:20:20
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
'''

# here put the import lib
import collections

def sfun(s, words):
    res = []
    words_dic = collections.Counter(words)
    flg = 0
    for word in words_dic:
        word_len = len(words_dic)
        
    return res

if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    r = sfun(s)
    print(r)