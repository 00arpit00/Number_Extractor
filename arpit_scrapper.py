import re,tkinter

window=tkinter.Tk()
window.title("Number Extractor")
window.geometry("400x200+200+200")
lb1=tkinter.Label(window,text="Enter File Name->")
lb1.grid(row=0)
e=tkinter.Entry(window)
e.grid(row=0,column=1)
file_count=1 # to generate different name to the processed files
def take_input():
	global e,file_count
	count={}   # to avoid duplicate numbers
	open_or_not=0 # whether input file open or not
	
	try:
		file=open(e.get(),'r')
		open_or_not=1
		lb3=tkinter.Label(window,text="Output File Generated")
		lb3.grid(row=4,column=1)
	except:
		lb2=tkinter.Label(window,text="   No such File Exist   ")
		lb2.grid(row=4,column=1)
	if open_or_not:
		opt=open('arpit_processed'+str(file_count)+'.txt','w')
		file_count+=1
		for line in file:
			list_each_line=re.findall(r'(?:\+91|)[789]{1}[0-9]{9}[0-9]*',line)  # regular expression for Indian phone number starting with 7 or 8 or 9
			if list_each_line==[]:
				pass
			else:
				for num in list_each_line:
					if (num[0]=='+' and len(num)==13) or len(num)==10:
						num=num[-10:]
					else:
						continue
					if num not in count:
						count[num]=1

						
					else:
						count[num]+=1
		for num in count.keys():
			opt.write(num+' occurs '+str(count[num])+' times.\n')
btn1=tkinter.Button(window,text='Submit',width=10,command=take_input)
btn1.place(x=10,y=80)
btn2=tkinter.Button(window,text="Exit",width=6,command=exit)
btn2.place(x=300,y=80)


window.mainloop()
