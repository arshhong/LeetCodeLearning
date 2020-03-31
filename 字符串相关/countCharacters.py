#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   countCharacters.py
@Time    :   2020/03/17 09:43:29
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。
@solution:    合理利用collect
'''

# here put the import lib
import collections

def sfun(words, chars):
    work_len = 0
    dic = {}
    for word in chars:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for word in words:
        tmp_dic = {}
        for s in word:
            if s not in tmp_dic:
                tmp_dic[s] = 1
            else:
                tmp_dic[s] += 1
        for key in tmp_dic:
            if key not in dic or dic[key]< tmp_dic[key]:
                break
        else:
            work_len += len(word)
    return work_len

def resultfun(words, chars):
    chars_cnt = collections.Counter(chars)
    ans = 0
    for word in words:
        word_cnt = collections.Counter(word)
        for c in word_cnt:
            if chars_cnt[c] < word_cnt[c]:
                break
        else:
            ans += len(word)
    return ans

if __name__ == "__main__":
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    s = sfun(words, chars)
    # s = resultfun(words, chars)
    print(s)