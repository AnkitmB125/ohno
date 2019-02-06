from ohno.gui import *
from ohno.opti import *
from ohno.main import *
from ohno.ans import *
from ohno.calender import *
from ohno.codechef import *
from ohno.spoj import *
from ohno.todo import *

def entry():
	if len(sys.argv) == 1:
		print_help()
		quit()
	if sys.argv[1] == '-h' or sys.argv[1] == '--help':
		print_help()
		quit()

	if sys.argv[1] == '-q' or sys.argv[1] == '--query':
		#send sys.argv[2] to function
		if len(sys.argv) < 3:
			print_help()
			quit()
		else:
			scrap([sys.argv[2]])
			quit()

	if sys.argv[1] == '-s' or sys.argv[1] == '--submit':
		submit()
		quit()

	if sys.argv[1] == '-g' or sys.argv[1] == '--gfg':
		if len(sys.argv) < 3:
			print_help()
			quit()
		else:
			answer_scrap_gfg("https://www.google.com/search?q=" + sys.argv[2] + "+gfg")
			quit()
	if sys.argv[1] == '-c' or sys.argv[1] == '--calender':
		calender()
		quit()


	language = get_lang(sys.argv[1])
	if language == None:
		print(RED + "Language not detected\n" + END)
		print_help()
		quit()

	command = language + sys.argv[1]

	out, err = execute(command)
	if out:
		print(out,end='')
	if err:
		print(err,end='')
	else:
		print(CYAN + BOLD + "\nNo errors detected" + END)
		quit()

	all_error = []

	if confirm():
		all_error.append(get_error(err, language))
		scrap(all_error[0])

def centry():
	if len(sys.argv) == 1:
		cprint_help()
		quit()
	if sys.argv[1] == '-h' or sys.argv[1] == '--help':
		cprint_help()
		quit()

	if sys.argv[1] == '-s' or sys.argv[1] == '--spoj':
		spoj()
		quit()

	if sys.argv[1] == '-c' or sys.argv[1] == '--codechef':
		codechef()
		quit()

def tentry():
	util_todo()