#!/usr/bin/python3
import subprocess


color_path = "/home/automata/.cache/wal/colors"

html_top = "<!DOCTYPE html>\n\
<html>\n\
    <head>\n\
	<meta charset=\"UTF-8\">\n\
	<title>color-scheme</title>\n\
        <style>\n\
            * {\n\
                font-family: monospace;\n\
                margin: 0;\n\
                padding: 0;\n\
            }\n\
            body {\n\
                margin-top: 4px;\n\
            }\n\
            div {\n\
                margin: 2px auto;\n\
                width: 1300px;\n\
                height: 40px;\n\
            }\n\
        </style>\n\
    </head>\n\
    <body>"

html_div ="\n       <div style=\"background:{0};\"><h3>{1:02d} {0}</h3></div>"

html_bot = "\n    </body>\n\
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
    """
    for c in color_scheme:
        print("{:02d} {}".format(n, c))
        n += 1
    """

    template = html_top
    for i in range(len(color_scheme)):
        template += html_div.format(color_scheme[i].upper(), i)

    template += html_bot

    with open("htmlvisualizer.html", 'w') as htmlfile:
        htmlfile.write(template)

    subprocess.call(["chromium", "htmlvisualizer.html"])


if __name__ == "__main__": main()
