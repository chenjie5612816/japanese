# -*- coding: utf8 -*-
from string import Template
s = Template('$t,goodbye $t')
print s.substitute(t = 'Love')
 
n = Template("It's ${t}meimei")
m = n.substitute(t='jingjing')
print m 

p = Template("Make $$ selling $f")
d = p.substitute(f = 'sweet')
print d

print '%.*s' % (5, 'Guido van')
# print '%*.s' % (5, 'Guido van')
# print '%*.*s' % (5, 'Guido van')

from string import maketrans
table = maketrans('ns','zz')
# print table
Da = table[97:123]
Xiao = table[65:91]
print Da +'\n', \
 Xiao
print 'ewwwe  weewe   weens  eeqwewq  eqw'.translate(table)
print 'ewwwe  weewe   weens  eeqwewq  eqw'.translate(table,' ')

