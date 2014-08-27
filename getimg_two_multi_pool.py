import commands
import multiprocessing
import urllib
import os
def getimg(url,k):
  try:  
    print url,os.getpid()
    urllib.urlretrieve(url,'%s.jpg'%k)
  except:
    pass
    #commands.getstatusoutput('wget %s'%url)
    #os.system('wget %s'%url)
    #print getpid()


def main(line):
    result=[]
    pool_size = 40
    process_pool = multiprocessing.Pool(processes=pool_size)
    for i,k in enumerate(line):
        result.append(process_pool.apply_async(func=getimg,args=(k,i)))
    process_pool.close()
    process_pool.join()
#    for i in result:
#        print i
if __name__=='__main__':
    line=[]
    with open('tt.txt') as f:
        for i in f.readlines():
            line.append(i) 
    main(line)

