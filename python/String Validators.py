if __name__ == '__main__':
    s = input()
    a=False
    b=False
    c=False
    d=False
    e=False
    for i in range(0,len(s)):
        if(s[i].isalnum()):
            a=True
        if(s[i].isalpha()):
            b=True
        if(s[i].isdigit()):
            c=True
        if(s[i].islower()):
            d=True
        if(s[i].isupper()):
            e=True
    if(a):
        print("True")
    else:
        print("False")
    if(b):
        print("True")
    else:
        print("False")
    if(c):
        print("True")
    else:
        print("False")
    if(d):
        print("True")
    else:
        print("False")
    if(e):
        print("True")
    else:
        print("False")
    
