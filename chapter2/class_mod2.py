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
# s.__inaccess() 不可用
p = Secretive()
p.access()#
print 'p = ',p#
q = Secretive().access()
print 'q = ',q#
#绑定方法
meth = s.access
meth()
#
s.meth = access
s.meth()
#
s._Secretive__inaccess()
s._Secretive_inaccess1()
