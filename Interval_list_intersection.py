class Solution:
    
    def getWindow(self, l1:[], l2: []):
        return [max(l1[0], l2[0]), min(l1[1], l2[1])]
    
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i1, i2 = 0,0
        result = []
        
        while i1 < len(firstList) and i2 < len(secondList):
            
            if firstList[i1][1] < secondList[i2][0]:
                i1+=1
            elif secondList[i2][1] < firstList[i1][0]:
                i2+=1
            else:
                result.append(self.getWindow(firstList[i1], secondList[i2]))
                if firstList[i1][1] >= secondList[i2][1]:
                    i2+=1
                else:
                    i1+=1
                
                
        return result
