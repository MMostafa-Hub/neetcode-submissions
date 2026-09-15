class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        code_to_anagrams = defaultdict(list)
        for string in strs:
            # building code
            chars_counter = [0]*26
            for char in string:
                chars_counter[ord(char) - ord('a')] += 1

            code = tuple(chars_counter)
            code_to_anagrams[code].append(string)
        
        return list(code_to_anagrams.values())
