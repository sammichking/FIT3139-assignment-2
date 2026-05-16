x0=10
y0=15
a0=10
r=0.8
s=-0.8
a=0.045
b=0.03
c=0.05765
d=0.000001
e=0.0001
u=0.13127809
v=5
n=100000
time=0.005


#Lets do Heun Method

def findmX(t):
    return 1

def findmY(t):
    return 1

def findmA(t):
    return 1


def differX(t):
    #just return the output of the function
    return (r/(1+v*findmY(t-1)))*findmX(t-1)-a*findmX(t-1)*findmY(t-1)-d*findmX(t-1)*findmZ(t-1)

def differY(t):
    #just return the output of the function
    return s*findmY(t-1)-b*findmY(t-1)*findmX(t-1)-e*findmY(t-1)*findmZ(t-1)

def differA(t):
    #just return the output of the function
    return r*findmA(t-1)-a*findmX(t-1)*findmY(t-1)-d*findmX(t-1)*findmZ(t-1)

#x(t)=x(t-1) + deltaT*(1/2* (differX(findX,findY,findX)) + 1/2*differX(find)    )