#!/usr/bin/python3
from time import sleep
from random import shuffle
import subprocess

dic = dict()
dire = []

dire.extend(subprocess.getoutput("ls | grep jpg").split("\n"))
dire.extend(subprocess.getoutput("ls | grep png").split("\n"))
message = "f[fill] c[center] v[viscolor] q[quit] _[append to _]| "
shuffle(dire)

for pic in dire:
    subprocess.call(["wal", "-q", "-n", "-i", pic])
    subprocess.call(["feh", "--bg-fill", pic])

    command = input(message)

    while command is 'f' or command is 'c' or command is 'v':
        if command is 'f' or command is "fill":
            subprocess.call(["feh", "--bg-fill", pic])
        if command is 'c' or command is "center":
            subprocess.call(["feh", "--bg-center", pic])
        if command is 'v' or command is "viscolor":
            subprocess.call(["python3", "/home/automata/Code/viscolor/viscolor.py"])
        command = input(message)

    if command is 'q': break
    if command not in dic: dic[command] = [pic]
    else: dic[command].append(pic)

for word in dic.keys():
    print(word, dic[word])
