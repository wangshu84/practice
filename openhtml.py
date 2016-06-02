#!/usr/bin/python
import urllib2
import os, sys, re
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
#need to install the BeautifulSoup first using apt-get.



#put full path for all .html files in the currentworkdir
currentworkdir=os.getcwd()
print currentworkdir
filelist=os.listdir(currentworkdir)
filepath=[]
cnt=0
for i in filelist:
    if i.endswith(".html"):
        filepath.append(os.path.join(currentworkdir,i))
        print filepath

#open all .html files in currentworkdir
for path in filepath:
    #path='file:C:\\Users\\shu.wang2\\Documents\\Personal\\Project\\TestReport.html'
    page=urllib2.urlopen('file:'+path).read()
    print page

path = 'file:C:\\Users\\shu.wang2\\Documents\\Personal\\Project\\TestReport.html'
page=urllib2.urlopen(path).read()
# in each page file, which is the html report, read line by line
#this part later can be simplified by def functions, and coupled with the previous loop
#for each page file, create a dic() that contain the line and the the linenumber
lines = {}
linenum = 0
testID={}
for line in page.splitlines():
    line=line.strip()
    if line.startswith("<td>src.dxHTMLTestRunner.testCases"):
        #lines[linenum]=line
        #linenum+=1
        #print lines, len(lines)
        testinfo=line.split(".")[4]
        testsetID=testinfo.split(":")[1][:-3]
        print testsetID
        #this is the testsetID, now need to get all testcase names for this testsetID, which could be dynamic number of test cases
        # contain class="test cases"

#use HTMLPraser, recognize the tag and extract the element?
"""
class HTMLParser.HTMLParser:
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data
#tr #pt1.1, then starttag as <div class="testcase">
#end tage is </div>
"""

#from testgroup/testcase, get the information for written into the excel
#infromation that need to get from the lines{} directory: test set ID, test case name; status and actual results
soup = BeautifulSoup(f, "html5lib")