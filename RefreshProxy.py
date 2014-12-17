__author__ = 'j'
import urllib
import time
import os
class RefreshProxy:
    proxyList = ["46.165.249.92:80",
                 "5.196.116.22:7808",
                 "199.200.120.140:7808",
                 "199.200.120.37:7808",
                 ]

    def start(self):
        workingList = self.checkWorkingProxy(self.proxyList)
        exportString = "export http_proxy='%s'"
        x = 0
        while True:
            os.system(exportString % workingList[x])
            if x+1 == len(workingList):
                x = 0
            else:
                x+=1
            print "Loaded new proxy, sleeping 30 minutes."
            time.sleep(1800)

    def checkWorkingProxy(self, proxyList):
        workingProxy = []
        a = 0
        for x in range(len(proxyList)):
            proxy = str(proxyList[x])
            try:
                urllib.urlopen("http://google.com", proxies={'http': "http://"+proxy})

            except IOError:
                print a,"/",len(proxyList)," Proxy not working"
                a +=1
            else:
                workingProxy.append(str(proxyList[x]))
        print "Done loading proxies."
        return workingProxy

    def __init__(self):
        pass