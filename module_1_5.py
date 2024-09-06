immutable_var = (1, 2, 3, 4, 'Черный пистолет', [1, 2, 3, 4, 5])
print(immutable_var)

#immutable_var[0] = '1'

#Traceback (most recent call last):
#   File "D:\Urban\pythonProject2\module_1_5.py", line 2, in <module>
#     immutable_var[0] = '1'
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 3, 4, 5, 'Братухе подгони на днюху черный пистолет']
print(mutable_list)
mutable_list[0] = 0
print(mutable_list)