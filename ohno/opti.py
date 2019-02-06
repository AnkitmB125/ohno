import requests
import re
from bs4 import BeautifulSoup
from ohno.gui2 import *
GREEN = '\033[92m'
GRAY = '\033[90m'
CYAN = '\033[36m'
RED = '\033[31m'
YELLOW = '\033[33m'
END = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
def answer_scrap_gfg(url):
	page=requests.get(url)
	html_doc=page.text
	soup=BeautifulSoup(html_doc,"lxml")
	new_soup=soup.find("a",href=re.compile("geeksforgeeks.org"))
	if new_soup==None:
		print(YELLOW + BOLD + "No result found" + END, end=' ')
		print()
		return
	new_soup=new_soup['href']
	new_soup=new_soup[new_soup.find("q=")+2:]
	new_soup=new_soup[:new_soup.find("&")]
	page_ans=requests.get(new_soup)
	html_doc_ans=page_ans.text
	soup_ans_all=BeautifulSoup(html_doc_ans,"lxml")
	all_methods=soup_ans_all.find_all("div",class_="responsive-tabs")
	length=len(all_methods)
	soup_ans=all_methods[length-1]
	all_codes=soup_ans.find_all("td",class_="code")
	language_tags=soup_ans.find_all("h2",class_="tabtitle")

	languages=[]
	codes=[]

	for tags in language_tags:
		languages.append(tags.text)

	for current_code in all_codes:
		codes.append(current_code.get_text())

	#print(len(languages))
	util(languages,codes)

# answer_scrap_gfg("https://www.google.com/search?q=fibonacci+gfg")
