def square(x):
    return x*x
def pass_func(func,x):
    sq=func(x)
    return sq
num=10
print(pass_func(square,num)) # Passing function as a argument 