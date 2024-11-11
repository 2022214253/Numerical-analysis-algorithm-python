class S:
    def __init__(self,intevel,f):
        self.a,self.b=intevel
        self.f=f
    def s(self,a,b):
        #s(a,b)=(h/6)*(self.f(a)+4*self.f((a+b)/2)+self.f(b))
        h=b-a
        return (h/6)*(self.f(a)+4*self.f((a+b)/2)+self.f(b))
    def Sn(self,n,a,b):
        #Sn(n,a,b)=Sn(n-1,a,(a+b)/2)+Sn(n-1,(a+b)/2,b)
        if n==1:
            return self.s(a,b)
        return self.Sn(n-1,a,(a+b)/2)+self.Sn(n-1,(a+b)/2,b)
    def __call__(self,n):
        return self.Sn(n,self.a,self.b)

    
