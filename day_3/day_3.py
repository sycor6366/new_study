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


import threading
import time

count = 0
def adder():
    global count
    count = count + 1
    time.sleep(0.5)
    count = count + 1

threads = []
for i in range(10):
    thread = threading.Thread(target=adder)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
