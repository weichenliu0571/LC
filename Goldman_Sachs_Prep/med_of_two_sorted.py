class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2

        a = nums1
        b = nums2

        if len(a) > len(b):
            a, b = b, a

        left = 0
        right = len(a) - 1

        while True:
            index1 = (left + right) // 2
            index2 = half - index1 - 2

            topLeft = float("-infinity") if index1 < 0 else a[index1]
            topRight = float("infinity") if index1 + 1 > len(a) - 1 else a[index1 + 1]

            botLeft = float("-infinity") if index2 < 0 else b[index2]
            botRight = float("infinity") if index2 + 1 > len(b) - 1 else b[index2 + 1]

            if topLeft <= botRight and botLeft <= topRight:

                if total % 2:
                    return min(topRight, botRight)
                else:
                    return (max(topLeft, botLeft) + min(topRight, botRight)) / 2

            if topLeft > botRight:
                right = index1 - 1
            else:
                left = index1 + 1







