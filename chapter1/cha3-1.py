# -*- coding:utf-8 -*-
#格式化字符串
width = input('Please enter width')
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format        = '%-*s%*.2f'

print '=' * width
print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format % (item_width, 'Apple', price_width, 0.4)
print format % (item_width, 'Pear', price_width, 0.5)
print format % (item_width, 'Cantaloupes', price_width, 1.4)
print format % (item_width, 'Prunes', price_width, 3.4)
print format % (item_width, 'Dried', price_width, 6.4)

print '=' * width
