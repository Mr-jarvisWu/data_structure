def bubble_sort(alist):
    """冒泡排序"""
    """冒泡排序是稳定性排序"""
    n = len(alist)
    for i in range(0, n-1):  # 循环n-1遍 i [0,1,2...n-2]
        count = 0
        for j in range(0, n-i-1): # 每次循环都少走一步
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]  # 交换位置
                count += 1
        if count == 0:   # 最优时间复杂度
            break


if __name__ == '__main__':
    alist = [2,5,91,38,45,1,9,0,10]
    print(alist)
    bubble_sort(alist)
    print(alist)