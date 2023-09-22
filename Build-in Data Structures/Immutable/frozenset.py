# It is Similar to sets, but frozen sets are immutable. Once created, you cannot change their content.
x=frozenset([1,2,3,3])
# x.add(5) It will cause the error as ===> AttributeError: 'frozenset' object has no attribute 'add's
print(x)