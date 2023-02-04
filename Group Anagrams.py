class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)    # (charCount) : [anagrams]    # TS = O(m.n)
        for string in strs:                                          # SC = O(n)  
            key = [0] * 26    # a....z
            for s in string:
                key[ord(s) - ord("a")] += 1
            hashmap[tuple(key)].append(string)
        return hashmap.values()