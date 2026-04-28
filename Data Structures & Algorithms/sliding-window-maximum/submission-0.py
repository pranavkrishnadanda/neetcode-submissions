class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = []

        l.append(max(nums[:k]))

        for i in range(k,len(nums)):
            l.append(max(nums[i-k+1:i+1]))
        
        return l