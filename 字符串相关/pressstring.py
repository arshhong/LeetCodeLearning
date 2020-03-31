#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pressstring.py
@Time    :   2020/03/16 09:36:49
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
'''

# here put the import lib

def fun(S):
    if not S :
        return ""
    cnt = 0
    flg = S[0]
    result = ''
    for i in S:
        if i == flg:
            cnt += 1
        else:
            result += flg + str(cnt)
            flg = i
            cnt = 1
    result += flg + str(cnt)
    if len(result) >= len(S):
        result = S
    return result

if __name__ == "__main__":
    S = "aabcccccaaa"
    s = fun(S)
    print(s)