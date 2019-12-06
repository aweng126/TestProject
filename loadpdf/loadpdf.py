# coding = UTF-8
import sys
import urllib.request as req

def loadPdfFile(filename):
    for line in open(filename):
        args = line.split()
        # print(args[0]+'\t'+args[1]+'\t'+args[2])
        id = args[0]
        title = args[1]
        url = args[2]
        req.urlretrieve(url,"files/"+title+".pdf")


if __name__ == '__main__':
    #file name like paper1206.txt
    filename = sys.argv[1] 
    loadPdfFile(filename)
   
