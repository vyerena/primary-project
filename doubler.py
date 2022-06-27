def func(a,b):
    x = a * b
    return x
x = func(5, 2)
print (x)

if not type (x) is int:
	raise TypeError("only function allowed")
