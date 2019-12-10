# coding = UTF-8
import sys
import logging
import urllib.request as req
import queue
import threading

q = queue.Queue()
threads = []
maxThreadsNum = 10
filePath = "files/{title}.pdf"



class pdfInfo(object):
    def __init__(self,_id,_title,_url):
        self.id = _id
        self.title = _title
        self.url = _url
    def selfInfo(self):
        print("id: %s title: %s url: %s" %(self.id,self.title,self.url))

def worker():
    while True:
        item = q.get()
        if item is None:
            break;
        
        # just test : download specific pdfInfo
        # item.selfInfo()

        # download pdf
        try:
             req.urlretrieve(item.url,filePath.format(title = item.title))
        except Exception as e:
             raise e
        else:
             logging.warning("download %s success"%(item.title))
        

        q.task_done()

def loadPdfInfo(filename):
    for line in open(filename):
        args = line.split()
        # print(args[0]+'\t'+args[1]+'\t'+args[2])
        id = args[0]
        title = args[1]
        url = args[2]
        q.put(pdfInfo(id,title,url))
       
            

def downloadPdfs(maxThreads):
    for i in range(maxThreads):
        t = threading.Thread(target = worker)
        t.start()
        threads.append(t)


def stopWorks():
    # block until all tasks are done
    q.join()

    # stop all workers
    for i in range(maxThreadsNum):
        q.put(None)
    for t in threads:
        t.join()   


if __name__ == '__main__':
    # file name like paper1206.txt
    filename = sys.argv[1] 
    maxThreadsNum = 10
    loadPdfInfo(filename)
    downloadPdfs(maxThreadsNum)
    stopWorks()
    