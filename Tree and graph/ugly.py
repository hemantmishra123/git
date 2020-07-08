#Funcion code for the programme
def func(count,i,flag,counter):
    stack=[2,3,5]
    print(stack)
    print(counter)

    val=stack[counter]
    print(val)
    q=int(count/val)
    r=count%val
    if(q!=1 or r!=0):
        val=stack[counter]
        q=int(count/val)
        r=count%val
        if(r==0):
            func(q,i,flag,counter)
        else:
            flag+=1
            counter+=1
            func(q*val+r,i,flag,counter)
    else:
        if(flag==3):
            return 0
        else:
            return 1
def fib(N):
    count=1
    i=1
    seen=1
    while(i<=N):
        result=func(count,i,0,0)
        if(seen==result):
            i+=1
        count+=1
    print(i)
    return count
t=int(input())
for i in range(1,t+1):
    N=int(input())
    result=fib(N)
    print(result)

        
    
    
            
            
        
        
        
        
        
        