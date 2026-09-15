class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        code_to_anagrams = defaultdict(list)
        for string in strs:
            code_to_anagrams[''.join(sorted(string))].append(string)
        
        return list(code_to_anagrams.values())
