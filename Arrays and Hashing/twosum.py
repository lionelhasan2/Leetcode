class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i,n in enumerate(nums):
            complement = target - n
            if dictionary.get(complement) is not None:
                return [i,dictionary.get(complement)]
            else: 
                dictionary[n] = i

                
