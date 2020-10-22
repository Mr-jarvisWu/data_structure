def insert_sort(alist):
    """插入排序
    最优时间复杂度O(n)
    最坏时间复杂度O(n^2)
    稳定排序
    """
    n = len(alist)
    for j in range(0, n):
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break

if __name__ == '__main__':
    alist = [2,5,91,38,45,1,9,0,10]
    print(alist)
    insert_sort(alist)
    print(alist)