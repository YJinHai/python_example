"""
查找第一个值等于给定值的元素
"""


def binary_search(a, v):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] > v:
            high = mid - 1
        elif a[mid] < v:
            low = mid + 1
        else:
            if mid == 0 or (a[mid - 1]) != v:
                return mid
            else:
                high = mid - 1

    return

"""
leetcode:33. 搜索旋转排序数组
"""
# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if nums is None:
#             return None
#         low, high = 0, len(nums) - 1
#
#         while low <= high:
#             mid = low + ((high - low) >> 1)
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < nums[high]:
#                 if nums[mid] < target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             else:
#                 if nums[low] <= target < nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#
#         return -1


"""
leetcode:81. 搜索旋转排序数组 II
参照文章：https://www.cnblogs.com/ariel-dreamland/p/9159124.html
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return None
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] > nums [low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target == nums[high]:
                    return high
                high -= 1

        return -1

a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
search = Solution()
print(binary_search(a, 10))
print(search.search([1,1,3,1], 3))
print(search.search([3, 5, 1], 3))
print(search.search([1,3,1, 1,1], 3))
print(search.search([3,1], 1))

