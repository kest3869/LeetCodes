class Solution(object):

    def myPow(self, x, n):
        if n>=0 :
            return Pow(1,x,n)
        
    def Pow(key,x,Pow):
        if(Pow>=0):
            key*=x
            a = Pow(key,x,Pow)
            key=a
        return key
