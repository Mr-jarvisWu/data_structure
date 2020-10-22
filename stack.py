"""
栈的实现
"""
class Stack(object):
    def __init__(self):
        self.__items = [] # 构造一个顺序表容器
        # self.items = Single_link_list() 构造一个链表容器

    def push(self, item):
        """添加一个元素到栈顶"""
        self.__items.append(item)  # O(1)
        # self.items.insert(0, item)  # O(n)

    def pop(self):
        """从栈顶弹出元素"""
        self.__items.pop()  # O(1)
        # self.items.pop(0)     # O(n)

    def peek(self):
        """返回栈顶元素"""
        return self.__items[-1]

    def is_empty(self):
        """判断是否为空"""
        return self.__items == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__items)