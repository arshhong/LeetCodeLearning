
import collections
def bfun(l):
    pass
    dic = collections.Counter(l)
    res_l = []
    tmp_l = []
    for i in l:
        if len(tmp_l)==0:
            tmp_l.append(i)
        elif i>tmp_l[-1]:
            tmp_l.append(i)
        elif i<=tmp_l[-1]:
            if len(res_l)<=len(tmp_l):
                res_l = tmp_l
            tmp_l = []
            tmp_l.append(i)
    
    return res_l

def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary

def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

if __name__ == "__main__":
    l = [3, 1, 3, 9, 4, 5, 6, 9, 1, 2]
    r = bfun(l)
    print(r)

    res = [ 12, 11, 13, 5, 6, 7] 
    print(max_heapify(res,5,12))