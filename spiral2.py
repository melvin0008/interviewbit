class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        a=[[0 for x in xrange(A)] for y in xrange(A)]
        # a=[[0,0],[0,0]]
        k=1
        l=0
        b=A-1
        r=A-1
        t=0
        while(t<b and l<r):
            for i in xrange(l,r):
                a[t][i]=k
                k+=1
                # print k
            for i in xrange(t,b):
                a[i][r]=k
                k+=1
                # print k

            for i in xrange(r,l,-1):
                a[b][i]=k
                k+=1
            for i in xrange(b,t,-1):
                a[i][l]=k
                k+=1
            t+=1
            b-=1
            l+=1
            r-=1
        if t==b:
            a[t][t]=k
        return a