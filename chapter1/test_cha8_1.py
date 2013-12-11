def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] ={}

def lookup(data, lable, name):
    return data[lable].get(name)

def store(data, full_name):
    names = full_name.split()
    if(len(names) == 2):
        names.insert(1,'')
    lables = ['first', 'middle', 'last']
    for lable, name in zip(lables, names):
        people = lookup(data, lable, name)
        if people:
            people.append(full_name)
        else:
            data[lable][name] = [full_name]

MyName ={}
init(MyName)
store(MyName, 'Robin Hood')
store(MyName, 'Robin Lockal')
store(MyName, 'Robin view Lockal')
print "lookup the first argument::" , lookup(MyName, 'first', 'Robin')
print 'lookup the middle argument is empty::' , lookup(MyName, 'middle', '')
print 'lookup the last argument::' , lookup(MyName, 'last', 'Hood')
