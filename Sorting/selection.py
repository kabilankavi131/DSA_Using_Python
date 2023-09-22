data=list(map(int,input("Enter values by comma separated : ").split(",")))
print('Before sorted : ',data)
length=len(data)
for i in range(length):
    swap=0
    for j in range(i+1,length):
        if data[i]>data[j]:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
            swap=1
    if swap==0:
        break
print('After sorted : ',data)