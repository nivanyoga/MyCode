__author__ = 'DEFAULT'

import os
import io
import fileinput

from bs4 import BeautifulSoup

HTML_FILE = 'C:\\HP_WORKLAPTOP\\TWG\\TWG_WEBSITE_COM\\htdocs\\index.asp'

def open_html(html_file):
    with open(html_file, encoding="utf8") as f:
        read_data = f.read()
        # print (read_data)
    f.closed
    return BeautifulSoup(read_data, 'html.parser')

def process_section(text):
    print ("***********************************start section")
    print (text)
    print (text.find('href'))
    print ("***********************************end section")

#def string_text(text):


#for bref in soup.find_all('span'):
#    process_section(bref)

def process_containers(soup):
    divs = soup.find_all("div")
    for div in divs:
        containers = div.find_all("span", {"class":"regtext"})
        for container in containers:
            print ("start con")
            texts = container.findAll(text=True)
            for t in texts:
                if t == "\t\n":
                    continue
                if (t != "Full Story" and t != "["  and t != "]" and t != "\n"):
                    print (str.strip(t))
            mylink = container.find("a")
            print ( mylink.attrs['href'] )
            print ("end con")

def main():
    soup = open_html(HTML_FILE)
    #print(soup.prettify())
    process_containers(soup)

if __name__ == "__main__":
    main()


