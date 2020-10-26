class Note:
    """结点类"""
    def __init__(self, item):
        self.item = item
        self.left_child = None # 左子结点
        self.right_child = None # 又子结点


class BinaryTree:
    def __init__(self, note=None):  # 初始化根结点
        self.root = note

    def add(self, item):   # 增加结点
        """
        广度优先遍历的方式添加结点，使用队列，先进先出
        :param item:
        :return:
        """
        queue = []
        if self.root is None:
            self.root = Note(item)
        else:
            queue.append(self.root)
            while queue:
                note = queue.pop(0)
                if note.left_child is None:
                    note.left_child = Note(item)
                    return
                else:
                    queue.append(note.left_child)
                if note.right_child is None:
                    note.right_child = Note(item)
                    return
                else:
                    queue.append(note.right_child)

    def breadth_traversal(self):  # 遍历结点
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            note = queue.pop(0)
            print(note.item, end=' ')
            if note.left_child:
                queue.append(note.left_child)
            if note.right_child:
                queue.append(note.right_child)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.breadth_traversal()


