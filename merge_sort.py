def merge_sort(alist):
    """归并排序
    归并排序不改变原列表"""
    n = len(alist)
    if n == 1:
        return alist
    mid = n // 2  # 将列表分为两个部分
    left_sorted_li = merge_sort(alist[:mid])  # 对左半部分进行归并排序
    right_sorted_li = merge_sort(alist[mid:])  # 对右半部分进行归并排序

    # 合并两个有序集合
    left, right = 0, 0
    merge_sort_li = []   # 将合并后的列表生成一个新列表

    left_n = len(left_sorted_li)
    right_n = len(right_sorted_li)

    while left < left_n and right < right_n:
        if left_sorted_li[left] <= right_sorted_li[right]:
            merge_sort_li.append(left_sorted_li[left])
            left += 1
        else:
            merge_sort_li.append(right_sorted_li[right])
            right += 1
    # 当有一边所有元素全部添加到新列表时
    merge_sort_li += left_sorted_li[left:]
    merge_sort_li += right_sorted_li[right:]

    return merge_sort_li

if __name__ == '__main__':
    alist = [2,5,91,38,45,1,9,0,10]
    print(alist)
    print(merge_sort(alist))
    print(alist)

