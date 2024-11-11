import numpy as np
import sympy as sp
import pandas as pd
class Tn:
    def __init__(self,intevel,f):
        #intevel为区间，f为被积函数
        self.intevel=intevel
        self.f=f
    def integ(self,inteval:np.ndarray):
        #将子区间的数量进行一次扩展
        length=inteval.size
        inteval1=[]
        for i in range(length-1):
            inteval1.append((inteval[i+1]+inteval[i])/2)
        res=[]
        for x,y in zip(inteval,inteval1):
            res.extend([x,y])
        res.append(inteval[-1])
        return np.array(res)
    def tn(self,n):
        #将区间的数量进行n次扩展，使其符合计算Tn的区间的数量要求
        inteval=self.total_integ(n)
        if n==1:
            return 0.5*self.f(inteval).sum()
        inteval1=self.integ(inteval)
        #计算h的大小
        h=(inteval1[1]-inteval1[0])*2
        indice=np.where(np.arange(inteval1.size)%2==1)[0]
        selece_inteval=inteval1[indice]
        #进行递推公式
        return 0.5*self.tn(n-1)+h*np.sum(self.f(selece_inteval))*0.5
    def total_integ(self,n):
        #将区间的数量进行n次扩展
        p=np.array(self.intevel)
        for i in range(n-1):
            p=self.integ(p)
        return p
    def __call__(self,n):
        return self.tn(int(np.log2(n)+1))

class speed:
    def __init__(self,intevel:np.ndarray,f):
        self.f=f
        self.intevel=intevel
        self.b_a=intevel[-1]-intevel[0]
    def Tm(self,m,n):
        #m为加速的次数，n为Tn的下标，例如1，2，4，8，16，32.。。。。。
        h=self.b_a/n
        #计算h
        if m==0:
            return Tn(self.intevel,self.f)(n)
        #进行递推公式
        return (4**m)/(4**m-1)*self.Tm(m-1,n*2)-1/(4**m-1)*self.Tm(m-1,n)
