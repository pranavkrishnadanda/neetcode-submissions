class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
    
        for word in strs:
            # Sort the word and use it as a key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())