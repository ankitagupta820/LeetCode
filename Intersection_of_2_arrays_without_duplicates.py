class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        i1, i2 = 0, 0
        nums1.sort()
        nums2.sort()
        result = []
        
        while i1< len(nums1) and i2 < len(nums2):
            
            if nums1[i1] > nums2[i2]:
                i2+=1
            elif nums1[i1] < nums2[i2]:
                i1+=1
            else:
                if len(result) == 0 or result[-1] < nums1[i1]:
                    result.append(nums1[i1])
                i1+=1
                i2+=1
                
                
        return result
