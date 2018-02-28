#!/usr/bin/python

import web
import bs4
import urllib2
import re

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        web.header('Content-Type', 'text/plain')
        response = urllib2.urlopen('https://boinc.bakerlab.org/rosetta/cpu_list.php')
        soup = bs4.BeautifulSoup(response, 'html5lib')
        tbl = soup.find('table', class_='table table-condensed ')
        for tr in tbl.tbody.find_all('tr'):
            s = '\t'.join( [td.string for td in tr.find_all( re.compile('td|th'))] )
            yield s

if __name__ == "__main__":
    app.run()
