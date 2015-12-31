from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, y):
        st="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    	q=deque([])
    	while(y):
    	    r=y%26
    	    if r==0:
    	        q.appendleft('Z')
    	        y=(y/26)-1
    	    else:
    	        q.appendleft(st[r-1])
    	        y=y/26
    	return "".join(q)