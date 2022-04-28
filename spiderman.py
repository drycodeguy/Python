#!/usr/bin/env python3
# Amos 
#2/4/2022

#this section imports external functions
from fileinput import close
import requests
import re

#this section defines the function called scrape
def scrape(url):
    #requests one url
    r = requests.get(url)
    #uses regex to parse through all data for valid URLs
    matches = re.findall(r'href=[\'|\"](\S*)[\'|\"]', r.text)
    fixed = []
    for x in matches:
        try:
            #turns relative url paths into absolute paths
            if x[0] == '/':
                fixed.append(f'{url}{x}')
            # looks for urls starting with http and includes https
            elif x[0:4] == 'http':
                fixed.append(x)
            #passes on broken or invalid links
            else:
                pass
        except IndexError:
            pass

    # returs results into a list called fixed
    return fixed

#the target url
web = 'http://example.com'
#results from the first scrape of the target url 
res = scrape(web)
#defines fin as a set 
#sets dont duplicate
fin = set()
#creates a list called res2 
res2 = []
#specifies one item in the list res in a loop 
for x in res:
    #adds the results of the first webscrape into the fin set
    fin.add(x)
    #adds the results of the first scrape into the list res2
    res2.extend(scrape(x))

#creates a list called res3
res3 = []
#specifies one item in the list res2 in a loop
for x in res2:
    #adds the 2nd results of the first webscrape into the fin set
    fin.add(x)
    #adds the 2nd results of the first scrape into the list res2
    res3.extend(scrape(x))
#specifies one item in the list res3 in a loop 
for x in res3:
    ##adds the 3rd results of the first scrape into the fin set 
    fin.add(x)

#specifies one item in the set fin and initialises a loop 
for x in fin:
    #opens the file OP1.txt in append mode 
    f = open("OP1.txt", "a")
    #writes the output for x, then moves to the next line
    f.write(str(x+'\n'))
    #closes the file 
    f.close


