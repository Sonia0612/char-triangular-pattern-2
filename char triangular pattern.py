def range_func(n):
    print("1")
    for i in range(1,n,1):
        for j in range(1,i+2,1):
            if j==1 or i+1==j:
                print(i,end="")
            else:
                print("0",end="")
        print()

def while_func(n):
    print("1")
    i=1
    while i<=n-1:
        #start_char = chr(ord("A") + n - i)
        j=1
        while j<=i+1:
            if j==1 or j==i+1:
                print(i,end="")
            else:
                print("0",end="")
            j=j+1

        i=i+1
        print()
n=int(input())
#while_func(n)
range_func(n)