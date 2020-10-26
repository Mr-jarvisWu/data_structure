def binary_search(alist, item):
    """
    二分查找递归版本实现
    """
    n = len(alist)
    if 0 == n:
        return False
    mid = n//2
    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return binary_search(alist[:mid], item)
    else:
        return binary_search(alist[mid+1:], item)


def binary_search2(alist, item):
    """
    二分查找非递归版本实现
    :param alist:
    :param item:
    :return:
    """
    start = 0
    end = len(alist) - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return False



if __name__ == '__main__':
    testlist = [1,3,4,5,6,9,13,24,56,78,91]
    print(binary_search(testlist, 5))
    print(binary_search(testlist, 12))
    print(binary_search2(testlist, 5))
    print(binary_search2(testlist, 12))