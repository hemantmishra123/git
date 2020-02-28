#minimum distance between two number 
def func(arr,x,y):
    m=0
    n=0
    d1=0
    d2=0
    min=99992
    for i in range(len(arr)):
        if(x==arr[i]):
            m=1
            d1=i
            
        if(y==arr[i]):
            d2=i
            n=1
        if(d1>d2 or (not d1==0) and (not d2==0)):
            d=d1-d2
        if(d2<d1):
            d=d2-d1

        if(min>d):
            min=d
    
    if(m==1 and n==1):
        return -1
    else:
        return min

arr=[]
t=int(input())
while(not t==0):
    num=input(" ")
    arr=num.split()
    print('enter the number that distance you want to find')
    x=int(input())
    y=int(input())
    ptr=func(arr,x,y)
    print(ptr)
        
        