
#!/usr/bin/python
import httplib
import sys
from termcolor import colored 

print colored ("welcome to my webchecker" + "!","blue", attrs=['bold'])  
if len(sys.argv) < 3:sys.exit("Usage " + sys.argv[0] + " <hostname> <port>\n")

host = sys.argv[1]
port = sys.argv[2]

client = httplib.HTTPConnection(host,port)
client.request("GET","/")
resp = client.getresponse()
client.close()

if resp.status == 200:
    print host + " : OK"
    sys.exit()
    print host + " : DOWN! (" + resp.status + " , " + resp.reason + ")"
