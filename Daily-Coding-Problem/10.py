# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


import time

def job_scheduler(f, n):
    time.sleep(n / 1000.0)  # sleep for n milliseconds
    f()  # call the function f after n milliseconds


def say_hello():
    print("Hello, world!")

job_scheduler(say_hello, 1000)  # prints "Hello, world!" after a 1 second delay