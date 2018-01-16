#!/usr/bin/python3
import subprocess


color_path = "/home/automata/.cache/wal/colors"
htmltemplate = "<!DOCTYPE html>\n\
\n\
<html>\n\
    <head>\n\
	<meta charset=\"UTF-8\">\n\
	<title>color-scheme</title>\n\
    </head>\n\
    <body style=\"color:white;\">\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
            background:{0};\"> <h3>00 {0}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{1};\"> <h3>01 {1}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{2};\"> <h3>02 {2}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{3};\"> <h3>03 {3}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{4};\"> <h3>04 {4}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{5};\"> <h3>05 {5}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{6};\"> <h3>06 {6}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{7};\"> <h3>07 {7}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{8};\"> <h3>07 {8}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{9};\"> <h3>09 {9}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{10};\"> <h3>10 {10}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{11};\"> <h3>11 {11}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{12};\"> <h3>12 {12}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{13};\"> <h3>13 {13}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{14};\"> <h3>14 {14}</div>\n\
	<div style=\"width:1332px;\n\
	    height:30px;\n\
	    background:{15};\"> <h3>15 {15}</div>\n\
    </body>\n\
</html>"

def load_color_scheme():
    colors = []
    with open(color_path, 'r') as cfile:
        for line in cfile:
            colors.append(line[:-1])
    return colors

def main():
    color_scheme = load_color_scheme()
    n = 0
    for c in color_scheme:
        print("{:02d} {}".format(n, c))
        n += 1

    template = htmltemplate.format(
            color_scheme[0],
            color_scheme[1],
            color_scheme[2],
            color_scheme[3],
            color_scheme[4],
            color_scheme[5],
            color_scheme[6],
            color_scheme[7],
            color_scheme[8],
            color_scheme[9],
            color_scheme[10],
            color_scheme[11],
            color_scheme[12],
            color_scheme[13],
            color_scheme[14],
            color_scheme[15]
            )
    with open("htmlvisualizer.html", 'w') as htmlfile:
        htmlfile.write(template)

    subprocess.call(["chromium", "htmlvisualizer.html"])


if __name__ == "__main__": main()
