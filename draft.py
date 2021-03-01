# def f(one, name, color):
#     """一个小函数"""
#     one["name"] = name
#     one["color"] = color
#     return one


# one = {"name": "Alice", "color": "red"}
# name = input("Please input the name:")
# color = input("Please input the color:")
# two = f(one, name, color)
# print("%s\n%s" % (one, two))

# n=int(input())
# for i in range(n):
#     print("*****")

'''函数 传递任意数量的键值对实参
def func(fname, lname, **info):
    profile = {}
    profile['first_name'] = fname
    profile['last_name'] = lname
    for key, value in info.items():
        profile[key] = value
    return profile


info = {'location': 'China', 'field': 'robotics'}
# user_profile = func('Jerry', 'Gao', **info)
# user_profile = func('Jerry', 'Gao', locaition='China',field='Robotics')
print(user_profile)
print(user_profile['location'])
'''
'''
class Dog():
    def __init__(self, name, age):#类属性的初始化
        self.name = name
        self.age = age
    def sit(self):
        print(self.name+' is sitting!')

mydog=Dog('Alice',6)
mydog.sit()
a=[1,2,3]
# print(a[0])
b={'name':'Alice','age':18}
# print(b['name'])
# print(a[2])
c=(1,2,3)
'''
'''文件
with open('pi.txt') as file_obj:
    # for line in file_obj:
    #     print(line.rstrip())
    lines=file_obj.readlines()

pi_str=''
for line in lines:
    pi_str+=line.rstrip()
# print(pi_str)

import json

filename='numbers.json'
numbers=[2,3,5,7,11,13]
with open(filename,'w') as file_obj:
    json.dump(numbers,file_obj)
'''

# unittest 笔记
'''
def get_formatted_name(first, last, middle=''):
    name = ''
    if middle:
        name = first+' '+middle+' '+last
    else:
        name = first+' '+last
    name = name.title()
    return name


class NameTestCase(unittest.TestCase):
    """测试get_formatted_name 函数"""

    def test_name(self):
        formatted_name = get_formatted_name('jerry', 'gao')
        self.assertEqual(formatted_name, 'Jerry Gao')

    def test_middle_name(self):
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
'''

import unittest

unittest.main()
