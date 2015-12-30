class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        a=float('inf')
        b=float('inf')
        B=[1]*len(A)
        for i in xrange(0,len(A)):
            if B[abs(A[i])-1]<0:
                a=A[i]
            else:
                B[abs(A[i])-1]=B[abs(A[i])-1]*(-1)

        for i in xrange(0,len(A)):
            if B[i]>0:
                b=i+1
                break
        return a,b

