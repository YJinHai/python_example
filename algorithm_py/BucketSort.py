"""
题目：假设我们现在需要对 D，a，F，B，c，A，z 这个字符串进行排序，要求将其中所有小写字母都排在大写字母的前面，
    但小写字母内部和大写字母内部不要求有序。比如经过排序之后为 a，c，z，D，F，B，A，这个如何来实现呢？
思路：桶排序，按照ASCII码分为三个桶
"""


def bucket_sort(a):
    a1 = ''
    a2 = ''
    a3 = ''
    for i in a:
        if 48 <= ord(i) <= 57:
            a1 += i
        elif 65 <= ord(i) <= 90:
            a2 += i
        elif 97 <= ord(i) <= 122:
            a3 += i
    print(a1)
    return a1 + a3+ a2


s = 'DaF123BcAz'
print(bucket_sort(s))

