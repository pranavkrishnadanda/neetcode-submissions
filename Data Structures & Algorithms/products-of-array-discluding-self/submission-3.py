class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = len(nums)
        result = [1]*k
        prefix = 1
        for i in range(k):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(k-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result