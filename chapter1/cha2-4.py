# -*- coding: utf8 -*-
#检查用户名和Pin码
dataOne = ['albrt', '1234']
dataTwo = ['dilbert','4224']
dataThree = ['zhaochenjie', '8080']
dataFourth = ['niujingjing', '80']

dataBase = [dataOne,dataTwo,dataThree,dataFourth]

username = raw_input('Please input your name:')
pin = raw_input('PIN code')

if[username, pin] in dataBase:
    print 'Access grant'
else:
    print 'You input donnot exit, Please zhuce'