from threading import Thread
import math


class ChildThread(Thread):
    def __init__(self, num, myfile):
        Thread.__init__(self)
        self.num = num
        self.myfile = myfile

    def run(self):
        for n in range(2, math.ceil(math.sqrt(self.num))):
            if self.num % n == 0:
                print(self.num, "is not a prime number")
                self.myfile.write("{0} is not a prime number\n".format(self.num))
                break
        else:
            print(self.num, "is a prime number")
            self.myfile.write("{0} is a prime number\n".format(self.num))

try:
    with open("prime_nums_out.txt","w") as f:
        nums = [39339393939, 12121212121212121, 2929292929237, 384338215415143, 62449878945613123484813]

        for num in nums:
            t = ChildThread(num,f)
            t.start()
            t.join()

        f.close()

except Exception as ex:
    print("Error:", ex);

