#-*- coding:utf-8-*-
class Secretive:
    
    def __inaccess(self):
        print "But you can't"
    def _inaccess1(self):
        print "But you can't1"
    def access(self):
        print 'you can'
        self.__inaccess()
def access():
        print 'you caneee'

s = Secretive()
# s.__inaccess() ������
p = Secretive()
p.access()#
print 'p = ',p#
q = Secretive().access()
print 'q = ',q#
#�󶨷���
meth = s.access
meth()
#
s.meth = access
s.meth()
#
s._Secretive__inaccess()
s._Secretive_inaccess1()
