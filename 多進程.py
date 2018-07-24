import multiprocessing as mp
import os
import time
a = mp.Value('i',0)

def job(a):
    while 1:
        print(a.value,0)
        a.value += 1
        time.sleep(1)

def job2():
    print (a.value,1)

if __name__ == '__main__':
    try:
        p1 = mp.Process(target=job, args=(a,))
        #p2 = mp.Process(target=job, args=(2,))
        p1.start()
        # p2.start()
        while 1:
            print(a.value)
            time.sleep(1)
    except:
        print("END")
