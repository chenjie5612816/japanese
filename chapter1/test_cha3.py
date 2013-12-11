#-*- coding:utf-8-*-
#clear 第一个函数
d={}
d['name'] = 'Gao'
d['age'] = 42
print d
print '=' * 10
#
y = d
print y
#way1 和 way2 只有一种方式可以运行，看看clear真正清空原始字典的所有元素
x = {}
print y
#way2
#     d.clear() #   x = {}   print y
#     print y 
#
print d.clear()
