#find people information
import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
query = input("Enter query to search ")
webbrowser.open('https://memebase.cheezburger.com/search#'+query)
webbrowser.open('https://me.me/s/'+query)
webbrowser.open('https://giphy.com/search/'+query)
webbrowser.open('https://www.tumblr.com/tv/'+query)
webbrowser.open('https://memegenerator.net/search?q='+query)
webbrowser.open('https://www.reddit.com/r/memes/search?q='+query)
webbrowser.open('https://imgur.com/search?q='+query)
webbrowser.open('https://frinkiac.com/?q='+query)
