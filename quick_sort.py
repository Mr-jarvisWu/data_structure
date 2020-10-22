def quick_sort(alist, start , end):
    """快速排序
    最优时间复杂度O(nlogn)
    最坏时间复杂度O(n^2)
    """
    if start >= end:
        return
    mid = alist[start]  # 设置初始值
    # 设置左右两个游标
    left = start
    right = end
    # 判断条件
    while left < right:
        while left < right and alist[right] > mid:
            right -=1
        alist[left] = alist[right]
        while left < right and alist[left] <= mid:
            left += 1
        alist[right] = alist[left]
    # 从循环退出，left == right
    alist[left] = mid
    quick_sort(alist, start, left-1)
    quick_sort(alist, left+1, end)

if __name__ == '__main__':
    alist = [2,5,91,38,45,1,9,0,10]
    print(alist)
    quick_sort(alist, 0, len(alist)-1)
    print(alist)



