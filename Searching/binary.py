data=list(map(int,input("Enter values by comma separated : ").split(",")))
key=int(input("Enter value to be searched : ")) # 1 2 3 4 5 6 
start=0
end=len(data)-1
while start<=end:
    mid=(start+end)//2
    if key==data[mid]:
        print('Value found at position {}'.format(mid))
        break
    elif key<data[mid]:
        end=mid-1
    elif key>data[mid]:
        start=mid+1
    else:
        pass
else:
    print('Value Not Found')