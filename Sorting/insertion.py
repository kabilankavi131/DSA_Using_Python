data=[7,6,5,4,3,2,1]
length=len(data)
for i in range(1,length):
    j=i-1
    temp=data[i]
    while(j>=0 and data[j]>temp):
        data[j+1]=data[j]
        j-=1
    data[j+1]=temp
print(data)

# 5 2 3 1 6 8 