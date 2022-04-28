#!/usr/bin/python3
#Amos Struthers 

#imports processes 
import re
from fileinput import close
import argparse
import sys

#creates janitor function 
def janitor(file):
    #creates list res
    res = []
    #parses file line by line
    for line in file:
        #if email arguments used, uses regex to find email 
        if args.email:
            matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
            for x in matches:
                #puts email matches into res list
                res.append(x)
        #if phone args used, uses regex to fine 10 digit number strings 
        elif args.phone:
            matches = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', line)
            for x in matches:
                #puts numbers into res list
                res.append(x)
        else:
            print('no valid search parameters')
    return res 

#if name == "_main_":
#creates arg parameters
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--phone", help="find phone numbers in data")
parser.add_argument("-e", "--email", help="find emails in data")
args = parser.parse_args()
#opens file as read 
with open(sys.argv[2], 'r') as my_file:
    results = janitor(my_file)
    # finds results and prints results line by line. 
    for x in results:
        print(x+'\n')
