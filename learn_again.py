a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
import os
print(n, f, s1, s2, s3, s4)
print('this process %s' %(os.getpid()))
g = ( x*x for x in range(10))

print(next(g))
 
from multiprocessing import Process


def run_proc(name):
	print('Run chlid process %s (%s)...' %(name, os.getpid()))
	
	
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance is %s' %balance)

#子进程不执行main内容
if __name__ == '__main__':
	print('Parent process %s' %(os.getpid()))
	p = Process(target = run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')