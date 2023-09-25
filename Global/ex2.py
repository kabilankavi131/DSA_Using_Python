def func():
    global a,b
    a+=2
    b+=5
    c.append(35)
a,b,c=10,15,[]
func()
print(a,b,c)