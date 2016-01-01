class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count=0
        for x in xrange(5,A+1,5):
            while(x%5==0):
                count+=1
                x/=5
        return count