import tkinter as tk
from tkinter import ttk
from ohno.ans import *

#from pynput.mouse import Button,Controller
def tabify(s):
	if s.endswith('answers'):
		l=s.replace('answers',' answers')
	else:
		l=s.replace('answer',' answer')
	a="  "+l
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
		selection+=2
		l.select_set(selection)
		l.activate(selection-1)
	#else:
	#	l.activate(selection-1)
def OnEntryUp(event):
	global selection
	if selection>0:
		l.select_clear(selection)
		selection-=2
		l.select_set(selection)
		l.activate(selection+1)

def print_answer_in_new_window(all_answer_tuple, upvotes):
	global global_stack_questions
	global selection
	global r
	global root
	r=tk.Toplevel(root)
	r.title(global_stack_questions[selection//2][0])
	txt_frm = tk.Frame(r, width=750, height=500)
	txt_frm.pack(fill="both", expand=True)
	# ensure a consistent GUI size
	txt_frm.grid_propagate(False)
	# implement stretchability
	txt_frm.grid_rowconfigure(0, weight=1)
	txt_frm.grid_columnconfigure(0, weight=1)

	# create a Text widget
	txt = tk.Text(txt_frm,background="black",foreground="white", borderwidth=2, relief="sunken")
	txt.config(font=("Times new roman", 14, "italic"), undo=True, wrap='word')
	txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

	# create a Scrollbar and associate it with txt
	scrollb = tk.Scrollbar(txt_frm, command=txt.yview)
	scrollb.grid(row=0, column=1, sticky='nsew')
	txt['yscrollcommand'] = scrollb.set
	txt.tag_configure("text", foreground="cyan")
	txt.tag_configure("code", foreground="yellow")
	txt.tag_configure("up", foreground="gold")
	txt.tag_configure("acode", foreground="papaya whip")
	txt.tag_configure("atext", foreground="green yellow")
	txt.tag_configure("aup", foreground="aquamarine2")
	for j in range(len(all_answer_tuple[0])):
		if all_answer_tuple[0][j][0].endswith("div"):
			txt.insert(tk.END,"\n")
		elif all_answer_tuple[0][j][0].endswith("code"):
			tag="code"
			txt.insert(tk.END,"%s"%(all_answer_tuple[0][j][1]),tag)
		else:
			tag="text"
			txt.insert(tk.END,"%s"%(all_answer_tuple[0][j][1]),tag)
	tag="up"
	txt.insert(tk.END, "\n\t\t\t\t\t\t\t\t\t%s votes\n\n" %(upvotes[0]),tag)
	txt.insert(tk.END, "********************************************************************************\n\n")


	for i in range(1, len(all_answer_tuple)):
		for j in range(len(all_answer_tuple[i])):
			if all_answer_tuple[i][j][0].endswith("div"):
				txt.insert(tk.END,"\n")
			elif all_answer_tuple[i][j][0].endswith("code"):
				tag="acode"
				txt.insert(tk.END, "%s" %(all_answer_tuple[i][j][1]),tag)
			else:
				tag="atext"
				txt.insert(tk.END, "%s"%(all_answer_tuple[i][j][1]),tag)
		tag="aup"
		txt.insert(tk.END, "\n\t\t\t\t\t\t\t\t\t%s votes\n\n"%(upvotes[i]),tag)
		txt.insert(tk.END, "------------------------------------------------------------------------------------------------------------------------\n")



	txt.bind("<Escape>",lambda event:r.destroy())
	txt.bind("q", lambda event:r.destroy())	
	txt.configure(state="disabled")
	txt.focus_set()
	r.mainloop()

def Call(event):
	global selection
	global global_stack_questions
	i = selection//2
	all_answer_tuple, upvotes = answer_scrap(global_stack_questions[i][1])
	print_answer_in_new_window(all_answer_tuple, upvotes)
	# r=tk.Tk()
	# t=tk.Listbox(r,height=25,width=100)
	# t.grid(column=0,row=0,sticky=(tk.N,tk.W,tk.E,tk.S))
	# p=ttk.Scrollbar(r,orient=tk.VERTICAL,command=t.yview)
	# p.grid(column=1, row=0, sticky=(tk.N,tk.S))
	# t['yscrollcommand']=s.set
	# t.insert(tk.END,"Hii How are you %d"%(selection))
	# r.mainloop()

def Terminate(event):
	global root
	root.destroy()

def util(stack_questions_list):
	global global_stack_questions
	global_stack_questions = stack_questions_list
	global root
	global selection
	global l
	global s
	root = tk.Tk()
	l =tk.Listbox(root, selectmode=tk.SINGLE,background="black",foreground="white",selectforeground="red",highlightcolor="white",borderwidth=2, highlightthickness=2,font=('Verdana', '10', 'bold italic'), height=25,width=100)
	l.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
	s = ttk.Scrollbar(root, orient=tk.VERTICAL, command=l.yview)
	s.grid(column=1, row=0, sticky=(tk.N,tk.S))
	l['yscrollcommand'] = s.set
	#mouse = Controller()
	#mouse.position()
	#ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
	#root.grid_columnconfigure(0, weight=1)
	#root.grid_rowconfigure(0, weight=1)
	selection = 0
	for i in range(len(global_stack_questions)):
		l.insert('end', '%s' %(stack_questions_list[i][0]))
		l.insert('end', tabify(stack_questions_list[i][2]))
	#l.select_set(0)
	#l.grid(row=1,column=0,sticky=(tk.S,tk.W))
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
	#l.get(ACTIVE)
	root.mainloop()
	#master, selectmode=tk.SINGLE, height = 3, exportselection=0)
