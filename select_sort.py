def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(0, n-1):  # 遍历整个列表
        min_index = j    # 将第j个元素看做最小的
        for i in range(j+1, n):  # 从之后的元素中查找最小的元素，看是否比第j个元素小
            if alist[i] < alist[min_index]:
                min_index = i
        if j != min_index:  # 如果最小元素不是本身
            alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == '__main__':
    alist = [2,5,91,38,45,1,9,0,10]
    print(alist)
    select_sort(alist)
    print(alist)