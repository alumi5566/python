import random
import threading
import time


class Producer(threading.Thread):
    """
    向列表中生产随机整数
    """

    def __init__(self, integers, event):
        """
        构造器

        @param integers 整数列表
        @param event 事件同步对象
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event

    def run(self):
        """
        实现Thread的run方法。在随机时间向列表中添加一个随机整数
        """
        while True:
            integer = random.randint(0, 256)
            self.integers.append(integer)
            print('%d appended to list by %s' % (integer, self.name))
            time.sleep(10)
            print('event set by %s' % self.name)
            self.event.set()		#设置事件

            time.sleep(10)
            self.event.clear()	#发送事件
            print('event cleared by %s' % self.name)


class Consumer(threading.Thread):
    """
     从列表中消费整数
    """

    def __init__(self, integers, event):
        """
        构造器

        @param integers 整数列表
        @param event 事件同步对象
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event

    def run(self):
        """
        实现Thread的run()方法，从列表中消费整数
        """
        while True:
            print("Consumer wait1")
            self.event.wait()	#等待事件被触发
            print("Consumer wait2")
            try:
                integer = self.integers.pop()
                print('%d popped from list by %s' % (integer, self.name))
            except IndexError:
                print("IndexError")
                # catch pop on empty list
                time.sleep(1)

def main():
    integers = []
    event = threading.Event()
    t1 = Producer(integers, event)
    t2 = Consumer(integers, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()