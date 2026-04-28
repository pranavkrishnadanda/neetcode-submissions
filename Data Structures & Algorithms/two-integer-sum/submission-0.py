class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return 