# class Record:
#     global_id = 0
#
#     def __init__(self, name, phone_number):
#         self.name  = name
#         self.phone_number = phone_number
#         Record.global_id += 1
#         self.record_id = Record.global_id
#
#     def set_number(self, phone_number):
#         self.phone_number = phone_number
#
#     def __str__(self):
#         return "{}\t{}\t{}".format(self.record_id, self.name , self.phone_number)
#         # return 'hello world'
#
# r1 = Record("贾敏强", "15801396646")
# print(r1.record_id)
# print(r1.name )
# print(r1.phone_number)
# print(r1)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# if __name__ == '__main__':
#     print(factorial(5))


# def test():
#     return test()
# if __name__ == '__main__':
#     test()

# def power(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x,n - 1)
# if __name__ == '__main__':
#     print(power(2,6))
# L = [1,2, [3,4,[5,6],7],8]
# isinstance(L,list)
# for i in L:
#     print(i)


# # 递归
# def test(n):
#     for i in n:
#         if isinstance(i,list) == False:
#             print(i)
#         else:
#             test(i)
#
#
# if __name__ == '__main__':
#     L = [1, 2, [3, 4, [5, 6], 7], 8]
#     test(L)

#闭包
# def npower():
#     n = 2
#     def power(x):
#         return x ** n
#     return power
#
# if __name__ == '__main__':
#     f = npower()
#     print(f(2))
#     print(f(3))
#     print(f.__closure__)
#     print(f.__closure__[0])
#     print(f.__closure__[0].cell_contents)



# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner
#
# # @deco
# def target():
#     print('running target()')
#
# if __name__ == '__main__':
#     target = deco(target)
#     target()



# import time
# def decorator(aa):
#     def wrapper():
#         start_time = time.time()
#         aa()
#         end_time = time.time()
#         print(end_time - start_time)
#     return wrapper
#
# @decorator
# def func():
#     print('hello,world')
#     time.sleep(1)
#
# func()


# def add_decorator(f):
#     print('加法')
#     return f
# @add_decorator
# def add_method(a,b):
#     return print(a+b)
#
# add_method(1,2)


# def out_f(arg):
#     print("out_f" + arg)
#     def decorator(func):
#         def inner():
#             func()
#         return inner
#     return decorator
#
# decorator = out_f('123')
# @decorator
# # @out_f("123")
# def func():
#     print('hello world')
#
# func()



#迭代器
# l = [1,2,3]
# b = l.__iter__()
# print(type(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


#迭代器
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __next__(self):
#         self.a,self.b = self.b, self.a +self.b
#         return self.a
#     def __iter__(self):
#         return self
#
# fibs = Fibs()
# for f in fibs:
#     if f > 1000:
#         print(f)
#         break

# def fibs(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a,  b = b, a + b
#         print(a,b)
#
# fibs(10)

#生成器，可用next方法调用，也可循环
# L = [[1,2],[3,4],[5,]]
# def flat(L):
#     for sublist in L:
#         for e in sublist:
#             yield e  #yield接受并返回，暂停循环,接受到next方法继续
# for num in flat(L):
#     print(num)
#
# f = flat(L)
# print(next(f))
# print(next(f))


#生成器send方法
# def gen():
#     for i in range(10):
#         x = (yield i)
#         print(x)
#
# g = gen()
# next(g)
# print(g.send(11))
# print(g.send(12))



#生成器表达式

# f = (x ** 2 for x in range(4))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

#os模块

import os
# print(os.getcwd())  #返回当前目录
# print(os.listdir()) #列出目录的内容
# os.mkdir('test')  #创建目录
# os.rmdir('test')  #删除空目录
# os.rename('1.py','2.py')  #重命名
# os.remove('2.py')  #删除文件
# os.system('dir')  #执行系统命令
# os._exit()  #退出程序
#os.walk() #遍历目录中的所有文件 os.walk 返回一个3元组生成器 当前目录的名称，当前目录中子目录的列表，当前目录中文件的列表
# g = os.walk('D:\project\\new_study\day2')
# print(next(g))
# print(next(g))






# abspath() 将相对路径转化为绝对路径 os.path.abspath(path)
# print(os.path.abspath('day2_test.py'))
# # dirname() 获取完整路径当中的目录部分 os.path.dirname("d:/1/test")
# print(os.path.dirname("D:\project\\new_study\day2\day2_test.py"))
# # basename()获取完整路径当中的主体部分 os.path.basename("d:/1/test")
# print(os.path.basename("D:\project\\new_study\day2"))
# # split() 将一个完整的路径切割成目录部分和主体部分 os.path.split("d:/1/test")
# print(os.path.split("D:\project\\new_study\day2"))
# # join() 将2个路径合并成一个 os.path.join("d:/1", "test")
# print(os.path.join("D:\project\\new_study\day2"),'\day2_test.py')
# # getsize() 获取文件的大小 os.path.getsize(path)
# print(os.path.getsize('D:\project\\new_study\day2\day2_test.py'))
# # isfile() 检测是否是文件 os.path.isfile(path)
# print(os.path.isfile('D:\project\\new_study\day2'))
# print(os.path.isfile('D:\project\\new_study\day2\day2_test.py'))
# # isdir() 检测是否是文件夹 os.path.isdir(path)
# print(os.path.isdir('D:\project\\new_study\day2'))
# print(os.path.isdir('D:\project\\new_study\day2\day2_test.py'))

# import os
#



# for dirpath, dirames, filenames  in os.walk("D:\project\\new_study\day2"):
#     print('[' + dirpath + ']')
#     for filename in filenames:
#         a = os.path.join(dirpath, filename)
#         print(a)



# def listfile(dir):
#     for file in os.listdir(dir):
#         path = os.path.join(dir,file)
#         if not os.path.isdir(path):
#             print(os.path.getsize(path),os.path.basename(path))
#         else:
#             listfile(path)
# listfile(dir = 'D:\project\\new_study\day2')


# max_size = 0
# for dir_path, dir_names, file_names in os.walk(r'D:\project\\new_study\day2'):
#     for file_name in file_names:
#         path = os.path.join(dir_path, file_name)
#         file_size = os.path.getsize(path)
#         if file_size > max_size:
#             max_size = file_size
#             max_file = path
#
# print(max_file, max_size)



# for dirpath, dirames, filenames  in os.walk("D:\project\\new_study\day2"):
#     # print(dirpath)
#     # print(dirames)
#     for dirame in dirames:
#         print(os.path.join(dirpath, dirame))
#     # print(filenames)
#     # print('[' + dirpath + ']')
#     for filename in filenames:
#         a = os.path.join(dirpath, filename)
#         # print(a)
#         # print(os.path.isfile(a))
#         # print(os.path.isdir(a))


# print(os.listdir())

s = '中文'
print(bytes(s,encoding='UTF-8'))
ss = '中文一'
print(ss.encode())
ss1 = ss.encode()
print(ss1.decode())




