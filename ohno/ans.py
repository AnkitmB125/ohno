import requests
import os
import subprocess
import re
import sys
from bs4 import BeautifulSoup
import urllib
from ohno.gui import *
import tkinter as tk
from tkinter import ttk

def answer_scrap(url):
	url="https://stackoverflow.com"+url
	page=requests.get(url)
	html_doc=page.text
	soup=BeautifulSoup(html_doc,'lxml')
	all_answer=soup.find_all('div',class_="post-text")
	upvote_soup=soup.find_all('div',{'itemprop':'upvoteCount'})
	upvote_count_first_q_then_ans=[]
	for upvote in upvote_soup:
		upvote_count_first_q_then_ans.append(upvote.text)
	i=0
	all_answer_tuple=[]
	for answer in all_answer:
		all_answer_tuple_sublist=[]
		for child in answer.recursiveChildGenerator():
			name=getattr(child,"name",None)
			if name is None:#leaf node check
				all_answer_tuple_sublist.append((child.parent.name,child))
		all_answer_tuple.append(all_answer_tuple_sublist)
		i=i+1
	# print(all_answer_tuple)
	return all_answer_tuple,upvote_count_first_q_then_ans