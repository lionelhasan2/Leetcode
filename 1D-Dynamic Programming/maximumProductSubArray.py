class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #[2,3,-2,4]
        min_product,max_product = 1,1
        result = max(nums)
        
        for num in nums:
            if num == 0:
                min_product = 1
                max_product = 1
            prev_max = max_product
            max_product = max(num,num*min_product,num*max_product)
            min_product = min(num,num*prev_max, num*min_product)
            result = max(result,max_product)

        
        return result