# coding = UTF-8
import sys
import urllib.request as req

def loadcode(filename):
    with open(filename,'r') as f:
        for line in f.readlines():
            line = line.strip()
        
            if line:
                args = line.split()
                name = args[0]
                url = args[1]
                # print(name+'\t'+url)
                req.urlretrieve(url+"/archive/master.zip","codes/"+name+".zip")
            # else:
                # todo
          

if __name__ == '__main__':
    filename = sys.argv[1]
    loadcode(filename)