if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
s=[]
c=0
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            t=''
            c=i+j+k
            if(c!=n):
                t+='['+str(i)+', '+str(j)+', '+str(k)+']'
                s.append(t)
l=str(s)
l=l.replace("'","")    
print(l)               
