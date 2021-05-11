class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         Two sum inside target set by 3rd number.
        n = len(nums)
        nums.sort()
        res= []
        for i in range(n-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
                
            l,r =i+1, n-1
            target = -nums[i]
            while l<r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]: l+=1
                
                elif nums[l] + nums[r] > target:
                    r-=1
                
                else:
                    l+=1
        return res
        
