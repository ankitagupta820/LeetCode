class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       """
       Brute Force Solution!
       """
        
        def isValid(A:[]):
            bal = 0
            for c in A:
                if c=="(":
                    bal+=1
                else:
                    bal-=1
                if bal<0: return False
            return bal==0
        
        answer=[]
        def generate(A=[]):
            if len(A)==2*n:
                if isValid(A):
                    answer.append("".join(A))
            
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
                
        generate()
        return answer
        
