import os
import subprocess
import re
import sys
import requests
from bs4 import BeautifulSoup
import urllib
from ohno.gui import *
import tkinter as tk
from tkinter import ttk
import json


GREEN = '\033[92m'
GRAY = '\033[90m'
CYAN = '\033[36m'
RED = '\033[31m'
YELLOW = '\033[33m'
END = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

def confirm():
	option = {"yes": True, "y": True, "no": False, "n": False, "": True}

	while True:
		print(BOLD + YELLOW + "\nDo you want to search StackOverflow? [Y/N]   " + END, end='')
		choice = input().lower()
		if choice in option:
			return option[choice]

		print("Please respond with ('yes' or 'no') or ('y' or 'n').\n")

# returns compiler
def get_lang(File_Path):
	if File_Path.endswith(".py"):
		return "python3 "
	elif File_Path.endswith(".cpp"):
		return "g++ "
	elif File_Path.endswith(".java"):	
		return "javac "
	elif File_Path.endswith(".c"):
		return "gcc "
	elif File_Path.endswith(".js"):
		return "rhino "
	else: 
		return None 		
		
# prints help
def print_help():
	print("%sNAME%s\n\tOhno\n"%(BOLD,END))
	print("%sSYNOPSIS%s\n\t%sohno%s %s[%sfile_name]%s\n" % (BOLD, END,BOLD, END, YELLOW,UNDERLINE,END))
	print("\t%sohno%s -q %s[%scustom_query]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s --query %s[%scustom_query]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s -g %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s --gfg %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s -s %s[%scode_file]%s %s[%sinput_file]%s\n"%(BOLD, END, YELLOW,UNDERLINE, END, YELLOW, UNDERLINE,END) )
	print("\t%sohno%s --submit %s[%scode_file]%s %s[%sinput_file]%s\n"%(BOLD, END, YELLOW,UNDERLINE, END, YELLOW, UNDERLINE,END) )
	# print("\t%sohno%s -c %s%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	# print("\t%sohno%s --calender %s%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("%sDESCRIPTION%s\n\t\n"%(BOLD,END))

