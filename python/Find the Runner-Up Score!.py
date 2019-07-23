if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr=sorted(arr)
    for i in range(n-1,-1,-1):
        if(arr[i]!=arr[i-1]):
            print(arr[i-1])
            break
