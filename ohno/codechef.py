from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import re
from bs4 import BeautifulSoup
import sys
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException 
from pyvirtualdisplay import Display
import getpass

def codechef():
	
	display = Display(visible=0, size=(800, 600))
	display.start()
	def check_exists_by_tag_name(scope_to_search,tag):
	    try:
	        scope_to_search.find_element_by_tag_name(tag)
	    except NoSuchElementException:
	        return False
	    return True
	driver=webdriver.Firefox()

	def get_lang_for_submission(File_Path):
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
	def codechef_login(user,passw):
		username=driver.find_element_by_id("edit-name")
		username.send_keys(user)
		password=driver.find_element_by_id("edit-pass")
		password.send_keys(passw)
		submit=driver.find_element_by_id("edit-submit")
		submit.click()
		url=driver.current_url
		if url=="https://www.codechef.com/session/limit":
			box=driver.find_elements_by_xpath("//input[@type='checkbox']")
			for check in box:
				check.click()
			box[len(box)-1].click()
			submit_session=driver.find_element_by_id("edit-submit")
			submit_session.click()
		

		language_choice=get_lang_for_submission(sys.argv[2])
		option_value=""
		if language_choice == "cpp":
			option_value = "44" 
		elif language_choice == "java":
			option_value = "10"
		elif language_choice == "python3":
			option_value = "116"
		elif language_choice == "c":
			option_value = "11"
		elif language_choice == "rhino":
			option_value = "35"
		else:
			option_value = None
		code_script=open(sys.argv[2],'r')
		code_script=code_script.read()
		time.sleep(5)
		text_area=driver.find_element_by_id("edit-program")
		text_area.send_keys(code_script)
		select=Select(driver.find_element_by_id("edit-language"))
		select.select_by_value(option_value)
		# langauge_button=driver.find_element_by_xpath("//select[@name='language']")
		# driver.execute_script("arguments[0].click();",langauge_button)
		# language_choose=driver.find_element_by_xpath("//select[@name='language']/option[text()='C++14(gcc 6.3)']")
		# language_choose=driver.find_element_by_xpath("//select[@name='language']/option[@value='"+option_value+"']")
		# driver.execute_script("arguments[0].click();",language_choose)
		code_submit=driver.find_element_by_id("edit-submit-1")
		driver.execute_script("arguments[0].click();",code_submit)
		time.sleep(4)
		while True:
			result=driver.find_element_by_id("display_result")
			if check_exists_by_tag_name(result,"strong")==False:
				time.sleep(4)
			else:
				result_has_come=result.find_element_by_tag_name("strong")
				print (result_has_come.text)																																																																																																																																																																									
				break


	GREEN = '\033[92m'
	GRAY = '\033[90m'
	CYAN = '\033[36m'
	RED = '\033[31m'
	YELLOW = '\033[33m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	BOLD = '\033[1m'
	print(RED + BOLD + "Contest[Y/N]" + END, end=' ')
	choice=input()
	contest_id=""
	if choice[0]=="Y":
		print(YELLOW + BOLD + "Enter contest_id" + END, end=' ')
		contest_id=input()
	codechef_link="https://www.codechef.com/"
	if contest_id!="":
		codechef_link=codechef_link+contest_id+"/submit/"
	else:
		codechef_link=codechef_link+"submit/"
	print(RED + BOLD + "Enter question id:" + END, end=' ')
	question_id=input()
	print(GRAY + BOLD + "Enter your username:" + END, end=' ')
	user=input()
	# print(CYAN + BOLD + "Enter your password:" + END, end=' ')
	# passw=input()
	passw = getpass.getpass(RED + BOLD + "Enter your password: " + END)
	codechef_link=codechef_link+question_id
	driver.get(codechef_link)
	codechef_login(user,passw)
	display.stop()

# codechef()