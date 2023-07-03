#U08A1 WebScraping part 1 and 2 of 3
#Write a program to test if a given page is found or not on the server.
#Write a Python program to download and display the content of target


from bs4 import BeautifulSoup as bs
import requests

site = input("Please enter a website: ")
#Get web page
res = requests.get(site)
text = res.text
#test if page is found or not on the server
status = res.status_code
#Create a response
if status == 200:
    print("Status: 200\nPage has been found on the server")
else:
    print("Status: 404\nPage has not been found.")

#Download and display content 
req = requests.get('http://') #add your target address
show = req.text
soup = bs(req.content, 'html.parser')
print(soup)

