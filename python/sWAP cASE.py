def swap_case(a):
    t=''
    for i in range(0,len(a)):
        if(a[i]>="A" and a[i]<="Z"):
            t+=a[i].lower()
        elif(a[i]>="a" and a[i]<="z"):
            t+=a[i].upper()
        else:
            t+=a[i]

            
    return t

