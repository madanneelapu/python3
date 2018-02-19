from threading import Thread


class SumThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        total = 0
        for n in range(1, self.num + 1):
            total += n

        print("Sum of ", self.num, "is", total)


t1 = SumThread(1212121)
t1.start()
