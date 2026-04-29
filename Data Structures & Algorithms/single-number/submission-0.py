class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums_freq = Counter(nums)

        return nums_freq.most_common()[-1][0]