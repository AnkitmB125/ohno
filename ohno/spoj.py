from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import sys
import time
import requests
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import getpass


def spoj():
	print("hi")
	display = Display(visible=0, size=(800, 600))
	display.start()


	GREEN = '\033[92m'
	GRAY = '\033[90m'
	CYAN = '\033[36m'
	RED = '\033[31m'
	YELLOW = '\033[33m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	BOLD = '\033[1m'

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

	code_script = open(sys.argv[2], 'r') # change argv accroding to argument inputs
	# print(code_script.read())
	code_script = code_script.read()
	language = get_lang_for_submission(sys.argv[2])
	# quit()

	print(YELLOW + BOLD + "Enter your SPOJ username:" + END, end=' ')
	username = input()
	# username = "ankit_125"
	password = getpass.getpass(RED + BOLD + "Enter your SPOJ password: " + END)
	# password = "fsociety343"
	print(CYAN + BOLD + "ENTER PROBLEM CODE: " + END, end='')
	code_id = input()
	# code_id = "PRIME1"

	firefoxProfile = FirefoxProfile()
	firefoxProfile.set_preference('permissions.default.stylesheet', 2)
	firefoxProfile.set_preference('permissions.default.image', 2)
	firefoxProfile.set_preference('javascript.enabled', False)
	firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
	driver = webdriver.Firefox(firefoxProfile)
	# driver.get("https://google.com")

	# WebDriverWait(driver, 3).until(EC.alert_is_present())
	# driver1 = driver.switch_to.alert
	# time.sleep(2)
	# driver1.send_keys("edcguest" + Keys.TAB + "edcguest")
	# time.sleep(2)
	# driver1.accept()
	driver.get("https://www.spoj.com/login")
	box=driver.find_element_by_id("inputUsername")
	box.send_keys(username)
	box=driver.find_element_by_id("inputPassword")
	box.send_keys(password)
	box=driver.find_elements_by_xpath("//button[@type='submit'][@class='btn btn-primary']")
	# print(len(box))
	# box=driver.find_element_by_id("edit-submit")
	box[0].click()
	url=driver.current_url
	# print(url)

	# print(code_id)
	# code_id = "PRIME1"
	driver.get("https://www.spoj.com/submit/" + code_id)
	code_input = driver.find_element_by_id("subm_file")
	code_input.send_keys(os.getcwd()+"/"+sys.argv[2])

	lang=""
	if language == "cpp":
		lang = "C++14 (gcc 6.3)"
	elif language == "java":
		lang = "JAR (JavaSE 6)"
	elif language == "python3":
		lang = "Python 3 (python  3.5)"
	elif language == "c":
		lang = "C (gcc 6.3)"
	elif language == "rhino":
		lang = "JavaScript (rhino 1.7.7)"
	else:
		lang = None

	time.sleep(1)
	driver.find_element_by_xpath("//select[@name='lang']/option[text()='"+ lang +"']").click()
	# submit_code=driver.find_elements_by_name("submit")
	time.sleep(2)
	button = driver.find_elements_by_xpath("//input[@type='submit']")

	time.sleep(1)

	# button[0].click()
	driver.execute_script("arguments[0].click();", button[0])

	time.sleep(1)
	print(GREEN + BOLD + "\nSolution Submitted Successfully..." + END)

	# submission page scrapping starts here
	while True:
		time.sleep(2)
		url = "https://www.spoj.com/status/" + username
		page = requests.get(url)
		html_doc = page.text
		soup = BeautifulSoup(html_doc, 'lxml')

		problem = soup.find('td', class_='sproblem')
		# print(problem.text)


		status = soup.find('td', class_='statusres')

		solution = status.text
		solution = solution.strip()
		# print(solution)
		if solution == "accepted":
			break
		elif not (solution == "waiting.." or solution == "compiling.." or solution[:8] == "running" or solution[:7] == "running" or solution[:6] == "running"):
			break

	print()
	if solution == "accepted":
		print(BOLD + GREEN + solution + END)
	else:
		print(BOLD + RED + solution + END)
	print(BOLD + YELLOW + problem.text + END)

	display.stop()

# spoj()