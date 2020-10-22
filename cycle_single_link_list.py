class Note(object):
    """节点类"""
    def __init__(self, item):
        self.item = item  # 节点的对象
        self.next = None  # 下一个节点


class CycleSingleLinkList(object):
    """单向循环链表"""
    def __init__(self, note=None):  # 设置节点默认值为None
        self.__head = note  # 设置头结点为私有属性

    def is_empty(self):
        """是否为空
        :return 如果链表为空，则返回True,否则返回False
        """
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head  # 引入一个游标，用来标记note当前的位置
        count = 1 # 计算链表的长度
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty(): # 如果链表为空
            print('')
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def add(self, item):  # item要保存的具体数据
        """链表头部添加元素"""
        note = Note(item)  # 构造一个节点对象实例
        if self.is_empty():
            self.__head = note
            note.next = note
        # 找到尾节点
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        note.next = self.__head
        self.__head = note
        cur.next = note

    def insert(self, site, item):  # 指定添加元素的位置
        """链表中间添加元素"""
        if site <= 0:  # 在头部添加元素
            self.add(item)
        elif site >= self.length():  # 在尾部添加元素
            self.append(item)
        else:  # 在中间添加元素
            note = Note(item)
            cur = self.__head
            count = 0
            while count < site - 1:  # 当链表长度小于位置的时候
                count += 1
                cur = cur.next
            note.next = cur.next
            cur.next = note

    def append(self, item):
        """链表尾部添加元素"""
        # 如果链表为空，需要重新设置
        note = Note(item)  # 生成新的节点
        if self.is_empty():
            self.__head = note
            note.next = note
        else:  # 如果链表不为空
            cur = self.__head  # 设置游标
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环的时候，cur.next指向尾节点
            cur.next = note
            note.next = self.__head

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None  # cur的前一个游标
        while cur.next != self.__head:
            # 找到了要删除的元素
            if cur.item == item:
                # 在头部找到了要删除的元素
                if self.__head == cur:
                    # 找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                # 在中间找到了要删除的元素
                else:
                    pre.next = cur.next
                return
            # 不是要找的元素，移动游标
            pre = cur
            cur = cur.next
        # 退出循环，对尾节点进行处理
        if cur.item == item:
            # 如果链表只有一个节点
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        """查找某个节点是否存在"""
        # 判空
        if self.is_empty():
            return False
        # 如果不为空
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        # 处理尾节点
        if cur.item == item:
            return True
        return False

if __name__ == '__main__':
    ll = CycleSingleLinkList()
    print(ll.length())
    ll.travel()

    ll.add(1)
    ll.travel()  # 1

    ll.append(3)
    ll.travel()  # 1,3

    ll.insert(1, 5)
    ll.travel()   # 1,5,3
    ll.insert(0, 9)
    ll.travel()  # 9,1,5,3
    ll.insert(20,10)
    ll.travel() # 9,1,5,3,10

    ll.remove(9)
    ll.travel() # 1,5,3,10
    ll.remove(10)
    ll.travel()  #  # 1,5,3
    ll.remove(5)
    ll.travel()  # 1,3
    ll.remove(0)
    ll.travel()  # 1,3
    ll.remove(3)
    ll.travel()

    print(ll.search(3))
    print(ll.search(9))
'''
0

1 
1 3 
1 5 3 
9 1 5 3 
9 1 5 3 10 
1 5 3 10 
1 5 3 
1 3 
1 3 
True
False
'''