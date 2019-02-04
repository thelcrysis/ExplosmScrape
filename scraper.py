import urllib2
from bs4 import BeautifulSoup
import sys
import os

def main():
    sourcepage = 'http://explosm.net/comics/'
    htmlfile = open('output.html','w+')
    htmlfile.write('<html><body>')
    emptyPages=0
    pageCounter=0
    while emptyPages<50:
        pageCounter+=1
        try:
            currentSourcepage=sourcepage + str(pageCounter)
            print currentSourcepage 
            page = urllib2.urlopen(currentSourcepage)
        except urllib2.HTTPError as e:
            emptyPages+=1
            continue
        soup = BeautifulSoup(page, 'html.parser')
        name = soup.find('img', attrs={'id': 'main-comic'})
        if name is not None:
            emptyPages = 0
        outputFormat = '<img src=\"http:' + name['src'] + '\"><br>' 
        htmlfile.write(outputFormat + '\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
           sys.exit(0)
        except SystemExit:
            os._exit(0)





