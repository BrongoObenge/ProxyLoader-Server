__author__ = 'j'
import urllib
import time
import os
import urllib2, socket

class RefreshProxy:
    proxyList = ["5.53.16.183:8080",
                "197.231.248.93:80",
                "197.231.248.92:80",
                "190.14.52.12:80",

                 ]
    socket.setdefaulttimeout(30)

    def start(self):
        workingList = self.checkWorkingProxy(self.proxyList)
        exportString = "export http_proxy='%s'"
        x = 0
        while True:
            print "Starting Proxy: "+ exportString % workingList[x]
                #print "echo \""+exportString % workingList[x]+"\" >> /home/ubuntu-0868049/.bash_profile"
            #Add something that deletes previous http_export
            os.system("echo "+exportString % workingList[x]+">> /etc/profile")
                #os.system("source /home/ubuntu-0868049/.bash_profile")
            if x+1 == len(workingList):
                x = 0
            else:
                x+=1
            print "Loaded new proxy, sleeping 30 minutes."
            time.sleep(1800)

    def checkWorkingProxy(self, proxyList):
        workingProxy = []
        for item in proxyList:
            if is_bad_proxy(item):
                print "Bad Proxy", item
            else:
                print "Added proxy"
                workingProxy.append(item)
        print "Done loading proxies."
        return workingProxy

    def __init__(self):
        pass

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('http://tweakers.net/pricewatch/352536/kingston-kta-mb1600s-4g/specificaties/')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0

