m,n= map(int,input().split()) 
arr=list(map(int,input().split())) 
for _ in range(m):
    l,r=map(int,input().split()) 
    if(arr[l-1]>=arr[r-1]):
        print("Yes")
        print(arr[l-1]>=arr[r-1])
    else:
        print("No")

