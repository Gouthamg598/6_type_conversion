'''name:goutham
date:13-05-1998
file discription:type coversion and casting
'''
from unicodedata import name


a=3
# print(float(a))#3.0
# print('%f' %a)#3.000000
# print(str(a))
# print('%s'%a)
b=4.78
# print(type(b))
# print(float(b))
# print(int(b))
# print('%f'%b)
# print('%.1f'%b)
# print('%s'%b)

# c='python'
# print(int(c))#ValueError: invalid literal for int() with base 10: 'python'
# print(float(c))#ValueError: invalid literal for int() with base 10: 'python'
# d='8'
# print(int(d))#8
# print(float(d))#8.0
# # print('%d'%d)#TypeError: %d format used for integer: a real number is required, not str
# # print('%f'%d)#TypeError: %f format used for float: must be real number, not str, not str
# print('%s'%d)

# e='6.9'
# print(int(e))#ValueError: invalid literal for int() with base 10: '6.9'
'''direct conversion of float character string into integer is not possible.
first we need convert into float then into integer
'''
# f=float(e)
# print(int(f))
# print('my name is goutham and my qualification is M.Tech ')

name='goutham'
qualification='M.Tech'
age=24
percentage=88.88

# print('my name is ',name, 'qualification',qualification)
# print('age:',age,'and percentage is',str(percentage),'%')
# print('my age is '+str(age)+' percentage is '+str(percentage)+'%')
# print('my name is',name ,'qualification is',qualification)
# print('my name is %s.qualification %s'%(name,qualification))#my name is goutham qualification M.Tech
# print('age:%d and percentage is %.2f.%'%(age,percentage))#ValueError: incomplete format
print('age:%d and percentage is %.2f.'%(age,percentage))#age:24 and percentage is 88.88 here notgetting % symbol