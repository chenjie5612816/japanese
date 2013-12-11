#-*- coding:utf-8-*-
#copy 第2个函数
x = {'username' : 'admin', 'machine': ['foo','zuu','baz']}
y = x.copy()
y['username'] = 'llll' #副本中的值改变后不影响原字典
y['machine'].remove('zuu')
print y ,'\n',x
#深度复制
from copy import deepcopy
d={}
d['name'] = ['Alfred','Bertrand']
c = d.copy()
dc =deepcopy(d) #深度复制
d['name'].append('zhao')
print dc , d

#更新的方法
d={
   'title' : 'I love you',
   'url'   : 'http://www.python.org',
   'change':'Mar 12 22 22:09 ' 
   }
print d
x = {'title':'You ?'}
d.update(x)
print d