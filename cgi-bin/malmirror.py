#!/bin/python

import cgi
#import cgitb
#cgitb.enable() # special exception handler (that just keeps me from running it in cli)

###### HTTP headers
print("Content-Type: application/xml; charset=UTF-8")
print("access-control-allow-origin: *")

print()

###### XML proxy
form = cgi.FieldStorage()

#form = {'u':'test', 'status':'some', 'type':'clacks'}
querymap = map(lambda key:key+'='+form[key], form.keys())
queries = '&amp;'.join(querymap)
#queries = '&'.join(querymap)

base_url = "http://myanimelist.net/malappinfo.php"
#queries = "u=FoxInFlame&status=all&type=anime"

print("<query>")
print(base_url + '?' + queries)
print("</query>")
