#coding:utf8
import urllib2
import urllib
import re
import os
import threading
lock = threading.Lock()
url='http://xxxxxxxxx/'
imgurl=[]
def getHtml(url):
    global imgurl
    page = urllib.urlopen(url)
    lock.acquire()
    html = page.read()
    reg=re.compile(r'src="(.[^?]*?\.jpg)"') 
    imglist = re.findall(reg,html)
    imgurl=imgurl+(list(set(imglist)))
    lock.release()

def getUrl(url):
        page = file('tt.txt','r')
        html = page.read()
        reg = re.compile(r'href="(/post/[\d\w_]*)"')
        urlList=re.findall(reg,html)
        return urlList            

newurl=getUrl(url)
url_list=[url+i for i in newurl]
url_list=list(set(url_list))

muth=[]
for i in url_list:
    muth.append(threading.Thread(target=getHtml,args=(i,)))
for i in muth:
    i.start()
for i in muth:
    i.join()

with open('tt.txt','wb+') as f:
    f.write('\n'.join(imgurl))

'''
for i in imgurl:
    os.system('wget %s'%i)
'''

