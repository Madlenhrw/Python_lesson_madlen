# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:58:15 2019

@author: madlen.maisel
"""

authors = ["Darwin", "Lovelace", "Hawking", "Noether"]

output_fh = open("list.html", "w")

scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grandiose Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""

for author in authors: 
    print ("<li> + author + "</li")
scaffold_end = """

</body>



</html>"""

scaffold_end = """

output_fh = open("list.html", "w")
output_fh.write(scaffold)
output_fh.close()