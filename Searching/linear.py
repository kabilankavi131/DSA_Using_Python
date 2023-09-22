data=input("enter the values as comma separated : ").split(",")
flag=0
key=input("Enter value to be searched : ")
for i in range(len(data)):
    if data[i]==key:
        flag=1
        print("Value found at position : {key}".format(key=i))
if flag==0:
    print("Value Not Found !")