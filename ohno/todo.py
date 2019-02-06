import tkinter as tk
from tkinter import ttk
import os
import ohno.stat

file_todo='.file1.txt'
SD_count='.file2.txt'
prev_str=''

def append_to_do(task):
	global prev_str
	if prev_str == task:
		pass
	else:
		prev_str=task		
		task=task + '\n'
		file1 = open('to_do_list.txt', 'a+')
		file1.write(task)
		file1.close()

def delete_to_do(task):

	file2=open('to_do_list.txt','r')
	lines=file2.readlines()
	file2.close()
	file2=open('to_do_list.txt','w+')
	for line in lines:
		if line!=task:
			file2.write(line)
	file2.close()

def get_to_do_list_from_file():
	try:
		file3=open('to_do_list.txt','r')
	except:
		pass
	else:	
		file3=open('to_do_list.txt','r')
		list_fetch=file3.readlines()
		return list_fetch

def Click(event):
	return "break"

def Start(c,p):
	global r1
	global file_todo
	global SD_count
	try:
		fptr1=open(file_todo,"r")
	except:
		fptr1=open(file_todo,"w")
		fptr1.write(p)
		fptr1.close()			
		fptr2=open(SD_count,"w")
		fptr2.write(str(c)+ " " +str(0)+ " "+str(1))
		fptr2.close()
		pth = ohno.stat.__file__
		os.system('python3 '+pth)
		#ohno.stat.entry()
	else:
		pass
	r1.destroy()

def End(c,p):
	global r1
	global file_todo
	global SD_count
	try:
		fptr1=open(file_todo,"r")
	except:
		pass
	else:
		fptr1=open(file_todo,"r")
		fptr2=open(SD_count,"r")
		ltext=fptr1.read()
		rtext=fptr2.read()
		lc=rtext.split(" ")
		if int(lc[0])==c:
			delete_to_do(p)
			#print('Going to kill')
			pth = ohno.stat.__file__
			os.system('python3 '+pth)
			#ohno.stat.entry()
		else:
			#print(c,'Unable to kill')
			pass
	r1.destroy()
	
def OnEntryDown(event):
	global selection,l
	if selection<l.size()-2:
		l.select_clear(selection)
		selection+=2
		l.select_set(selection)
		l.activate(selection-1)

def OnEntryUp(event):
	global selection
	if selection>0:
		l.select_clear(selection)
		selection-=2
		l.select_set(selection)
		l.activate(selection+1)

def View_entry():
	global root
	global r1
	#lst=["Kanpsack","DSU","DFS","BFS","Bit Masking"]
	lst=get_to_do_list_from_file()
	r1=tk.Toplevel(root)
	#r.geometry("200x200")
	#r.configure(background='white',borderwidth=10)
	r1.columnconfigure(0, weight=1)
	if lst == None:
		pass
	else:
		for i in range(0,len(lst)):																			
			lbl=tk.Label(r1,text=lst[i],foreground='red',background='yellow',font=('Verdana', '10' , 'bold italic'),borderwidth=5).grid(row=2*i,column=0,sticky='ew',columnspan=2)		
			b1=tk.Button(r1,text='Start',background='cyan',font=('Verdana', '10', 'bold italic'),command=lambda c=i:Start(c,lst[c])).grid(row=2*i+1,column=0,padx=5,pady=5)
			b2=tk.Button(r1,text='Done',background='cyan',font=('Verdana', '10', 'bold italic'),command=lambda c=i:End(c,lst[c])).grid(row=2*i+1,column=1,padx=5,pady=5)	


	r1.bind("<Escape>",lambda event:r1.destroy())
	r1.bind("q", lambda event:r1.destroy())	

def Add_entry():
	global root
	r=tk.Toplevel(root)
	r.geometry("530x100")
	r.configure(background='white')
	lbl=tk.Label(r,text="Objective : ",foreground='red',background='white',font=('Verdana', '10', 'bold italic'),borderwidth=10)
	lbl.grid(row=0)	
	todo=tk.StringVar()
	e=tk.Entry(r,textvariable=todo,background='white',width=50)
	e.grid(row=0,column=1)	
	b1=tk.Button(r,text='Submit',background='cyan',font=('Verdana', '10', 'bold italic'),command=lambda:append_to_do(todo.get())).grid(columnspan=4,pady=20)
	r.bind("<Escape>",lambda event:r.destroy())
	r.bind("q", lambda event:r.destroy())	
	r.mainloop()

def Call(event):
	global selection
	i = selection//2
	if i==0:
		Add_entry()
	else:
		View_entry()

def Terminate(event):
	global root
	root.destroy()

def util_todo():
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
	l.insert('end', 'Add entry To-Do List')
	l.insert('end', '')
	l.insert('end', 'View To-Do List')
	l.bind("<Down>", OnEntryDown)
	l.bind("<Up>", OnEntryUp)
	l.bind("<Return>",Call)
	l.bind("<Escape>", Terminate)
	l.bind("q", Terminate)
	l.bind("<ButtonPress-1>",Click)
	l.bind("<ButtonRelease-1>",Click)
	l.select_set(0)
	l.focus_set()
	l.activate(0)
	root.mainloop()


