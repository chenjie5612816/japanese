#-*- coding:utf-8-*-
#clear ��һ������
d={}
d['name'] = 'Gao'
d['age'] = 42
print d
print '=' * 10
#
y = d
print y
#way1 �� way2 ֻ��һ�ַ�ʽ�������У�����clear�������ԭʼ�ֵ������Ԫ��
x = {}
print y
#way2
#     d.clear() #   x = {}   print y
#     print y 
#
print d.clear()
