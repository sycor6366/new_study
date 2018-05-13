# import threading
# import time
# def helloworld():
#     time.sleep(2)
#     print('helloworld')
#
# t = threading.Thread(target=helloworld)
# t.start()
# print('main thread')


# import threading
# import time
# def helloworld(id):
#     time.sleep(2)
#     print("thread %d helloworldid" % id)
#
# for i in range(5):
#     t = threading.Thread(target=helloworld,args=(i,))
#     t.start()
# print("main thread")


# import threading
# import time
# #共享变量需要加锁
# count = 0
# def adder():
#     global count
#     count = count + 1
#     time.sleep(0.5)
#     count = count + 1
#
# threads = []
# for i in range(10):
#     thread = threading.Thread(target=adder)
#     thread.start()
#     threads.append(thread)
#
# #等待线程退出后主线程再退出
# for thread in threads:
#     thread.join()
#
# print(count)
# print(threads)



# import  threading,time
# count = 0
# #同一时间只有一个线程对变量进行访问
# def adder(addlock):
#     global count
#     addlock.acquire()#申请锁
#     count = count + 1
#     addlock.release()#释放锁
#     time.sleep(0.1)
#     addlock.acquire()
#     count = count + 1
#     addlock.release()
# addlock = threading.Lock() #互斥锁
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
# #等线程退出完后，主线程再退出
# for thread in threads:
#     thread.join()
#
# print(count)






# import threading,time
# count = 0
# def adder (addlock):
#     global count
#     with addlock:
#         count = count + 1
#     time.sleep(0.1)
#     with addlock:
#         count = count + 1
#
# addlock = threading.Lock()
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# print(count)





# import threading,time
# class Helloworld(threading.Thread):
#     def run(self):
#         time.sleep(2)
#         print("helloworld")
#
#
# t = Helloworld()
# t.start()
# print("main thread")


# import  threading,time
# class Helloworld(threading.Thread):
#     def __init__(self,id):
#         self.id = id
#         super(Helloworld,self).__init__()
#     def run(self):
#         time.sleep(2)
#         print("thread %d helloworld" % self.id)
#
# for i in  range(5):
#     t = Helloworld(i)
#     t.start()
#
# print("main thread")




# import threading,time
# class Helloworld(threading.Thread):
#     count = 0
#     def run(self):
#         Helloworld.count += 1
#         time.sleep(0.5)
#         Helloworld.count += 1
# threads = []
# for i in range(5):
#     t = Helloworld()
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
#
# print(Helloworld.count)


import threading,time
class Helloworld(threading.Thread):
    count = 0
    addlock = threading.Lock()
    def run(self):
        with Helloworld.addlock:
            Helloworld.count += 1
        with Helloworld.addlock:
            Helloworld.count += 1

threads = []
for i in range(5):
    t = Helloworld()
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(Helloworld.count)











