# Who.is website analyzer for Python 3
# Author: @itzAlex

import os
import requests
import signal
import sys
import time
import re
from bs4 import BeautifulSoup
import analyzer

# Detect CTRL+C

def control_c(signal, frame):
    print("\nCTR+C pressed, stopping program...")
    exit()

# Clean HTML and JS tags

def clean_website(html_page):
	soup = BeautifulSoup(html_page, features = "lxml" )
	for ticks in soup(['script', 'style']):
		ticks.decompose()
	with open("clean_html.txt", "w+") as file:	
		print(' '.join(soup.stripped_strings), file=file)	

# Read the clean_html file and removes unimportant strings

def read_clean_website():
	read_file_clean = (open("clean_html.txt", "r")).read()
	cleaned_file = read_file_clean[read_file_clean.find("Registrar Info"):(read_file_clean.find("Get")-1)]
	with open("cleaned_website.txt", "w+") as file:
		print(cleaned_file, file=file)


signal.signal(signal.SIGINT, control_c)
os.system("cls")
whois_website = 'https://who.is'
website_to_analyze = input("Website to analyze (eg: github.com): ")
result = requests.get(whois_website+"/whois/"+website_to_analyze)

if result.status_code != 200:
	print("This domain could not be analyzed, check that it is written correctly. If it is well written, try to do the whois manually. If it works manually, notify me in Github about this problem. Status code received: ", result.status_code)
	exit()

print(result.status_code, result.reason, "Here it comes the get response...")

with open("get_response.html", "w+") as file:
    print(result.text, file=file)

print("Get response finished")

print("Saving website without HTML & JS tags...")

clean_website(result.text)
read_clean_website()

print("Analyzing the received information...")

analyzer.analyze()

os.remove("clean_html.txt")
os.remove("get_response.html")
os.remove("cleaned_website.txt")

exit()