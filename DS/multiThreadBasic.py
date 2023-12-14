import threading
import time
def run(header):
    time.sleep(2)
    print('当前线程的header是： ', header)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)

# if __name__ == '__main__':

start_time = time.time()

print('这是主线程：', threading.current_thread().name)
thread_list = []
for i in range(5):
    # 这里是创建Thread 实例，传递给他一个函数
    header = i
    t = threading.Thread(target=run, args=(header,))
    thread_list.append(t)

for t in thread_list:
    # 在python中，默认情况下（其实就是setDaemon(False)），主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。
    # 這裡我們把 thread的daemon設成true，這個child thread 就變成守護thread，當main thread結束的時候就終止這個child thread
    # 可能出現的狀況就是child thread還沒有完全執行節結束就被終止
    # t.daemon = True
    t.start()



for t in thread_list:
    # join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止。
    # 对于多线程 Thread 对象的 join(timeout=None) 属性 ，直至启动的线程终止之前一直挂起，除非给出了 timeout(秒) ，否则会一直阻塞
    t.join()

print('主线程结束！' , threading.current_thread().name)
print('一共用时：', time.time()-start_time)