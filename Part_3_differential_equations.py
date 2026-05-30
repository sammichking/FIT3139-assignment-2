import matplotlib.pyplot as plt


xvals=[]
tvals=[]
yvals=[]
avals=[]


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
time=1

alpha=1
beta=1

xdiff0=(r/(1+v*y0))*x0-a*x0*y0-d*x0*a0
ydiff0=s*y0-b*x0*y0-e*y0*a0
adiff0=u*a0-c*a0*x0

#Lets do Heun Method

def findmX(t):
    if xmemo[t] != -1:
        return xmemo[t]
    else:
    ## set up dynamic programming
        xmemo[t]=differX(t-1,findmX(t-1))+time*(1/2*(differX(t-1,findmX(t-1))+1/2*(differX(t-1+alpha*time,findmX(t-1)+beta*time*(differX(t-1,findmX(t-1)))))))
        return xmemo[t]
    #differX(1/2(di))

def findmY(t):
    if ymemo[t] != -1:
        return ymemo[t]
    else:
    ## set up dynamic programming
        ymemo[t]=differY(t-1,findmY(t-1))+time*(1/2*(differY(t-1,findmY(t-1))+1/2*(differY(t-1+alpha*time,findmY(t-1)+beta*time*(differY(t-1,findmY(t-1)))))))
        return ymemo[t]
def findmA(t):
    if amemo[t] != -1:
        return amemo[t]
    else:
    ## set up dynamic programming
        amemo[t]=differA(t-1,findmA(t-1))+time*(1/2*(differA(t-1,findmA(t-1))+1/2*(differA(t-1+alpha*time,findmA(t-1)+beta*time*(differA(t-1,findmA(t-1)))))))
        return amemo[t]


def differX(t,x):
    if xdiffmemo[t] != -1:
        return xdiffmemo[t]
    else:
        xdiffmemo[t]=(r/(1+v*findmY(t)))*x-a*x*findmY(t)-d*x*findmA(t)
    #just return the output of the function
    return xdiffmemo[t]

def differY(t,y):
    if ydiffmemo[t] != -1:
        return ydiffmemo[t]
    else:
        ydiffmemo[t]=s*y-b*findmX(t)*y-e*y*findmA(t)
    #just return the output of the function
    return ydiffmemo[t]

def differA(t,A):
    if adiffmemo[t] != -1:
        return adiffmemo[t]
    else:
        adiffmemo[t]=u*A-c*A*findmX(t)
    #just return the output of the function
    return adiffmemo[t]

#x=x(t-1) + deltaT*(1/2* (differX(findX,findY,findX)) + 1/2*differX(find)    )

n=100

xmemo=[]
xmemo.append(x0)
ymemo=[]
ymemo.append(y0)
amemo=[]
amemo.append(a0)

xdiffmemo=[]
xdiffmemo.append(xdiff0)
ydiffmemo=[]
ydiffmemo.append(ydiff0)
adiffmemo=[]
adiffmemo.append(adiff0)

for i in range(1,n):
    xmemo.append(-1)

for i in range(1,n):
    ymemo.append(-1)

for i in range(1,n):
    amemo.append(-1)

for i in range(1,n):
    xdiffmemo.append(-1)

for i in range(1,n):
    ydiffmemo.append(-1)

for i in range(1,n):
    adiffmemo.append(-1)



for i in range(0,n):
    tvals.append(i)


for i in range(0,n):
    #print("nth x val: ",findx(i)[0]," nth y val: ",findy(i)[0]," nth dx: ",findx(i)[1]," nth dy: ",findy(i)[1])
    xvals.append((findmX(i)))
    
    yvals.append((findmY(i)))
    
    avals.append((findmA(i)))

x_line=plt.plot(tvals,xvals)
y_line=plt.plot(tvals,yvals)
a_line=plt.plot(tvals,avals)
plt.xlabel("t")
plt.ylabel("Population")
plt.legend(["fish","sharks","algae"])
plt.title("3")
#plt.plot(tvals,dxvals)
#plt.plot(tvals,dyvals)
#plt.plot(tvals,davals)
plt.show()
