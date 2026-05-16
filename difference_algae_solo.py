import matplotlib.pyplot as plt

x0=10
y0=15
r=0.8
s=-0.8
a=0.045
b=0.03
c=0.05
d=0.001
u=0.13127809


#Let's do simpler find the nth term of series thing

def findx(t):
    if xmemo[t] != -1:
        return (xmemo[t])
    else:
        xmemo[t] = findx((t-1))+0.05*((r)*findx((t-1))-a*findx(t-1)*findy(t-1)-d*finda(t-1))
        return xmemo[t]
        #return ((r+1)*findx((t-1))[0]-a*findx(t-1)[0]*findy(t-1)[0],(r+1)*findx((t-1))[0]-a*findx(t-1)[0]*findy(t-1)[0]-findx(t-1)[0])
    
def findy(t):
    if ymemo[t] != -1:
        return ymemo[t]
    else:
        ymemo[t] = findy(t-1)+0.05*((s)*findy(t-1)+b*findy(t-1)*findx(t-1)-d*finda(t-1))
        return ymemo[t]
        #return ((s+1)*findy(t-1)[0]+b*findy(t-1)[0]*findx(t-1)[0],((s+1)*findy(t-1)[0]+b*findy(t-1)[0]*findx(t-1)[0]-findy(t-1)[0]))

def finda(t):
    if amemo[t] != -1:
        return amemo[t]
    else:
        amemo[t] = finda(t-1)+0.05*(u*finda(t-1)-c*findx(t-1))
        return amemo[t]


xvals=[]
tvals=[]
yvals=[]
avals=[]
dxvals=[]
dyvals=[]


n=1000

xmemo=[]
xmemo.append(10)
ymemo=[]
ymemo.append(15)
amemo=[]
amemo.append(10)

for i in range(1,n):
    xmemo.append(-1)

for i in range(1,n):
    ymemo.append(-1)

for i in range(1,n):
    amemo.append(-1)

for i in range(0,n):
    tvals.append(i)



for i in range(0,n):
    #print("nth x val: ",findx(i)[0]," nth y val: ",findy(i)[0]," nth dx: ",findx(i)[1]," nth dy: ",findy(i)[1])
    xvals.append((findx(i)))
    yvals.append((findy(i)))
    avals.append((finda(i)))

plt.plot(tvals,xvals)
plt.plot(tvals,yvals)
plt.plot(tvals,avals)
plt.show()




