class Solution:
    def trap(self, height: List[int]) -> int:
        
        left,right = 0,len(height) - 1

        leftmax,rightmax = height[left],height[right]

        totalwater = 0

        while left < right:

            if leftmax<rightmax:

                left += 1
                leftmax = max(leftmax,height[left])
                totalwater += leftmax - height[left]
            else:
                right -= 1

                rightmax = max(rightmax,height[right])
                totalwater += rightmax - height[right]
        
        return totalwater