class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter

        code_to_anagrams = defaultdict(list)
        for string in strs:
            code_to_anagrams[str(sorted(string))].append(string)
        
        return list(code_to_anagrams.values())
            
