# CTEC 121
# Parsing HTML files using Python
# CTEC 121 - Clark College
# Reading HTML files with Python
# by Bruce Elgort
# August 20, 2017
# Lab No. 8

# HTML Parser library - https://docs.python.org/3/library/html.parser.html
from html.parser import HTMLParser

# io library - https://docs.python.org/3/library/io.html
import io

class MyHTMLParser(HTMLParser):
    # COMMENT THIS
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    # COMMENT THIS
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    # COMMENT THIS
    def handle_data(self, data):
        print("Encountered some data  :", data)

    # COMMENT THIS
    def handle_comment(self,data):
        print("Encountered a comment  :",data)

    # COMMENT THIS
    def unknown_decl(self,data):
        print("Encountered something unknown!",data)

def main():
    print("Starting...")
    
    # COMMENT THIS
    parser = MyHTMLParser()

    # COMMENT THIS
    filename = 'welcome_page.html'

    # COMMENT THIS
    with io.open(filename,'r',encoding='utf8') as f:
        # COMMENT THIS
        text = f.read()
        # COMMENT THIS
        parser.feed(text)

    print("Parsing completed!")


    
main()    
