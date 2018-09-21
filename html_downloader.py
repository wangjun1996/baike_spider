# coding:utf8
import urllib

class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        #equest = urllib.request.Request(url)
        #response = urllib.request.urlopen(request,context = context)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    



