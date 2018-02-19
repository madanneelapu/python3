from threading import Thread,current_thread,active_count
import math


class ChildThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        print("In Thread",self.getName()) # print thread name
        self.num = num

    def run(self):
        for n in range(2, math.ceil(math.sqrt(self.num))):
            if self.num % n == 0:
                print(self.num, "is not a prime number")
                break
        else:
            print(self.num, "is a prime number")


nums = [39339393939, 12121212121212121, 2929292929237, 384338215415143, 62449878945613123484813]

print("In Thread",current_thread().getName()) # print thread name

for num in nums:
    t = ChildThread(num)
    t.start()
    print("No.of active threads",active_count()) # display active threads count
