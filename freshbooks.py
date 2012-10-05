#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring
from time import sleep

def main():
    html = fromstring(urlopen('http://community.freshbooks.com/addons').read())
    for a in html.cssselect('.addons a.nohover'):
        website = addon(a.attrib['href'])
        print 'freshbooks.com,' + website + ',' + a.attrib['href']
        sleep(5)

def addon(url):
    html = fromstring(urlopen(url).read())
    website = html.xpath('//strong[text()="Website:"]/following-sibling::a[position()=1]/text()')[0]
    return website

main()
