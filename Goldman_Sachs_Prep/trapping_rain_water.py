class Solution: # two pointer solution, keeping track of leftmax and rightmax
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]
        ret = 0

        while left < right:

            if leftMax <= rightMax:

                left += 1
                ret += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
            else:

                right -= 1
                ret += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])

        return ret
