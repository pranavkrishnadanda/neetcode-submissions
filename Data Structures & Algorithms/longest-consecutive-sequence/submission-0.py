class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <1: 
            return 0
        nums.sort()

        res = streak = i = 0
        current = nums[0]
        while i < len(nums):

            if nums[i] != current:
                current = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == current:
                i+= 1
            streak += 1
            current += 1
            res = max(res,streak)
        return res