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
# threads = []
# for i in range(10):
#     thread = threading.Thread(target=adder)
#     thread.start()
#     threads.append(thread)
# #等待线程退出后主线程再退出
# for thread in threads:
#     thread.join()
# print(count)




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


# import threading,time
# class Helloworld(threading.Thread):
#     count = 0
#     addlock = threading.Lock()
#     def run(self):
#         with Helloworld.addlock:
#             Helloworld.count += 1
#         time.sleep(0.5)
#         with Helloworld.addlock:
#             Helloworld.count += 1
#
# threads = []
# for i in range(5):
#     t = Helloworld()
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
# print(Helloworld.count)





#
# import threading,queue
# import time
# numconsumers = 2   #消费者
# numproducers = 2  #生产者
# nummessages = 4  #消息数量
# lock = threading.Lock()  #定义一个锁
# dataQueue = queue.Queue()   #定义一个队列
#
# def producer(idnum):
#     for msgnum in range(nummessages):
#         dataQueue.put("producer id = %d,count = %id" %(idnum,msgnum))
#
# def consummer(idum):
#     while not  dataQueue.empty(): #列队不为空
#         data = dataQueue.get(block=False)  #非阻塞队列，如果队列中的数没被消费掉，就会阻塞
#         with lock:
#             print("consumer",idum,"got =>",data)
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     consumerThreads = []
#     producerThreads = []
#     for i in range(numproducers):
#         t = threading.Thread(target=producer,args=(i,))
#         producerThreads.append(t)
#         t.start()
#     for i in range(numconsumers):
#         t = threading.Thread(target=consummer,args=(i,))
#         consumerThreads.append(t)
#         t.start()
#     for i in producerThreads:
#         i.join()
#     for i in consumerThreads:
#         i.join()







#
# import threading,queue
# import time
#
# numconsumers = 2
# numproducers = 2
# nummessages = 4
#
# dataQueue = queue.Queue()
#
# class Producer(threading.Thread):
#     def __init__(self,idnum,nummessages):
#         self.idnum = idnum
#         self.nummessages = nummessages
#         super(Producer,self).__init__()
#
#     def run(self):
#         for msgnum in range(self.nummessages):
#             dataQueue.put("producer id = %d ,count = %d" %(self.idnum,msgnum))
#
# class Consummer(threading.Thread):
#     lock = threading.Lock()
#     def __init__(self,idnum):
#         self.idnum = idnum
#         super(Consummer,self).__init__()
#
#     def run(self):
#         while not dataQueue.empty():
#             data = dataQueue.get(block=False)
#             with Consummer.lock:
#                 print("consumer",self.idnum,"got =>",data)
#             time.sleep(0.1)
#
# if __name__ == '__main__':
#     consumerThreads = []
#     producerThreads = []
#     for i in range(numproducers):
#         t = Producer(i,nummessages)
#         producerThreads.append(t)
#         t.start()
#     for i in range(numconsumers):
#         t = Consummer(i)
#         consumerThreads.append(t)
#         t.start()
#     for i in producerThreads:
#         i.join()
#     for t in consumerThreads:
#         t.join()
#

#使用多线程编写一个并发HTTP，get请求的程序，可设置并发数，提交书
#练习代码
# import requests
# import threading,queue
# import time
# start=time.time()
# count=100
# num=2
# url="http://www.baidu.com"
# lock=threading.Lock()
# q=queue.Queue()
# threads=[]
# result={}
# def get_content(url):
#     while not q.empty():
#         q.get(block=False)
#         r=requests.get(url)
#         with lock:
#             try:
#                 result[r.status_code]=result.setdefault(r.status_code,0)+1
#             except:
#                 result["error"]=result.setdefault('error',0)+1
# for i in range(count):
#     q.put(i)
# for i in range(num):
#     t=threading.Thread(target=get_content,args=(url,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# end=time.time()
# t=end-start
# print("time %d"% t)
# for item in result:
#     print("status_code[%s]:%d"%(item,result.get(item)))
#





# import os
#
# from multiprocessing import Process, Lock
#
# def whoami(label, lock):
#     msg = '%s: name:%s, pid:%s'
#     with lock:
#         print(msg % (label, __name__,os.getpid()))
#
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for i in range(5):
#         p = Process(target=whoami, args=('child', lock))
#         p.start()




import time, queue
from multiprocessing import Process, Queue, Lock


# class Consumer(Process):
#     lock = Lock()
#     def __init__(self, id, q):
#         self.id = id
#         self.post = q
#         super(Consumer,self).__init__()
#
#     def run(self):
#         while True:
#             try:
#                 data = self.post.get(block=False)
#             except queue.Empty:
#                 break
#             with Consumer.lock:
#                 print("process id: %d,data:%d" % (self.id, data))
#             time.sleep(0.1)
#
# if __name__ == '__main__':
#     q = Queue()
#     for i in range(10):
#         q.put(i)
#
#     for i in range(2):
#         c = Consumer(i, q)
#         c.start()



# def helloworldid(n):
#     while True:
#         p = yield
#         print("hello world %d : %d"%(n,p))
#
# g1 = helloworldid(1)
# g2 = helloworldid(2)
# g3 = helloworldid(3)
# next(g1)
# next(g2)
# next(g3)
# for i in range(5):
#     g1.send(i)
#     g2.send(i)
#     g3.send(i)



# def addnum(start,end):
#     sum = 0
#     for i in range(start,end):
#         sum += i
#         # print(sum)
#         yield
#     return sum
#
# g1 = addnum(1,51)
# g2 = addnum(51,101)
#
# next(g1)
# next(g2)
#
# for i in range(50):
#     try:
#         g1.send(1)
#     except StopIteration as exc:
#         sum1 = exc.value
#     try:
#         g2.send(1)
#     except StopIteration as exc:
#         sum2 = exc.value
# print(sum1 + sum2)


