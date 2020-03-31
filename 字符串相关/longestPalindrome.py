#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py
@Time    :   2020/03/19 16:02:42
@Author  :   LuSu 
@Version :   1.0
@Contact :   lusu@tongbanjie.com
@License :   (C)Copyright 2017-2018, tbj
@Desc    :   给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
'''

# here put the import lib
import collections
def sfun(s):
    s_cnt = collections.Counter(s)
    ans = 0
    flg = 0
    for i in s_cnt:
        ans += s_cnt[i]//2 *2
        if s_cnt[i]%2 == 1 and ans %2 ==0:
            ans+=1
        print(ans,i,flg,s_cnt[i])
    ans = ans + flg
    return ans

if __name__ == "__main__":
    # s = "abccccdd"
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    r = sfun(s)
    print(r)
