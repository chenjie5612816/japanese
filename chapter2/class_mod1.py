__metaclass__ = type

class Cla:
    def med(self):
        print 'i don'

def function():
        print 'ddd'
        
instance = Cla()
print '-'*20
instance.med()
print '*'*20
instance.med = function
instance.med()
# instance.med() = function()
print '='*20
function()
        