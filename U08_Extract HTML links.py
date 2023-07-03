#U8A1 part 3
#Extract HTML links
#This program will use Beautiful Soup to write a 
# Python program that will extract all of the HTML links from a target

from bs4 import BeautifulSoup as bs
import requests

#Get website using an HTTP client 
url = 'https' #add your own target web address
html = requests.get(url).text

#Use beautiful soup to parse html and create an object
soup = bs(html, 'html.parser' )

#find and print all href tags
for link in soup.find_all('a'):
    http_url = link.get('href')                     #finds all value of href attribute
    if http_url and http_url.startswith('http'):    #finds all values that start with 'http'
       print(http_url)
       
       

