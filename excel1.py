class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        st="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n=len(A)
        sum1=0
        i=n-1
        for x in A:
            sum1+=(st.index(x)+1)*(26**i)
            i-=1
        return sum1