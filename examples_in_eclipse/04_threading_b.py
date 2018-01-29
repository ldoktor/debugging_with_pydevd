#!/usr/bin/env python

"""
Example to demonstrate multiple threads interaction
- with locks it's better ;-)

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
        with self.__lock:
            for word in self.__msg:
                print("%s: %s" % (self.name, word))
                time.sleep(0)


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
