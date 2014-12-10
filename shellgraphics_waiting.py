#!/usr/bin/env python

from sys import stdout
import time

def waiting(text=''):
                c = 0
                while 1:
                    for i in range(1,4):
                         stdout.write("\r")
                         stdout.write(text + " [" + "." * i + " " * (3 - i) + ']')
                         stdout.flush()
                         time.sleep(1)
                    stdout.write("\r")
                    stdout.write("              ")
                    stdout.write("\r")
                    c += 1
                    if c > 5:
                                    return

if __name__ == '__main__':
                waiting('<program>')
                if True:
                                waiting('<program2>')
                print 'done'