class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxwater = 0

        left,right = 0,len(height) - 1
        while left < right:
            maxarea = (right - left)*min(height[left],height[right])

            maxwater = max(maxwater,maxarea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxwater
