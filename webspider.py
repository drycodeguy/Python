www#!/usr/bin/python3

import requests
import re

#Create variable to store URL
url=input("Enter a URL: ")

#Define fcuntion
def scrape(url):
#Use imported module with url as argument    
    r = requests.get(url)
#Create varibel to store strings that match regex
    matches = re.findall(r'href=[\'|\"](\S*)[\'\"]',r.text)
    fixed=[]
#Iterate through list to differentiate between relative and absolute paths
    for x in matches:
        if x[0] == '/':
            fixed.append(f'{url}{x}')
        
        else:
            fixed.append(x)
    return fixed

#Call function and stor output in variable
res = scrape(url)

fin = set()

#Iterate through list of links and add to set. Duplicates ignored
for x in res:
    fin.add(x)

#runs function for each link in set and prints to screen
for x in fin:
    out = scrape(x)

f = open('testfile2.txt', 'a')
f.write(str(out))
f.close()