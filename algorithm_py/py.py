class LNode:
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = LNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            LNode = LNode(i)
            p.next = LNode
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

        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.data is not prev.data:
                return False
            slow, prev = slow.next, prev.next

        return True



if __name__ == '__main__':
    s = 'non'
    link = LinkList()
    link.init_list(s)
    print(link.get_palindrome())
