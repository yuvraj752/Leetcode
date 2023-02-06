class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)                # TC = O(n)
        prefix = 1                              # SC = O(n)
        postfix = 1
        for index in range(len(nums)):
            result[index] = prefix
            prefix *= nums[index]
        for reverseIndex in range(len(nums) - 1, -1, -1):
            result[reverseIndex] *= postfix
            postfix *= nums[reverseIndex]
        return result     

