class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}    # num : count                     # TC = O(n)
        array = [[] for i in range(len(nums) + 1)]        # SC = O(n) 
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        for key, value in hashmap.items():
            array[value].append(key)
        result = []
        for reverseIndex in range(len(array) - 1, 0, -1):
            for num in array[reverseIndex]:
                result.append(num)
                if len(result) == k:
                    return result


