__author__ = 'j'
import urllib
import time
import os
class RefreshProxy:
    proxyList = [
                 "62.153.96.164:80",
                 "83.128.239.152:80",
                 "94.210.6.125:80",
                 "185.30.147.197:8080",
                 "5.53.16.183:8080",


                 ]

    def start(self):
        workingList = self.checkWorkingProxy(self.proxyList)
        exportString = "export http_proxy='%s'"
        x = 0
        while True:
            print "Starting Proxy: "+ exportString % workingList[x]
            os.system(exportString % workingList[x])
            if x+1 == len(workingList):
                x = 0
            else:
                x+=1
            print "Loaded new proxy, sleeping 30 minutes."
            #time.sleep(1800)

    def checkWorkingProxy(self, proxyList):
        workingProxy = []
        a = 0
        for x in range(len(proxyList)):
            proxy = str(proxyList[x])
            try:
                urllib.urlopen("http://tweakers.net/pricewatch/323351/crucial-ballistix-tactical-blt2c4g3d1608et3lx0ceu/specificaties/", proxies={'http': "http://"+proxy})
            except IOError:
                print "Proxy not working: " + proxy
                a +=1
            except:
                print "Error"
            else:
                workingProxy.append(str(proxyList[x]))
        print "Done loading proxies."
        return workingProxy

    def __init__(self):
        pass