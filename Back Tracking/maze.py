def count(r,c):
    if r==1 or c==1:
        return 1
    else:
        left=count(r-1,c)
        right=count(r,c-1)
    return left+right
print(count(3,3))