if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first=-101
    second=-101
    for i in range(n):
        if(arr[i]>first):
            second=first
            first=arr[i]
        if(arr[i]>second and arr[i] != first):
            second=arr[i]
    
    print(second)
