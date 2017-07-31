#!/bin/python

import cgi
#import cgitb
#cgitb.enable() # special exception handler (that just keeps me from running it in cli)

import urllib.request

###### HTTP headers
#print("Content-Type: application/xml; charset=UTF-8")
print("Content-Type: text/html")
print("access-control-allow-origin: *")

print()

###### XML proxy
#form = cgi.FieldStorage()
#form = {'u':'test', 'status':'some', 'type':'clacks'}
form = {'u':'SkeevingQuack', 'status':'all', 'type':'anime'}

querymap = map(lambda key:key+'='+form[key], form.keys())
queries = '&'.join(querymap)

base_url = "http://myanimelist.net/malappinfo.php"

request = base_url + '?' + queries

with urllib.request.urlopen(request) as response:
#    print(response.read().decode('utf-8', errors='replace'))
    with open("list.xml", 'wb') as f:
        f.write(response.read())

print("<root></root>")
