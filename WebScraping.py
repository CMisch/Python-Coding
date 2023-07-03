#U08A1 WebScraping part 1 and 2 of 3
#Write a program to test if a given page is found or not on the server.
#Write a Python program to download and display the content of robots.txt for http://www.capella.edu.


from bs4 import BeautifulSoup as bs
import requests

site = input("Please enter a website: ")
#Get web page
res = requests.get(site)    #requests.get('http://www.capella.edu')
text = res.text
#test if page is found or not on the server
status = res.status_code
#Create a response
if status == 200:
    print("Status: 200\nPage has been found on the server")
else:
    print("Status: 404\nPage has not been found.")

#Download and display content from robots.txt for http://www.capella.edu.
req = requests.get('http://www.capella.edu/robots.txt')
show = req.text
soup = bs(req.content, 'html.parser')
print(soup)

