class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        main=[]
        for i in xrange(A):
            inside=[]
            if i==0:
                inside.append(1)
            elif i==1:
                inside.append(1)
                inside.append(1)
            else:
                temp=main[i-1]
                inside.append(1)
                for i in xrange(1,len(temp)):
                    inside.append(temp[i]+temp[i-1])
                inside.append(1)
            main.append(inside)
        return main