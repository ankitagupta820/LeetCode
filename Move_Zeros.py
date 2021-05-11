class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        r,w = 0, 0
        
        while r < len(nums):
            
            if nums[r] != 0:
                nums[w] = nums[r]
                w+=1
                
            r+=1
        
        while w < len(nums):
            nums[w]=0
            w+=1
