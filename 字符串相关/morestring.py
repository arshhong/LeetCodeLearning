#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   morestring.py
@Time    :   2020/03/13 15:37:28
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
'''

# here put the import lib
def sfun(nums):
    l = len(nums)
    if l==0 or l<=2:
        return False
    tmp = []
    nums.sort()
    for i in nums:
        if len(tmp)==0:
            tmp.append(i)
        elif i == tmp[0]:
            tmp.append(i)
        elif i != tmp[0] and len(tmp)<=l/2:
            tmp = []
            tmp.append(i)
        elif i != tmp[0] and len(tmp)>l/2:
            return tmp[0]
    return tmp[0]   


def ffun(nums):
    l = len(nums)
    if l<=2:
        return nums[0]
    di = {}
    for i in nums:
        if i in di.keys():
            di[i] = di[i]+1
        else:
            di[i] = 1
    for key in di.keys():
        if di[key]>l/2:
            return key


if __name__ == "__main__":
    nums = [3,2,3]
    s = ffun(nums)
    print(s)