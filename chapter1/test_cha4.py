#-*- coding:utf-8-*-
#copy ��2������
x = {'username' : 'admin', 'machine': ['foo','zuu','baz']}
y = x.copy()
y['username'] = 'llll' #�����е�ֵ�ı��Ӱ��ԭ�ֵ�
y['machine'].remove('zuu')
print y ,'\n',x
#��ȸ���
from copy import deepcopy
d={}
d['name'] = ['Alfred','Bertrand']
c = d.copy()
dc =deepcopy(d) #��ȸ���
d['name'].append('zhao')
print dc , d

#���µķ���
d={
   'title' : 'I love you',
   'url'   : 'http://www.python.org',
   'change':'Mar 12 22 22:09 ' 
   }
print d
x = {'title':'You ?'}
d.update(x)
print d