class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # print len(A)
        n=len(A)
        if max(A)<=0:
            return 1
        j=0
        for i in xrange(len(A)):
            if A[i]<=0:
                A[i],A[j]=A[j],A[i]
                j+=1
        for x in xrange(j,n):
            if abs(A[x]) <=n-j :
                A[abs(A[x])+j-1]*=(-1)
        for i in xrange(j,n):
            if A[i]>0:
                return i+1-j
        return n-j+1