import math
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, num):
        negFlag=False
        if num <0:
            negFlag=True
        num=abs(num)
        digits = int(math.log10(num))+1
        ret=0
        j=0
        for i in xrange(digits-1,-1,-1):
            base=10**i
            ret+=(num/base)*(10**j)
            if ret > 2147483647:
                return 0
            j+=1
            num=num%base
        
        if negFlag:
            return -1*ret
        return ret
