'''
Send requests to salt-api and return responses to the CLI
'''
import json
import urllib
import urllib2

SALTAPIURL = 'localhost:8000'
SALTUSER = 'shouse'
SALTPASS = 'saltdev'

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
}

lowstate = [{
    'client': 'local',
    'tgt': '*',
    'fun': 'test.ping',
    'username': SALTUSER,
    'password': SALTPASS,
}]

postdata = json.dumps(lowstate).encode()
clen = len(postdata)

req = urllib2.Request(SALTAPIURL, postdata, HEADERS)
req.add_header('Content-Length', clen)
        
try:
    f = urllib2.urlopen(req)
    print "XXX: %s" % f.read()
except (urllib2.HTTPError, urllib2.URLError):
    pass
