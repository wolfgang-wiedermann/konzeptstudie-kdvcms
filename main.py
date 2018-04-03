#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import os
import sys  
import markdown

reload(sys)  
sys.setdefaultencoding('utf8')

CONTENT_ROOT = "./sites"
OUTPUT_ROOT = "./out"
TEMPLATE_FILE = "./template.html"

#
# Methode zur Umwandlung eines einzelnen Markdown-Files in eine Seite
#
def convert(root, out, file, template):
    in_filename = os.path.join(root, file)
    out_filename = os.path.join(out, file.replace(".md", ".html"))

    with open(in_filename, "r") as in_file:
        md_content = in_file.read()
        
    html_content = markdown.markdown(md_content, extensions=['markdown.extensions.fenced_code'])
    page = template.format("Titel", "Menu", html_content)
    print(page)

    with open(out_filename, "w") as out_file:
        out_file.write(page)


#
# Hier das zukünftige Main
#
md = markdown.Markdown()
template = ""

with open(TEMPLATE_FILE, "r") as template_file:
    template = template_file.read()

for root, subfolders, files in os.walk("./sites", followlinks=False):
    print("{0} {1}".format(root, files))
    for file in files:
        convert(root, OUTPUT_ROOT, file, template)

