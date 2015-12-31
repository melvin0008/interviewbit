import math
class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        n=int(math.sqrt(2147483647))-1
        for i in xrange(1,n):
            for j in xrange(2,32):
                if math.pow(i,j)>2147483647:
                    break
                if math.pow(i,j)==A:
                    return True
        return False