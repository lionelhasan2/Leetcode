class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        currHighestFreq = 0
        res = None
        for num in nums:
            freq[num] += 1 
            if freq[num] > currHighestFreq:
                currHighestFreq = freq[num]
                res = num
        return res

        