class Solution:
    
    maxcount=0
    count=0
    ele=None
        
    def driver(self, root: TreeNode, res: List[int]):
        if(root==None):
            return
        self.driver(root.left, res)
        if(self.ele==None):
            self.ele=root.val
            self.count=1
        else:
            if(root.val==self.ele):
                self.count+=1
            else:
                
                if(self.count>=self.maxcount):
                    if(self.count>self.maxcount): #clear res when count >maxcount. If count==maxcount, only append res with ele
                        res.clear()
                    res.append(self.ele)
                    self.maxcount=self.count
                
                self.ele=root.val
                self.count=1
                
        self.driver(root.right, res)
        
        return 
    
        
    def findMode(self, root: TreeNode) -> List[int]:
        
        res=[]
        
        self.driver(root, res)
        if(self.count>=self.maxcount):
            if(self.count>self.maxcount):
                res.clear()
            res.append(self.ele)
         
        return res
