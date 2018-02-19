from threading import Thread


class PrintThread(Thread):  # extend 'Thread' classs
    def run(self):  # override 'run' method
        for n in range(1, 11):
            print(n)




t1 = PrintThread()  # create object
t2 = PrintThread()
t1.start()  # call 'start' method. This invokes 'run' method.
t2.start()
