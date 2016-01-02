import math
class Solution:
    # @param A : string 
    # @return an integer
    def countOccur(self,count,s):
        for x in s:
            count[ord(x)]+=1
        for i in xrange(256):
            count[i]+=count[i-1]

    def updateCount(self,count,ch):
        for i in xrange(ord(ch),256):
            count[i]-=1

    def findRank(self, A):
        n=len(A)
        f=math.factorial(n)
        count=[0]*256
        self.countOccur(count,A)
        rank=0
        for i in xrange(n):
            f/=n-i
            rank+=count[ord(A[i])-1]*f
            self.updateCount(count,A[i])
        return (rank+1)% 1000003
