class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        a=map(str,A)
        a.sort(lambda a,b : cmp(b+a, a+b))
        k=''.join(a).lstrip('0')
        if k:
            return k
        return 0