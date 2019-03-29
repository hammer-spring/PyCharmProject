import _thread, time

class threadClass:

    def __init__(self):
        self._threadFunc = {}
        self._threadFunc['1'] = self.threadFunc1
        self._threadFunc['2'] = self.threadFunc2
        self._threadFunc['3'] = self.threadFunc3
        self._threadFunc['4'] = self.threadFunc4

    def threadFunc(self, selection, seconds):
        self._threadFunc[selection] (seconds)

    def threadFunc1(self, seconds):
        _thread.start_new_thread(self.output, (seconds, 1))

    def threadFunc2(self, seconds):
        _thread.start_new_thread(self.output, (seconds, 2))

    def threadFunc3(self, seconds):
       _thread.start_new_thread(self.output, (seconds, 3))

    def threadFunc4(self, seconds):
        _thread.start_new_thread(self.output, (seconds, 4))

    def output(self, seconds, number):
        for i in range(seconds):
            time.sleep(0.0001)
        print ("No. %d is recorded" % number)

mythread = threadClass()

mythread.threadFunc('1', 700)
mythread.threadFunc('2', 700)
mythread.threadFunc('3', 500)
mythread.threadFunc('4', 300)

time.sleep(5.0)
