from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    print(*a,sep='',end='\n')

