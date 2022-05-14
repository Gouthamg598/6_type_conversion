# 6_type_conversion
conversion of int and float to string is possible but string to int and float not possible we get value error
# integer
conversion of integer to string is possible<br>
Ex:<br>
a=6<br>
print(str(a)) #3<br>
# float
conversion of float to string<br>
Ex:<br>
print(str(5.8)) #5.8
# '''direct conversion of 'float value' inside the string into integer is not possible.first we need convert into float then into integer'''
Ex:<br>
e='6.9'<br>
print(int(e))#ValueError: invalid literal for int() with base 10: '6.9'<br>
f=float(e)<br>
print(f)#6.9<br>
print(int(f))#6

