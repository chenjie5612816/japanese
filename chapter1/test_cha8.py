storage = {}
storage['first'] = {}
storage['middle']={}
storage['last'] ={}

me = 'Magnus xxxx uuuuu'
storage['first']['Magnus'] = [me]
storage['middle']['xxxx'] = [me]
storage['last']['uuuuu'] = [me]
print storage['middle']['xxxx']

my_sister = 'Anne xxxx uuuuu'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('xxxx', []).append(my_sister)
storage['last'].setdefault('uuuuu', []).append(my_sister)

print storage['first']['Anne']
print storage['middle']['xxxx']