def cprint_help():
	print("%sNAME%s\n\tcprog\n"%(BOLD,END))
	print("\t%sohno%s -c %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s --codechef %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s -s %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("\t%sohno%s --spoj %s[%scode_name]%s\n"%(BOLD, END, YELLOW,UNDERLINE,END) )
	print("%sDESCRIPTION%s\n\t\n"%(BOLD,END))


def error_on_python(error):
	list_err = []
	if any(err in error for err in["KeyboardInterrupt", "SystemExit", "GeneratorExit"]):
		return None
	else:
		list_err.append(error.split('\n')[-2].strip())
		return list_err

def error_on_java(error):
	list_err = []
	length = len(error.split('\n'))
	for i in range(length):
		m = re.search(r'.*error:(.*)', error.split('\n')[i])
		if m:
			list_err.append(m.group(1).strip())
	return list_err

def error_on_cpp(error):
	list_err = []
	length = len(error.split('\n'))
	for i in range(length):
		m = re.search(r".*error:(.*)", error.split('\n')[i])
		if m:
			list_err.append(m.group(1).strip())
	for i in range(len(list_err)):
		list_err[i] = list_err[i][:list_err[i].find("(")]
		list_err[i] = list_err[i][:list_err[i].find("{")]
		list_err[i] = list_err[i][:list_err[i].find("[")]
	return list_err

def error_on_c(error):
	list_err = []
	length = len(error.split('\n'))
	for i in range(length):
		m = re.search(r".*error:(.*)", error.split('\n')[i])
		if m:
			list_err.append(m.group(1).strip())
	for i in range(length):
		m = re.search(r".*warning:(.*)", error.split('\n')[i])
		if m:
			list_err.append(m.group(1).strip())
	for i in range(len(list_err)):
		list_err[i] = list_err[i][:list_err[i].find("(")]
		list_err[i] = list_err[i][:list_err[i].find("{")]
		list_err[i] = list_err[i][:list_err[i].find("[")]
	return list_err

def error_on_js(error):
	list_err = []
	list_err.append(error.split('\n')[0][4:].strip())
	for i in range(len(list_err)):
		list_err[i] = list_err[i][:list_err[i].find("(")]
		list_err[i] = list_err[i][:list_err[i].find(":")+2]
		list_err[i] = list_err[i][:list_err[i].find("{")]
		list_err[i] = list_err[i][:list_err[i].find("[")]
	return list_err

def get_error(error, language):
	if error == "":
		return None
	elif language == "python3 ":
		return error_on_python(error)
	elif language == "javac ":
		return error_on_java(error)
	elif language == "g++ ":
		return error_on_cpp(error)
	elif language == "gcc ":
		return error_on_c(error)
	elif language == "rhino ":
		return error_on_js(error)
	else:
		return None

def execute(command):
	sp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err=sp.communicate()
	return (out.decode('utf-8'), err.decode('utf-8'))

def scrap(errors_list):
	global stack_questions_list
	stack_questions_list = []
	for error in errors_list:
		params = {"q": error}
		error_next = urllib.parse.urlencode(params)
		url="https://stackoverflow.com/search?pagesize=3&"+error_next
		page=requests.get(url)
		html_doc=page.text
		soup=BeautifulSoup(html_doc,'lxml')
		all_a_tags_questions=soup.find_all('a',class_="question-hyperlink")
		all_stats_tags_for_answer=soup.find_all('div',class_=["c","status"])
		i=0
		for question in all_a_tags_questions:
			if i>=10:
				break
			stack_questions_list.append([(question.text).strip(),question['href']])
			i=i+1
		i=0
		for each_strong in all_stats_tags_for_answer:
			if i>=10:
				break
			each_strong.find('strong')
			stack_questions_list[i].append((each_strong.text).strip())
			i=i+1
	util(stack_questions_list)


def get_lang_for_exec(File_Path):
	if File_Path.endswith(".py"):
		return "python3"
	elif File_Path.endswith(".cpp"):
		return "cpp"
	elif File_Path.endswith(".java"):	
		return "java"
	elif File_Path.endswith(".c"):
		return "c"
	elif File_Path.endswith(".php"):
		return "php"
	elif File_Path.endswith(".pl"):
		return "perl"
	elif File_Path.endswith(".rb"):
		return "ruby"
	elif File_Path.endswith(".go"):
		return "go"
	elif File_Path.endswith(".sh"):
		return "bash"
	elif File_Path.endswith(".sql"):
		return "sql"
	elif File_Path.endswith(".pas"):
		return "pascal"
	elif File_Path.endswith(".cs"):
		return "csharp"
	elif File_Path.endswith(".r"):
		return "r"
	elif File_Path.endswith(".js"):
		return "rhino"
	elif File_Path.endswith(".m"):
		return "octave"
	elif File_Path.endswith(".coffee"):
		return "coffeescript"
	elif File_Path.endswith(".b"):
		return "brainfuck"
	elif File_Path.endswith(".swift"):
		return "swift"
	elif File_Path.endswith(".lua"):
		return "lua"
	elif File_Path.endswith(".kt"):
		return "kotlin"
	else: 
		return None

def submit():
	clientId = "ac41af890db3dff65bb5278e2b7880f"
	clientSecret = "5b9748536e29f2c9e360e82fa2b59865f4d6540eea17ffe5401c58bf3923de5c"
	script = open(sys.argv[2], 'r').read()
	stdin = ""
	if len(sys.argv) > 3:  # change when -s is introduced
		stdin = open(sys.argv[3], 'r').read()	
	language = get_lang_for_exec(sys.argv[2])
	versionIndex = "2"
	if language == "brainfuck" or language == "rhino":
		versionIndex = "0"
	if language == "kotlin" or language == "lua":
		versionIndex = "1"
	# print(stdin)

	''' To check credits spent '''
	# credit = {"clientId": clientId,"clientSecret": clientSecret}
	# check_credits = requests.post(url = "https://api.jdoodle.com/v1/credit-spent", json=credit)
	# print(check_credits.text)


	data = {"clientId": clientId,"clientSecret": clientSecret,"script":script,"stdin":stdin,"language":language,"versionIndex":versionIndex}
	req = requests.post(url = "https://api.jdoodle.com/v1/execute", json=data)
	# print(req.text)
	answer = json.loads(req.text)
	error = False
	if answer["memory"] == None and answer["cpuTime"] == None:
		error = True
	if error == False:
		print(answer["output"])
		print("\nMemory used: "+ GREEN + BOLD + answer["memory"] + END)
		print("\nCPU Time: "+ GREEN + BOLD + answer["cpuTime"] + END)
	else:
		if answer["output"] == "\n\n\n JDoodle - Timeout \nIf your program reads input, please enter the inputs in STDIN box above or try enable \"Interactive\" mode option above.\nPlease check your program has any endless loop. \nContact JDoodle support at jdoodle@nutpan.com for more information.":
			print(RED + BOLD + "Please input the STDIN file as an argument!" + END)
		else:	
			if language == "python3":
				language = "python3 "
			elif language == "java":
				language = "javac "
			elif language == "cpp":
				language = "g++ "
			elif language == "c":
				language = "gcc "
			elif language == "rhino":
				language = "rhino "
			else:
				language = None


			if language == None:
				print(CYAN + BOLD + "Currently search on stackoverflow is available only for C, C++, Java, Python and JavaScript!!!")
			else:
				print(answer["output"])
				err = answer["output"]
				all_error = []
				if confirm():
					all_error.append(get_error(err, language))
					scrap(all_error[0])

			
			
