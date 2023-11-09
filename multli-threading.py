from time import sleep
from promise import Promise


def myFunc(p1, p2):
    sleep(3)
    return p1+p2;



promise_1 = Promise(target=myFunc, args=(10,20))
promise_2 = Promise(target=myFunc, args=(10,-20))
promise_1.start()
promise_2.start()
promise_1_result = promise_1.join()
promise_2_result = promise_2.join()

print(promise_1.join() + promise_2.join());


