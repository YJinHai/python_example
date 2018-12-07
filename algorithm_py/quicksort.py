class QuickSort:
    def quick_sort(self, a):
        self._quick_sort_between(a, 0, len(a) - 1)

    def _quick_sort_between(self, a, l, h):
        if l >= h:
            return

        m = self._partition(a, l, h)
        self._quick_sort_between(a, l, m - 1)
        self._quick_sort_between(a, m + 1, h)

    def _partition(self, a, l, h):
        k = a[l]
        i, j = l, h
        while i != j:
            while i < j and a[j] >= k:
                j -= 1
            while i < j and a[i] <= k:
                i += 1
            if i < j:
                a[i], a[j] = a[j], a[i]
            print(a)
        a[l] = a[i]
        a[i] = k
        return i


a = [6, 1, 2, 5, 9, 4, 7, 10, 8]
quick_sort = QuickSort()
quick_sort.quick_sort(a)
print(a)
"""
图解链接：https://blog.csdn.net/adusts/article/details/80882649
"""
