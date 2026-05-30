import matplotlib.pyplot as plt



#Check out my sweet dynamic programming...
#nice to have algo complexity stuff be useful instead of just be stuff to ROTE learn



xvals=[]
tvals=[]
yvals=[]
avals=[]

dxvals=[]
dyvals=[]
davals=[]


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
v=0.13127809
n=10000
time=0.005

print(x0,"\n",y0,"\n",a0,"\n",r,"\n",s,"\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",u,"\n",v,"\n",time)

#Let's do simpler find the nth term of series thing

def findx(t):
    if xmemo[t] != -1:
        return (xmemo[t])
    else:
        xmemo[t] = (findx((t-1))+time*((r/(1+v*findy(t-1)))*findx((t-1))-a*findx(t-1)*findy(t-1)-d*finda(t-1)*findx(t-1)))
        return xmemo[t]
        #return ((r+1)*findx((t-1))[0]-a*findx(t-1)[0]*findy(t-1)[0],(r+1)*findx((t-1))[0]-a*findx(t-1)[0]*findy(t-1)[0]-findx(t-1)[0])
    
def findy(t):
    if ymemo[t] != -1:
        return ymemo[t]
    else:
        ymemo[t] = findy(t-1)+time*((s)*findy(t-1)+b*findy(t-1)*findx(t-1)-e*finda(t-1)*findy(t-1))
        return ymemo[t]
        #return ((s+1)*findy(t-1)[0]+b*findy(t-1)[0]*findx(t-1)[0],((s+1)*findy(t-1)[0]+b*findy(t-1)[0]*findx(t-1)[0]-findy(t-1)[0]))

def finda(t):
    if amemo[t] != -1:
        if amemo[t] < 0:
            return 0
        return amemo[t]
    else:
        amemo[t] = finda(t-1)+time*(u*finda(t-1)-c*findx(t-1))
        if amemo[t] < 0:
            amemo[t]=0
        return amemo[t]




###
# 
# THESE ONES ARE FOR IF YOU WANT TO CALCULATE DIFFERENCES INSTEAD OF THE VALUES THEMSELVES
# 
# ###
def findDx(t):
    
    if dxmemo[t] != -1:
        return dxmemo[t]
    dxmemo[t] = dxmemo[t] - findDx(t-1)
    return dxmemo[t]
    
    
def findDy(t):
    
    if dymemo[t] != -1:
        return dymemo[t]
    dymemo[t] = dymemo[t] - findDy(t-1)
    return dymemo[t]

def findDa(t):
    
    if damemo[t] != -1:
        return damemo[t]
    damemo[t] = damemo[t] - findDa(t-1)
    return damemo[t]






xmemo=[]
xmemo.append(x0)
ymemo=[]
ymemo.append(y0)
amemo=[]
amemo.append(a0)
dxmemo=[]
dxmemo.append(0)
dymemo=[]
dymemo.append(0)
damemo=[]
damemo.append(0)


for i in range(1,n):
    xmemo.append(-1)

for i in range(1,n):
    ymemo.append(-1)

for i in range(1,n):
    amemo.append(-1)

for i in range(1,n):
    dxmemo.append(-1)

for i in range(1,n):
    dymemo.append(-1)

for i in range(1,n):
    damemo.append(-1)



for i in range(0,n):
    tvals.append(i)



for i in range(0,n):
    #print("nth x val: ",findx(i)[0]," nth y val: ",findy(i)[0]," nth dx: ",findx(i)[1]," nth dy: ",findy(i)[1])
    xvals.append((findx(i)))
    
    yvals.append((findy(i)))
    
    avals.append((finda(i)))
    dxvals.append(findDx(i))
    dyvals.append(findDy(i))
    davals.append(findDa(i))

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




