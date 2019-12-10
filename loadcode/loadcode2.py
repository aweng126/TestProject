# coding = UTF-8
import sys
import urllib.request as req
import queue
import threading
import logging

q = queue.Queue()
threads = []
maxThreadsNum = 10
filePath = "codes/{name}.zip"
codeUrl = "{url}/archive/master.zip"


class codeInfo(object):
    def __init__(self,_id,_name,_url):
        self.id = _id
        self.name = _name
        self.url = _url

    def selfInfo(self):
        print("codeInfo id: %s, name: %s, url: %s"%(self.id,self.name,self.url))

          
def loadCodeInfo(filename):
     with open(filename,'r') as f:
        for line in f.readlines():
            line = line.strip()
        
            if line:
                args = line.split()
                id = args[0]
                name = args[1]
                url = args[2]
                q.put(codeInfo(id,name,url))


def worker():
    while True:
        item = q.get()
        if item is None:
            break;

        # item.selfInfo()
        try:
            req.urlretrieve(codeUrl.format(url = item.url),filePath.format(name = item.name))
        except Exception as e:
            raise e
        else:
            logging.warning("download %s success"%(item.name))

        q.task_done()


def downloadCodes(maxThreadsNum):
    for i in range(maxThreadsNum):
        t = threading.Thread(target = worker)
        t.start()
        threads.append(t)

def stopWorkers():
    q.join()

    for i in range(maxThreadsNum):
        q.put(None)
    for t in threads:
        t.join()

if __name__ == '__main__':
    filename = sys.argv[1]
    loadCodeInfo(filename)
    downloadCodes(maxThreadsNum)
    stopWorkers()
