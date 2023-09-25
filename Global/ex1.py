def func():
    global a,b
    a+=2
    b+=5
a,b=10,15
func()
print(a,b)