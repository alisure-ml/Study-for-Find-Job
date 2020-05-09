"""
read read[addr=0x17,mask=0xff,val=0x7],read_his[addr=0x17,mask=0xff,val=0x7],read[addr=0xf0,mask=0xff,val=0x80]

read read[addr=0x17,mask=0xff,val=0x7t],read_his[addr=0x17,mask=0xff,val=0x7],read[addr=0xf0,mask=0xff,val=0x80]
"""
import re
import sys

def f():
    p, v = sys.stdin.readline().strip().split(" ")
    v = v.split("],")
    v[-1] = v[-1][:-1]
    v = [v1.split("[") for v1 in v]
    is_f = True
    for one in v:
        if p == one[0]:
            if re.match(r"addr=0(X|x)[0-9a-fA-F]+,mask=0(X|x)[0-9a-fA-F]+,val=0(X|x)[0-9a-fA-F]+$", one[1], flags=0):
                r = [o.split("=")[1] for o in one[1].split(",")]
                print r[0], r[1], r[2]
                is_f = False
        pass
    if is_f:
        print "FAIL"

f()
