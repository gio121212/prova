import math


a= math.log(1)
print(a)
b= int(a)
print(b)

c=r'Hello \n world'
d='\nHello\nworld'
print(c,d)

str='Palla'
s = str.strip('P')
s1 = str.replace ('a','e')
print(s, s1)
print(str.isupper())
str1 = str.upper()
print(str1.isupper())
str2 = str1.center(10, '.')
print(str2)
x= str.rfind('LLA')
y= str.find('lla')
print(x,y)