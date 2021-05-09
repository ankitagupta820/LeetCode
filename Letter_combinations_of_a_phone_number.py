class Solution:
    
    result =[]
    
    map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    
    
    def letterCombinations(self, digits: str) -> List[str]:      
        
        if digits == "":
            return []
        
        self.result = []
        self.DFS(digits, "")
        return self.result
    
    
    def DFS(self, digits, substring):
        
        if digits == "":
            self.result.append(substring)
            return
        
        c = int(digits[len(digits)-1])
        chars = self.map[c]
        
        for ch in chars:
            self.DFS(digits[0: len(digits)-1], ch+substring)
