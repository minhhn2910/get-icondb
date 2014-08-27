import urllib
import urllib2
from bs4 import BeautifulSoup
url = 'http://www.iconsdb.com/icon-sets/green-fabric-icons/?page='
for i in range(1,50):
    while True:
        try:            
            print 'parse url ' + url+str(i)
            request = urllib2.Request(url+str(i), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36' })
            html = urllib2.urlopen(request).read()
            soup = BeautifulSoup(''.join(html))
            imgTags = soup.findAll('figure') # find all image tags
            for imgTag in imgTags:
                soup_figure = BeautifulSoup(str(imgTag))
                source= soup_figure.img['src']
                array = source.split('/')
                img_old = array[len(array)-1]
                img_link = 'http://www.iconsdb.com/icons/download/icon-sets/green-fabric/'+img_old[:-6]+'512'+img_old[-4:]
                fileName = img_old[:-7]+img_old[-4:]
                print img_link
                req = urllib2.Request(img_link, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36' })
                imgData = urllib2.urlopen(req).read()
                output = open(fileName,'wb')
                output.write(imgData)
                output.close()
        except:
            continue
        break
