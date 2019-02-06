import tkinter as tk
from tkinter import ttk
from ohno.ans import *

def Click(event):
	return "break"

def OnEntryDown(event):
	global selection,l
	if selection<l.size()-1:
		l.select_clear(selection)
		selection+=1
		l.select_set(selection)

def OnEntryUp(event):
	global selection
	if selection>0:
		l.select_clear(selection)
		selection-=1
		l.select_set(selection)
	
def Call(event):
	global selection
	global code_list
	global lang_list
	global r
	global root
	r=tk.Toplevel(root)
	r.title(lang_list[selection])
	txt_frm = tk.Frame(r, width=750, height=500)
	txt_frm.pack(fill="both", expand=True)
	txt_frm.grid_propagate(False)
	txt_frm.grid_rowconfigure(0, weight=1)
	txt_frm.grid_columnconfigure(0, weight=1)
	txt = tk.Text(txt_frm,background="black",foreground="white", borderwidth=2, relief="sunken")
	txt.config(font=("Times new roman", 14, "italic"), undo=True, wrap='word')
	txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
	scrollb = tk.Scrollbar(txt_frm, command=txt.yview)
	scrollb.grid(row=0, column=1, sticky='nsew')
	txt['yscrollcommand'] = scrollb.set
	txt.tag_configure("code", foreground="yellow")
	tag='code'
	txt.insert(tk.END,"%s"%code_list[selection],tag)
	txt.insert(tk.END, "\n\n********************************************************************************")
	txt.bind("<Escape>",lambda event:r.destroy())
	txt.bind("q", lambda event:r.destroy())	
	txt.configure(state="disabled")
	txt.focus_set()
	r.mainloop()

def Terminate(event):
	global root
	root.destroy()

def util(ll,cl):
	global lang_list
	lang_list=ll
	global code_list
	code_list=cl
	global root
	global selection
	global l
	global s
	root = tk.Tk()
	txt_frm = tk.Frame(root, width=750, height=500)
	txt_frm.pack(fill="both", expand=True)
	txt_frm.grid_propagate(False)
	txt_frm.grid_rowconfigure(0, weight=1)
	txt_frm.grid_columnconfigure(0, weight=1)
	l =tk.Listbox(txt_frm, selectmode=tk.SINGLE,background="black",foreground="white",selectforeground="red",highlightcolor="white",borderwidth=2, highlightthickness=2,font=('Verdana', '10', 'bold italic'), height=25,width=100)
	l.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
	s = ttk.Scrollbar(txt_frm, orient=tk.VERTICAL, command=l.yview)
	s.grid(column=1, row=0, sticky=(tk.N,tk.S))
	l['yscrollcommand'] = s.set
	selection = 0
	for i in range(len(lang_list)):
		l.insert('end', r'%d.    %s' %(i+1,lang_list[i]))
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
