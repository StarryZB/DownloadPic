from urllib import request
import re
import os

def open_url(num):
	url = 'http://www.umei.cc/meinvtupian/'+str(num)+'.htm'
	req = request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
	page = request.urlopen(req)
	page = page.read().decode('utf-8')
	return page

def get_image(page):
        p = r'<img src="([^"]+\.jpg)"'
        imglist = re.findall(p,page)
        for each in imglist:
                print(each)
                filename = each.split("/")[-1]
                try:
                    request.urlretrieve(each,filename,None)
                except BaseException as e:
                    print('图片加载出错')	

if __name__ == '__main__':

        for x in list(range(1,3)):#下载第1到第3页图片
            page = open_url(x)
            get_image(page)
	
