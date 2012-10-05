#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring
from time import sleep

done = open('freshbooks.csv').read()

def main():
    html = fromstring(urlopen('http://community.freshbooks.com/addons').read())
    for a in html.cssselect('.addons a.nohover'):
        url = a.attrib['href']
        # Weird pages
        if url in [
            'http://community.freshbooks.com/addons/view/os_x_time_tracker_widget/',
            'http://community.freshbooks.com/addons/view/late_payment_fees/',
        ]:
           continue
        elif url in done:
           continue

        website = addon(url)
        print 'freshbooks.com,' + website + ',' + url
        sleep(5)

def addon(url):
    html = fromstring(urlopen(url).read())
    website = html.xpath('//strong[text()="Website:"]/following-sibling::a[position()=1]/@href')[0]
    return website

main()
#addon('http://community.freshbooks.com/addons/view/os_x_time_tracker_widget/')
