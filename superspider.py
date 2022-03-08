#!/usr/bin/env python3

from fileinput import close
import requests
import re

def scrape(url):
    r = requests.get(url)
    matches = re.findall(r'href=[\'|\"](\S*)[\'|\"]', r.text)
    fixed = []
    for x in matches:
        try:
            #turns relative paths into absolute paths
            if x[0] == '/':
                fixed.append(f'{url}{x}')
                
            elif x[0:4] == 'http':
                fixed.append(x)
            #passes on broken or invalid links
            else:
                pass
        except IndexError:
            pass

    # print(matches)
    return fixed

web = 'http://example.com'

res = scrape(web)

#print(res)
#sets dont duplicate
fin = set()
res2 = []
for x in res:
    fin.add(x)
    res2.extend(scrape(x))
    #print(x)
#print(res2)


res3 = []
for x in res2:
    fin.add(x)
    res3.extend(scrape(x))
for x in res3:
    fin.add(x)
#print(res3)
f = open("OP1.txt", "a")
f.write(str(fin))
f.close







'''      
#print(type(fin2))
#print(len(fin))
    fin2 = set()
    for x in fin:
        fin2.add(x)
        #res2.extend(scrape(x))
        #print(len(fin))
    fin3 = set()
    for x in fin2:
        fin3.add(x)
res2.extend(scrape(x))
#print(len(fin))

f = open('layers.txt', 'a')
f.write(set(fin))
f.close()
''' 


