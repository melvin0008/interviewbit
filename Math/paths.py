class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def cachefun(self,A,B,cache):
        if A==1 or B==1:
            return 1
        if (A,B) in cache:
            return cache[(A,B)]
        l=self.cachefun(A-1,B,cache)
        cache[(A-1,B)]=l
        r=self.cachefun(A,B-1,cache)
        cache[(A,B-1)]=r
        return l+r
    
    def uniquePaths(self, A, B):
        return self.cachefun(A,B,{})
        
