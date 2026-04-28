class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}

        max_frequency = left = maxlen = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0) + 1

            max_frequency = max(max_frequency,count[s[right]])

            window_size = right-left +1

            if window_size - max_frequency > k:
                count[s[left]] -= 1

                left += 1

            maxlen = max(maxlen,right-left+1)
        
        return maxlen