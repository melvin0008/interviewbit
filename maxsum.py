class Solution:
    # @param A : tuple of integers 0 0
    # @return an integer
    def maxSubArray(self, A):
        n=len(A)
        dpArray=[0]*n
        flag=True
        for i in A:
            if i >= 0:
                flag=False
        if flag:
            return max(A)
        if dpArray[0]>0:
            dpArray[0]=A[0]
        else:
            dpArray[0]=0
        for i in xrange(1,len(A)):
            if (dpArray[i-1]+A[i])>0:
                dpArray[i]=dpArray[i-1]+A[i]
            else:
                dpArray[i]=0

        return max(dpArray)