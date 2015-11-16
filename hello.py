#!/bin/env python 
import requests
import threading

class MyThread(threading.Thread):
    def __init__(self, urls):
        super(MyThread, self).__init__()
        self.urls = urls

    def run(self):
        for url in self.urls:
            try:
                r = requests.get("http://" + url)
                if r.status_code == 200:
                    print "[ " + url +" ]" + " success"
                else:
                    print "[ " + url + "] " + " fail"
            except requests.ConnectionError:
                print "Failed to get http://" + url 

if __name__ == '__main__':
	URLS = ["www.baidu.com", "www.sina.com.cn", "www.qq.com", "www.pptv.com", "www.huzichun.com"]

	mythreads = []
	for i in range(5):
		mythread = MyThread(URLS)
		mythreads.append(mythread)
		mythread.start()

	for mythread in mythreads:
		mythread.join()

	print "I'm in the main thread."
