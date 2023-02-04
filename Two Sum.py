class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # value : index               # TC = O(n)
        for index, value in enumerate(nums):        # SC = O(n)
            diff = target - value
            if diff in hashmap:
                return [index, hashmap[diff]]
            else:
                hashmap[value] = index