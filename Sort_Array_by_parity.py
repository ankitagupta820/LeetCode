class Solution:
    
    """
    Used skip-skip-action
    """
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        l,r =0, len(A)-1
        
        while(l<r):
            
            if A[l]%2 == 0:
                l+=1
            elif A[r]%2 == 1:
                r-=1
            else:
                A[l], A[r] = A[r], A[l]
                l+=1
                r-=1
                
        return A
