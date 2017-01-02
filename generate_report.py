#!/usr/bin/env python3


import sqlite3
from build_db import ATTACKS

HTML="""
<!DOCTYPE html>

<html>
<head>
    <style>
body,textarea,input,select{{background:0;border-radius:0;font:16px sans-serif;margin:0}}.addon,.btn-sm,.nav,textarea,input,select{{outline:0;font-size:14px}}.smooth{{transition:all .2s}}.btn,.nav a{{text-decoration:none}}.container{{margin:0 20px;width:auto}}@media(min-width:1310px){{.container{{margin:auto;width:1270px}}}}.btn,h2{{font-size:2em}}h1{{font-size:3em}}.table th,.table td{{padding:.5em;text-align:left}}.table tbody>:nth-child(2n-1){{background:#ddd}}.row{{margin:1% 0;overflow:auto}}.col{{float:left}}.table,.c12{{width:100%}}.c11{{width:91.66%}}.c10{{width:83.33%}}.c9{{width:75%}}.c8{{width:66.66%}}.c7{{width:58.33%}}.c6{{width:50%}}.c5{{width:41.66%}}.c4{{width:33.33%}}.c3{{width:25%}}.c2{{width:16.66%}}.c1{{width:8.33%}}@media(max-width:870px){{.row .col{{width:100%}}}}.msg{{background:#def;border-left:5px solid #59d;padding:1.5em}}    
    </style>
    <title>Attack report</title>
</head>

<body>

<div class="row">
<h1>Attack report</h1>
    <div class="col c4"> </div>
    <div class="col c4">    {0} </div>
    <div class="col c4"></div>
</div>



</body>
</html>

"""


def rows_to_table(headers, rows):
    table="<table class='table'>"
    
    table+="<thead>"
    table+="<tr>"
    for h in headers:
        table+="<th>"+h+"</th>"
    table+="</tr>"
    table+="</thead>"
    
    table+="<tbody>"
    for row in rows:
        table+="<tr>"
        for pos in range(0, len(row)):
            table+="<td>" + str(row[pos])+ "</td>"
        table+="</tr>"
    table+="</tbody>"
    
    table+="</table>"
    
    return table

def generate_report_by_country(conn):
    sql="select country, count(*) as total from attacks group by country order by total desc limit 20;"
    rows=conn.execute(sql)
    report=rows_to_table(["Country", "Total"],rows)
    return report

def generate_report_by_city(conn):
    sql="select country, city, count(*) as total from attacks group by country, city order by total desc limit 20;"
    rows=conn.execute(sql)
    report=rows_to_table(["Country", "City", "Total"],rows)
    return report
    
    
def generate_report():
    conn=sqlite3.connect(ATTACKS)
    generate_report_by_country(conn)
    report=""
    report+"<h3>By country</h3>"
    report+=generate_report_by_country(conn)
    report+"<h3>By city</h3>"
    report+=generate_report_by_city(conn)
    print (HTML.format(report))
    conn.close()
    
if __name__ == '__main__':
    generate_report()