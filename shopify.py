#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring
from time import sleep

done = '' #open('shopify.csv').read()

def main():
    html = fromstring(urlopen('http://apps.shopify.com').read())
    for a in html.cssselect('#pageless-apps a.appcard-content-wrapper'):
        url = a.attrib['href']
        if url in done:
           continue

        try:
            website = addon(url)
        except:
            website = ''

        print 'freshbooks.com,' + website + ',' + url
        sleep(5)

def addon(url):
    html = fromstring(urlopen(url).read())
    website = html.xpath('//td[text()="Website"]/following-sibling::td[position()=1]/a/@href')[0]
    return website

main()
#print addon('http://apps.shopify.com/landable')
