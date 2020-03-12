#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   string.py
@Time    :   2020/03/12 14:14:54
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
'''

# here put the import lib

def sfun(s):
    size = len(s)

    last_appear_index = [0 for _ in range(26)]
    if_in_stack = [False for _ in range(26)]

    # 记录每个字符最后一次出现的索引
    for i in range(size):
        print(i,s[i],ord(s[i]),ord(s[i])-ord('a'))
        last_appear_index[ord(s[i]) - ord('a')] = i
        print(last_appear_index)

    stack = []
    for i in range(size):
        if if_in_stack[ord(s[i]) - ord('a')]:
            continue

        while stack and ord(stack[-1]) > ord(s[i]) and \
                last_appear_index[ord(stack[-1]) - ord('a')] >= i:
            top = stack.pop()
            if_in_stack[ord(top) - ord('a')] = False

        stack.append(s[i])
        if_in_stack[ord(s[i]) - ord('a')] = True

    return ''.join(stack)


if __name__ == "__main__":
    s = 'cdadabcc'
    a = sfun(s)
    print(a)