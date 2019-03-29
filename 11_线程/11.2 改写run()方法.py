import threading, time, random

class threadClass(threading.Thread):
    def run(self):
        x = 0
        y = random.randint(1, 100)
        while x < y:
            x += 1
            time.sleep(0.0001)
        print (y)

for i in range(25):
    mythread = threadClass()
    mythread.start()
print ("End of excution")
