#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   卡牌分组.py
@Time    :   2020/03/27 16:04:57
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib

def bfun(nums):
    import collections
    from fractions import gcd
    from functools import reduce
    vals = collections.Counter(nums).values()
    return reduce(gcd, vals) >= 2

if __name__ == "__main__":
    # nums = [1,2,3,4,4,3,2,1]
    nums = [1,1,2,2,2,2]
    res = bfun(nums)
    print(res)
    print(5//2)