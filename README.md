# use-promise-like-thread-in-python

### For using a Thread's output into a variable use following guideline.

from promise import Promise

Declare your thread with a sub class Promise as this:

promise_1 = Promise(target=myFunc, args=(10,20))

It automatically starts the thread. If you want the result in main thread, just using Thread's join() method as this:

promise_1_result = promise_1.join()


