#!/usr/bin/env python

"""
Example to demonstrate multiple threads interaction
- Hmm, what happens when lock is not acquired?

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""

import threading
import time


class SplitPrintThread(threading.Thread):

    """
    Prints individual words of the message
    """

    def __init__(self, name, msg, lock):
        """
        :param name: Name of the thread
        :param msg: Message to be sliced and printed
        """
        super(SplitPrintThread, self).__init__(name=name)
        self.__msg = msg.split(' ')
        self.__lock = lock

    def run(self):
        #if self.__lock.acquire(1):
        if self.__lock.acquire(0):
            try:
                for word in self.__msg:
                    print("%s: %s" % (self.name, word))
                    time.sleep(0)
            finally:
                self.__lock.release()
        else:
            try:
                import sys
                import os
                sys.path.insert(0, os.path.dirname(__file__))
                import black_box
                black_box.cleanup()
            except Exception as details:
                print("Fail to cleanup: %s" % details)


def say(no_threads, msg):
    """
    Spawns $no_workers to print the message
    :param no_threads: How many threads to spawn
    :param msg: Message to be printed
    """
    lock = threading.Lock()
    threads = [SplitPrintThread("worker%s" % i, msg, lock)
               for i in range(no_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    say(3, "Welcome to the world of debugging")
