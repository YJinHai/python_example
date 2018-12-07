class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = Node(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def get_palindrome(self):
        prev = None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            # 保存链表前部分倒序
            slow_next = slow.next
            # 头插法
            slow.next = prev
            prev = slow
            slow = slow_next

        # 判断元素奇偶数量
        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.data != prev.data:
                return False
            slow, prev = slow.next, prev.next

        return True


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.head = None


    def init_list(self, data):
        self.head = DNode(data[0])

        p = self.head

        for i in data[1:]:
            node = DNode(i)
            p.next = node
            node.prev = p
            p = p.next

        self.head.prev = p

    def get_palindrome(self):
        head = self.head
        tail = self.head.prev
        while tail is not self.head:
            if head.data != tail.data:
                return False
            head,tail = head.next, tail.prev

        return True



if __name__ == '__main__':

    s = 'non'
    # 单向链表实现
    link = LinkList()
    link.init_list(s)
    print(link.get_palindrome())
    # 双向链表实现
    link = DoubleLinkList()
    link.init_list(s)
    print(link.get_palindrome())
