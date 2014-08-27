#coding:utf8
#!/usr/bin/env python

import eventlet, re
from eventlet.green import urllib2
import time
import sys
from urlparse import urlparse
import socket
url_list='http://www.163.com'
def url_return(tu):
    i=0
    while 1:
        if i>=tu:break
        i+=10
        yield i,i+10
		
		
		
def fetch(url):#打开url
    try:
          buf = urllib2.urlopen(url).read()
          return  url,buf
    except:
        pass
		
		
def target(url_list):#打开一个url
    url,buf = fetch(url_list)
    list_url = re.findall(r'<a href="(http.*?)"', buf)
    set_url = set(list_url)
    print '\n'.join(list(set_url))
    print len(set(list_url)),'初始url_len'
    f=open('url.test', 'a+')
    f.write('\n'.join(list(list_url)))
    f.close()
    return list(set_url),len(list(set_url))#返回一个列表和长度 这是已经写入文件中的url
	
	
def async_fetch(url_list):
    n_url_list,len_url=target(url_list)
    ini=0
    set_url = set()
    list_url=[]
    list_u=[]
    for tg,ty in url_return(len(n_url_list)):
        print tg,ty,'###########################################################'
        pool = eventlet.GreenPool(10)#开启协程
        list_buf = []
        try:
            for url, buf in pool.imap(fetch,n_url_list[tg:ty]):#通过函数imap生成器迭代的方
                    list_buf.append(buf)
        except:
            pass
        for buf in list_buf:
            list_url = re.findall(r'<a href="(http.*?)"', buf) 
            print '\n'.join(list_url),len(list_url)
            set_url = set(list_url)
            ini+=len(set_url)
          
            f=open('url.test', 'a+')
            f.write('\n'.join(list(set_url)))
            f.close()
            print ini,'******************************************'
            if ini > (10000-len_url):
                print '超过一万了'
                sys.exit()
				
				
if __name__ == '__main__':
    f=open('url.test', 'wb+')
    f.close()
    #target(url_list)
    #fetch(url_list)
    async_fetch(url_list)
