__author__ = 'DEFAULT'

import os
import io
import fileinput
import codecs

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    href = 0

    def handle_starttag(self, tag, attrs):
        print ("Encountered the beginning of a %s tag" % tag)
        if tag == "a" and attrs[0]=="href":
            self.href = 1
        else:
            self.href = 0


    def handle_endtag(self, tag):
        print ("Encountered the end of a %s tag" % tag)

    def handle_comment(self, data):
        print ("Encountered comment %s tag" % data)

    def handle_data(self, data):
        print ("Encountered comment %s tag" % data)
        if self.href == 1:
            print ("href" + data)

def main():
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()

    path = "C:\\HP_WORKLAPTOP\\TWG\\TWG_WEBSITE_COM\\htdocs\\"
    html_file = path + "index.asp"
    print (html_file)
    #f = open(html_file, "r")
    fileObj = codecs.open( html_file, "r", "utf-8" )
    contents = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file
    parser.feed(contents)

if __name__ == "__main__":
    main();