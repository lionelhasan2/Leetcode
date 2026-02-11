class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        valid = 0 
        directions = [-1,1] # left , right
        for i,num in enumerate(nums):
            # Found Curr position
            if num == 0:
                # Initial direction for this run, try right
                for direction in directions:
                    curr = i 
                    copy = nums[:]
                    while(curr >= 0 and curr < len(copy)):
                        if copy[curr] == 0:
                            curr += direction
                        else:
                            copy[curr] -= 1
                            # Reverse direction
                            direction *= -1
                            curr += direction
                    # Check if all elements are zero
                    if all(x == 0 for x in copy):
                        valid += 1
        return valid                    
                        
                


                
            

                
