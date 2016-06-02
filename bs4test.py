#!/usr/bin/env python
from bs4 import BeautifulSoup
import os
import urllib2
import fnmatch
import openpyxl

#file is a list of the files in the current directory, and the fnmatch would return the files that match the
#pattern that is .html file
filelist=os.listdir('.')
print fnmatch.filter(filelist, '*.html')


file=open("TestReport.html")
soup=BeautifulSoup(file, 'html.parser')
table=soup.find("table", {'id':"result_table"})
#print table
tablerows=iter(table.find_all('tr'))
#print tablerows
#tabletd=iter(table.find_all('td')
#print tabletd

for row in tablerows:
    if row.has_attr('class'):
        #in each tr, iterate the td, all td would follow the headrow in 6 columns.
        #the max of the td would be the 6; the 1st td is where we get the TC_ID and testcase name info.
        #the 4-6 td is the testcase status.
        #print row
        rowtd=iter(row.find_all('td'))
        for td in rowtd:
            if td.has_attr('id'):
            #use zip() to create a list of tuple. td content in header_row will be paired with td content
            #from other rows that has class attribute
                testcase_stat=zip(["TestCase", "Duration", "Count", "Pass", "Fail", "Error", "View"], [td.get_text().strip()])
                print testcase_stat