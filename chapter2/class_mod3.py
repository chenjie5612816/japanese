class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence\
                if x not in self.blocked]
class ZHAOFilter(Filter):
    def init(self):
        self.blocked ='ZHAO'
        
shili2 = ZHAOFilter()
shili2.init()
shili2.filter(['ZHAO','chen','JIE','ZHAO','chen','ZHAO'])

    