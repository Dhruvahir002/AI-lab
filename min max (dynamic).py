import math

def Fun_Minmax(cd,node,maxt,scr,fd):
    if(cd==fd):
        return(scr[node])
    if(maxt):
        return max(Fun_Minmax(cd+1,node*2,False,scr,fd),Fun_Minmax(cd+1,node*2+1,False,scr,fd))
    else:
        return min(Fun_Minmax(cd+1,node*2,True,scr,fd),Fun_Minmax(cd+1,node*2+1,True,scr,fd))

scr = []
n = int(input("Enter no of leaf nodes: "))
for i in range(n):
    temp = int(input("Enter value: "))
    scr.append(temp)
node = int(input("Enter node value: "))
cd = int(input("Enter current depth: "))
maxt = True
fd = math.log(len(scr),2)
print(Fun_Minmax(cd,node,maxt,scr,fd))