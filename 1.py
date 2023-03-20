import numpy
S0=[1,0]
S1=[0,1]

M1=[[-(3/5),0],[0,-(4/5)]]
print(M1)

print((M1[0][0]**2+M1[1][1]**2))
print("P(0)=")
print(numpy.inner(numpy.inner(M1,S0),numpy.inner(M1,S0)))
print("P(1)=")
print(numpy.inner(numpy.inner(M1,S1),numpy.inner(M1,S1)))