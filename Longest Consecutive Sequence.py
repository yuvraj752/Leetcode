class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)                      # TC = O(n)
        longest = 0                             # SC = O(n)
        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest,length)
        return longest