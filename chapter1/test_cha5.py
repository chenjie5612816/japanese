# -*- coding:utf-8 -*-
#男孩女孩匹配的问题
girls = ['alice','bernamr','clarice']
boys  = ['chris','arnold','bob']
letterGirls = {}

for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
for b in boys:
    a = letterGirls[b[0]]
    for g in a :
        print [b+'+'+g  ]
