import requests
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from urllib.parse import quote
import tkinter as tk
from tkinter import ttk
import webbrowser

GREEN = '\033[92m'
GRAY = '\033[90m'
CYAN = '\033[36m'
RED = '\033[31m'
YELLOW = '\033[33m'
END = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

def tabify(tple):
	a = "  Platform: "  + tple[1]  + " ,Start Time: " + tple[2]  +" ,End Time: " + tple[3] + " ,Duration: " + tple[4]	
	#print(a)	
	return a

def Click(event):
	return "break"

def Terminate2(event):
	global r
	r.destroy()

def OnEntryDown(event):
	global selection,l
	if selection<l.size()-2:
		l.select_clear(selection)
		selection+=3
		l.select_set(selection)
		l.activate(selection-1)

def OnEntryUp(event):
	global selection
	if selection>0:
		l.select_clear(selection)
		selection-=3
		l.select_set(selection)
		l.activate(selection+1)


def Call(event):
	global selection
	global event_list
	i = selection//3
	webbrowser.open(event_list[i][5]);

def Terminate(event):
	global root
	root.destroy()

def util(el):
	global event_list
	event_list = el
	global root
	global selection
	global l
	global s
	root = tk.Tk()
	root.title("Coding Calender")
	txt_frm = tk.Frame(root, width=1000, height=500)
	txt_frm.pack(fill="both", expand=True)
	txt_frm.grid_propagate(False)
	txt_frm.grid_rowconfigure(0, weight=1)
	txt_frm.grid_columnconfigure(0, weight=1)



	l =tk.Listbox(txt_frm, selectmode=tk.SINGLE,background="black",foreground="white",selectforeground="red",highlightcolor="white",borderwidth=2, highlightthickness=2,font=('Verdana', '10', 'bold'), height=25,width=100)
	l.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
	s = ttk.Scrollbar(txt_frm, orient=tk.VERTICAL, command=l.yview)
	s.grid(column=1, row=0, sticky=(tk.N,tk.S))
	l['yscrollcommand'] = s.set
	selection = 0
	for i in range(len(event_list)):
		l.insert('end', '%d. %s' %(i+1,event_list[i][0]))
		l.insert('end', r'%s'%(tabify(event_list[i])))
		l.insert('end', r'')
		l.itemconfig(3*i+1, fg='cyan')

	l.bind("<Down>", OnEntryDown)
	l.bind("<Up>", OnEntryUp)
	l.bind("<Return>",Call)
	l.bind("<ButtonPress-1>",Click)
	l.bind("<ButtonRelease-1>",Click)
	l.bind("<Escape>", Terminate)
	l.bind("q", Terminate)
	l.select_set(0)
	l.focus_set()
	l.activate(0)
	root.mainloop()


# util([('Lunch Time','CodeChef','123123','123123','2131231','https://www.codechef.com/')])

def iso_format(dt):
	try:
		utc = dt + dt.utcoffset()
	except TypeError as e:
		utc = dt
		isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
	return isostring.format(int(round(utc.microsecond/1000.0)))


def GetTime(sec):
    sec = timedelta(seconds=sec)
    d = datetime(1,1,1) + sec
    ans = ("%d:%d" % (d.hour, d.minute))
    return ans

def calender():
	api_key = "9ecde431b1d60f1a5c592d9a0a0afce57438ed91"
	username = "abhadage"

	date_today = datetime.today()
	date_after_two_months = date_today + relativedelta(months=3)
	curr_date = (date_today)
	end_date = (date_after_two_months)
	curr_date = quote(iso_format(curr_date))
	end_date = quote(iso_format(end_date))
	# print(quote(iso_format(curr_date)))
	# print(quote(iso_format(end_date)))
	# quit()

	req = requests.get(url="https://clist.by/api/v1/contest/?username="+username+"&api_key="+api_key+"&format=json&start__gt="+curr_date+"&end__lt="+end_date)
	answer = json.loads(req.text)

	send_list_to_gui = []

	for ans in answer["objects"]:
		if ans["resource"]["id"] == 1 or ans["resource"]["id"] == 2 or ans["resource"]["id"] == 35 or ans["resource"]["id"] == 73 or ans["resource"]["id"] == 12:
			duration = GetTime(ans["duration"])
			# duration = duration/3600
			event = ans["event"]
			end_time = ans["end"]
			start_time = ans["start"]
			href = ans["href"]
			name = ans["resource"]["name"]
			send_list_to_gui.append((event, name, start_time, end_time, duration, href))

	util(send_list_to_gui)
