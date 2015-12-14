#Fuck ISIS
 
#We are Anonymous. We are Legion. We do not forgive. We do not forget. Expect us

import requests
from bs4 import BeautifulSoup


data = [line.strip() for line in open("targets.txt",'r')]


def printTweets(username):

    page = requests.get("https://twitter.com/"+username)
    
    soup = BeautifulSoup(page.content, 'html.parser')
#    tweets = soup.find_all('li','js-stream-item')
    x = soup.prettify() 
    x = x.encode('ascii', 'ignore').decode('ascii') 
    print x
#for i in data:
printTweets('mohanad_202012')

