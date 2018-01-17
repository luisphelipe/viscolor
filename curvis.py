#!/usr/bin/python3
import curses


color_path = "/home/automata/.cache/wal/colors"
def load_color_scheme():
    colors = []
    with open(color_path, 'r') as cfile:
        for line in cfile:
            colors.append([\
                    int(line[1:3], 16),\
                    int(line[3:5], 16),\
                    int(line[5:7], 16)])
    return colors

def main(stdscr):
    curses.curs_set(False)
    colors = load_color_scheme()
    stdscr.clear()

    curses.init_color(100, 255, 255, 255)
    for c in range(1, len(colors)+1):
        curses.init_color(c, \
                colors[c-1][0], \
                colors[c-1][1], \
                colors[c-1][2])
        curses.init_pair(c, 100, c)

    blank = " "*74 + "\n"
    for c in range(1, len(colors)+1):
        string1 = "{:02d} #".format(c-1)
        for color in colors[c-1]:
            hexs = str(hex(color))[2:].upper()
            if len(hexs) == 1: string1 += "0"
            string1 += hexs
        string1 += " "*64 + "\n"

        stdscr.addstr(string1, curses.color_pair(c))
        stdscr.addstr(blank, curses.color_pair(c))

    stdscr.refresh()
    while(stdscr.getkey() != 'q'):
        continue

if __name__ == "__main__": 
    curses.wrapper(main)

