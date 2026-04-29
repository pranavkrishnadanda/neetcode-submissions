class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for i,val in enumerate(numbers):

            temp = target - val

            if temp in seen:

                return [seen[temp]+1,i+1]
            seen[val] = i
        
        return []