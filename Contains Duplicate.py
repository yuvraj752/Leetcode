class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()                    # TC = O(n)                 
        for value in nums:                 # SC = O(n)
            if value in hashset:
                return True
            else:
                hashset.add(value)
        return False