def func(x):
    return x.isalnum()

def func1(x,y):
    return x+y
seq =["foo","x41","?1","**"]
seq1 =['foo',"x41","?1","**"]

print filter(func, seq1)

print filter(lambda x: x.isalnum(), seq1)

print [x for x in seq if x.isalnum()]

number=[1,2,3,4,5,6,7,8,9,10]
print reduce(lambda x,y: x+y,number)
print reduce(func1,number)