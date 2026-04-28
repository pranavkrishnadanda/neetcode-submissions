class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s: return ""
        target = Counter(t)

        have =left = 0
        need = len(target)
        res = float('inf'),0,0
        window = {}

        for right in range(len(s)):

            window[s[right]] = window.get(s[right],0 ) + 1

            if s[right] in target and window[s[right]] == target[s[right]]:
                have += 1
            
            while have == need:

                if right-left + 1 < res[0]:
                    res = (right-left+1,left,right)
                
                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        min_len,l,r = res
        return s[l:r+1] if min_len<float('inf') else ''