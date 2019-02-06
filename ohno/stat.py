import time
import os
import datetime
import pyxhook
import threading
import signal

if __name__ == "__main__":
	curr_time = time.time()

	keylog_file='.keylog'
	timelog_file='.timelog'

	def decode():
		fd=open('.keylog','r')
		keys=fd.read()
		lis=keys.split()
		print('Number of keystrokes : ')
		print(len(lis))
		count=0
		for i in lis:
			if i=='space':
				count=count+1
		print('Number of words : ')
		print(count)
		os.system('rm .keylog')

	def OnKeyPress(event):
		fob=open(keylog_file,'a')
		fob.write(event.Key)
		fob.write('\n')
		if event.Ascii==96:
			fob.close()
			new_hook.cancel()

	def start_keylogger():
		new_hook=pyxhook.HookManager()
		new_hook.KeyDown=OnKeyPress
		new_hook.HookKeyboard()
		new_hook.start()

	def entry():
		try:
			fptr =open(".timelog" ,"r")
		except:
			pid=os.fork()
			if pid>0:
				#print('Parent Process')
				fptr=open(".timelog","w")
				fptr.write(str(curr_time))
				print("Stopwatch started at " + str(datetime.datetime.now()))		
			else:
				id = os.getpid()
				command = 'echo '+str(id)+' > .pidlog'
				os.system(command)
				start_keylogger()
		else:
			if fptr:
				prev_time=fptr.read()
				prev_time=float(prev_time)
				print("Stopwatch ended at " + str(datetime.datetime.now()))
				print("Worked for ",curr_time-prev_time)
				decode()
				os.remove(".timelog")
				os.remove(".file1.txt")
				os.remove(".file2.txt")
				fptr=open(".pidlog","r")
				pid = fptr.read()
				#print(pid)
				os.system('kill -9 '+ pid)
				#os.killpg(os.getpgid(pid),signal.SIGTERM)
				os.remove('.pidlog')
	entry()