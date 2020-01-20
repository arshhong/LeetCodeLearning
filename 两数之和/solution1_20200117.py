#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   solution_20200117.py
@Time    :   2020/01/17 10:40:41
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   通过效率 执行用时1620ms, 内存消耗13.8M
'''

# here put the import lib


class Solution:
    def towSum(self, nums, target):
        lens = len(nums)
        rlist = []
        for i in range(lens):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if i !=j and i not in rlist and j not in rlist:
                    rlist.append(i)
                    rlist.append(j)
        return rlist
            

if __name__ == "__main__":
    s = Solution()
    nums = [-1,-2,-3,-4,-5]
    target = -8
    r = s.towSum(nums, target)
    print(r)