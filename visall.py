#!/usr/bin/python3
from time import sleep
from random import shuffle
import subprocess

dic = dict()
dire = []
local = subprocess.getoutput("pwd")
dots = len(local.split('/')) - 3
picname = ""
copy = ""

dire.extend(subprocess.getoutput("ls | grep jpg").split("\n"))
dire.extend(subprocess.getoutput("ls | grep png").split("\n"))
message = "f[fill] c[center] v[viscolor] q[quit] _[append to _]| "
shuffle(dire)

for pic in dire:
    subprocess.call(["wal", "-q", "-n", "-i", pic])
    subprocess.call(["feh", "--no-fehbg", "--bg-fill", pic])

    command = input(message)
    copy = "--bg-fill"
    while command is 'f' or command is 'c' or command is 'v':
        if command is 'f' or command is 'c':
            copy = ("--bg-fill" if command is 'f' else "--bg-center")
        if command is 'f' or command is "fill":
            subprocess.call(["feh", "--no-fehbg", "--bg-fill", pic])
        if command is 'c' or command is "center":
            subprocess.call(["feh", "--no-fehbg", "--bg-center", pic])
        if command is 'v' or command is "viscolor":
            subprocess.call(["python3", "/home/automata/Code/viscolor/viscolor.py"])
        command = input(message)

    picname = pic
    if command is 'q': break
    if command not in dic: dic[command] = [pic]
    else: dic[command].append(pic)

for word in dic.keys():
    print(word, dic[word])

if copy:
    subprocess.call(['cp', picname, 'wallpaper'])
    subprocess.call(['feh', copy, 'wallpaper'])
    subprocess.call(['cp', 'wallpaper', '../' * dots + "wallpaper"])
