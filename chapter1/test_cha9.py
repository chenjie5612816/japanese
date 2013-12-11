#    参数列表练习
def hello_1(greeting, name):
    formating = '%s, %s\n'
    print formating %(greeting, name)

def hello_2(greeting, name='zhaochen'):
    formating = '%s, %s\n'
    print formating %(greeting, name)
    
def hello_3(greeting='JING', name='zhaochen'):
    formating = '%s, %s\n'
    print formating %(greeting, name)
    
def hello_4(greeting='JING', name='zhaochen',*param):
    formating = '%s, %s,%s\n'
    print formating %(greeting, name,param)
    
def hello_5(greeting='JING', name='zhaochen',**param):
    formating = '%s, %s, %s\n'
    print formating %(greeting, name,param)

def hello_6(**param):
    formating = ' %s\n'+'='*20
    print formating %(param)
    
def hello_7(greeting='JING', name='zhaochen',nut=''):
    formating = '%s, %s, %s\n'+'-'*10
    print formating %(greeting, name,nut)
    
params={'name':'Zhao','greeting':'Chenjie','nut':'well-off'}
hello_6(**params)

hello_7(**params)

hello_1(name='chenjie', greeting='Love')
hello_2('Love')
hello_2('')
hello_3()
hello_3('DAJING')
hello_4('DAJING','jjjj',1,2,3,4)
hello_4('DAJING','',1,2,3,4)
hello_5('DAJING','vre',hoo=2,pph=4)
#注意  这里的name1 如果改为name将会造成关键字重名，从而系统报错
params1={'name1':'Zhao','greeting1':'Chenjie','nut':'well-off'}
hello_5(greeting='DING', name='Dzhaochen',**params1)