#Build-in Modules imported
import MySQLdb as mdb
from datetime import date
#con = mdb.connect('localhost', 'staffs', 'Shrutisusan26@', 'library')
con = mdb.connect('localhost', 'LibraryStaffs', 'Staffpw', 'library')
import Tkinter as Tk
import ttk
def onbuttonclick(current,prev):
	current.destroy()
	prev.deiconify()

#Registration Students
def registerstudents(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Student Registration")
	label1=Tk.Label(Frame,text="Enter ID number",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter name",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Enter Department",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: registerstudentscode(Frame,frame,p1,p2,p3))
	btn.place(relx=0.35,rely=0.6,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.6,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def registerstudentscode(current,prev,p1,p2,p3):
	with con: 
    		cur = con.cursor()
		ID=p1.get()
		Name=p2.get()
		Department=p3.get()
		print(Name)
		print(Department)
		try:
			if(Name!='' and Department!=''):
			   	cur.execute("INSERT INTO STUDENT VALUES(%s,%s,%s)",(int(ID),Name,Department))
				label4=Tk.Label(current,text="Saved",bg='black', fg='white')
				label4.place(relx=0.45,rely=0.85,relwidth=0.15,relheight=0.1)
			else:
				raise
		except:
			label4=Tk.Label(current,text="Failed",bg='black', fg='white')
			label4.place(relx=0.45,rely=0.85,relwidth=0.15,relheight=0.1)

#Adding Books
def addbooks(frame,root): 
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Books Registration")
	label1=Tk.Label(Frame,text="Enter title of book",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter price",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Enter copies of books available",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
	label4=Tk.Label(Frame,text="Enter author ID (If not available add NULL)",bg='black', fg='white')
	label4.place(relx=0.28,rely=0.58,relwidth=0.45,relheight=0.05)
	label5=Tk.Label(Frame,text="You can modify this info later",bg='black', fg='white')
	label5.place(relx=0.28,rely=0.63,relwidth=0.45,relheight=0.05)
	p4=Tk.StringVar()
	entry4=Tk.Entry(Frame,textvariable=p4)
	entry4.place(relx=0.28,rely=0.68,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addbookscode(Frame,frame,p1,p2,p3,p4))
	btn.place(relx=0.35,rely=0.8,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.8,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def addbookscode(current,prev,p1,p2,p3,p4):
	with con:	    
    		cur = con.cursor()
		Title=p1.get()
		Price=p2.get()
		Count=p3.get()
		AuthorID=p4.get()
		try:
			if(Title!='' and Price!='' and Count!='' and Author!=''):
				if AuthorID=='NULL':
					cur.execute("INSERT INTO BOOKS (Title,Price,Count,A_ID) VALUES(%s,%s,%s,NULL)",(Title,int(Price),int(Count)))   
				else:
				   	cur.execute("INSERT INTO BOOKS (Title,Price,Count,A_ID) VALUES(%s,%s,%s,%s)",
	(Title,int(Price),int(Count),int(AuthorID)))
				label4=Tk.Label(current,text="Saved",bg='black', fg='white')
				label4.place(relx=0.45,rely=0.94,relwidth=0.15,relheight=0.1)
			else:
				raise
		except:
			label4=Tk.Label(current,text="Failed",bg='black', fg='white')
			label4.place(relx=0.45,rely=0.94,relwidth=0.15,relheight=0.1)	
    
 
#Student Display Table**********
def displays(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Students")
	with con:
		cur=con.cursor()
	  	cur.execute("select * from STUDENT")
	  	Label=Tk.Label(Frame,text="View All Students",bg="black",fg="white").pack(side='top')
		cols = ('MIS:ID', 'Name', 'Department')
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
		    listBox.insert("", "end", values=(i[0],i[1],i[2]))
		    m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()
#Replenish book stock
def replenish(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Restock Book")
	label1=Tk.Label(Frame,text="Enter Book code",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter number of copies bought",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Save", command=lambda: replenishcode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.4,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.4,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def replenishcode(current,prev,p1,p2):
	bc=p1.get()
	n=p2.get()
    	with con:
		try:
			if(bc!='' and n!=''):
		    		cur=con.cursor()
		    		cur.execute("select B_ID from BOOKS where B_ID=%s",(bc,))
		    		rows = cur.fetchall()
		    		if(rows):
				  	cur.execute("UPDATE BOOKS SET Count = Count+%s WHERE B_Id = %s ",(n,bc))
					label2=Tk.Label(current,text="Saved",bg='black', fg='white')
					label2.place(relx=0.43,rely=0.6,relwidth=0.15,relheight=0.1)
				else:
					label2=Tk.Label(current,text="Failed! Check Book Code and try again",bg='black', fg='white')
					label2place(relx=0.43,rely=0.6,relwidth=0.15,relheight=0.1)
			else:
				raise
    		except:
			label2=Tk.Label(current,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.43,rely=0.6,relwidth=0.15,relheight=0.1)

#Student Display Table Classwise**********
def displsc(frame,Frame,p1,root):
	Frame.destroy()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Students")
	with con:
		cur=con.cursor()
		c=p1.get()
		cur.execute("select * from STUDENT where Department=%s",(c,))
		Label=Tk.Label(Frame,text="STUDENTS IN A BRANCH ",bg="black",fg="white",bd=5).pack(side='top')
		cols = ('MIS:ID', 'Name', 'Department')
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
		    listBox.insert("", "end", values=(i[0],i[1],i[2]))
		    m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()
def displaysc(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Students")
        Label=Tk.Label(Frame,text="Enter a branch",bg='black', fg='white')
        Label.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
        p1=Tk.StringVar()
        entry=Tk.Entry(Frame,textvariable=p1)
        entry.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Enter", command=lambda: displsc(frame,Frame,p1,root))
        btn.place(relx=0.43,rely=0.3,relwidth=0.15,relheight=0.1)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn.place(relx=0.43,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
        Frame.mainloop()

#Deleting Students
def deletestudents(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Deleting membership")
	label1=Tk.Label(Frame,text="Warning!!! Deleting membership may result in removal of unpaid fines",bg='black', fg='white')
	label1.place(relx=0.10,rely=0.0,relwidth=0.9,relheight=0.05)
	label2=Tk.Label(Frame,text="To continue press Continue or else Exit",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.05)
	btn = Tk.Button(Frame, text="Continue", command=lambda: deletestudents1(Frame,frame,root))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn1 = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn1.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def deletestudents1(Frame,frame,root):
	Frame.withdraw()
	Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        Frame1.geometry("800x800")
        Frame1.title("Deleting membership")
	label1=Tk.Label(Frame1,text="Enter Student ID to delete",bg='black', fg='white')
	label1.place(relx=0.07,rely=0.0,relwidth=0.9,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame1,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame1, text="Delete", command=lambda: deletestudentscode(Frame1,Frame,frame,p1))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
	btn0.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame1.protocol("WM_DELETE_WINDOW", root.destroy)

def deletestudentscode(curr,conf,prev,p1):
    	with con:
	    	cur=con.cursor()
	    	try:
		    	bc=int(p1.get())
		    	cur.execute("select S_ID from STUDENT where S_ID=%s",(bc,))
		    	rows = cur.fetchall()
		    	if(rows):
				sql_Delete_query = "Delete from STUDENT where S_ID = %s"
			   	cur.execute(sql_Delete_query, (bc,))
				label2=Tk.Label(curr,text="Deleted Successfully",bg='black', fg='white')
				label2.place(relx=0.43,rely=0.55,relwidth=0.15,relheight=0.1)
			else:
			   	label2=Tk.Label(curr,text="Failed! Check S_ID!",bg='black', fg='white')
				label2.place(relx=0.43,rely=0.55,relwidth=0.15,relheight=0.1) 
		except:
	   		label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.43,rely=0.55,relwidth=0.15,relheight=0.1)

#Deleting Books
def delbooks(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Deleting Book records")
	label1=Tk.Label(Frame,text="Warning, Deleting books may affect students who have already borrowed the book",bg='black', fg='white')
	label1.place(relx=0.10,rely=0.0,relwidth=0.9,relheight=0.05)
	label2=Tk.Label(Frame,text="To continue press Continue otherwise Exit",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.05)
	btn = Tk.Button(Frame, text="Continue", command=lambda: delbooks1(Frame,frame,root))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn1 = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn1.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def delbooks1(Frame,frame,root):
	Frame.withdraw()
	Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        Frame1.geometry("800x800")
        Frame1.title("Deleting Books")
	label1=Tk.Label(Frame1,text="Enter Book ID to delete",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame1,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame1, text="Delete", command=lambda: delbookscode(Frame1,Frame,frame,p1))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
	btn0.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame1.protocol("WM_DELETE_WINDOW", root.destroy)

def delbookscode(curr,conf,prev,p1):
	flag=0
    	with con:
    		cur=con.cursor()
	    	try:
	    		if(p1.get!=''):
		    		bc=int(p1.get())
		    		cur.execute("select B_ID from BOOKS where B_ID=%s",(bc,))
		    		rows = cur.fetchall()
		    		if(rows):
				   	sql_Delete_query = "Delete from BOOKS where B_ID = %s"
				   	cur.execute(sql_Delete_query, (bc,))
					label2=Tk.Label(curr,text="Deleted !",bg='black', fg='white')
					label2.place(relx=0.43,rely=0.5,relwidth=0.15,relheight=0.1)
				else:
					label2=Tk.Label(curr,text="Failed! Check Book ID and try again!",bg='black', fg='white')
					label2.place(relx=0.43,rely=0.5,relwidth=0.15,relheight=0.1)
			else:
				raise
		except Exception as e:
			label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.43,rely=0.5,relwidth=0.15,relheight=0.1)   


#View your books  
def viewlog(frame,Frame,p1,root):
	Frame.destroy()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Borrowed Books")
	with con:
		cur=con.cursor()
	 	k=p1.get()
	 	cur.execute("select BOOKS.B_ID,BOOKS.Title,BOOKS.Price,BOOKS.A_ID,ISSUED.Issuedate from BOOKS,ISSUED where BOOKS.B_ID=ISSUED.B_ID  and ISSUED.S_ID=%s",(k,))
	 	Label=Tk.Label(Frame,text="Books Borrowed By You ",bg="black",fg="white",bd=5).pack(side='top')
		cols = ('BookID','Title','Price','AuthorID','Issued')
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
		    listBox.insert("", "end", values=(i[0],i[1],i[2],i[3],i[4]))
		    m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	 	Frame.mainloop()

#View your books  
def viewlog1(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
        Frame.title("Borrowed Books")
        Label1=Tk.Label(Frame,text="Enter Your Library Roll Number",bg="black",fg="white")
        Label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
        p1=Tk.StringVar()
        entry=Tk.Entry(Frame,textvariable=p1)
        entry.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Submit", command=lambda: viewlog(frame,Frame,p1,root))
        btn.place(relx=0.43,rely=0.25,relwidth=0.15,relheight=0.1)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn.place(relx=0.43,rely=0.35,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
        Frame.mainloop()

#Book Display Table
def displayb(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Books")
	with con:
	 	cur=con.cursor()
	  	cur.execute("select * from BOOKS")
	  	#Label=Tk.Label(Frame,text="View All Books",bg="black",fg="white",bd=5).grid(row=0,columnspan=2)
		Label=Tk.Label(Frame,text="View All Books",bg="black",fg="white",bd=5).pack(side='top')
	  	cols=("BID","Title","Price","Count","AuthorID")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings',selectmode='browse')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
		    listBox.insert("", "end", values=(i[0],i[1],i[2],i[3],i[4]))
		    m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
	  	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()	
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)	
		Frame.mainloop()
#Issue books                 
def issueb(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Issue Books")
	label1=Tk.Label(Frame,text="Enter Student ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Book Code",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Issue", command=lambda: issuebcode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def issuebcode(current,prev,p1,p2):
	rn=p1.get()
	bc=p2.get()
    	today = date.today()
    	with con:
		try:    
    			cur = con.cursor()
        		cur.execute("select * from STUDENT where S_ID = %s",(int(rn),))
			if len(cur.fetchall()) > 0:
				cur.execute("select * from BOOKS where B_ID=%s and Count>=1",(int(bc),))
				if len(cur.fetchall()) > 0:
					cur.execute("Update BOOKS set Count=Count-1 where B_ID=%s",(int(bc),))
					cur.execute("INSERT INTO ISSUED VALUES(%s,%s,%s)",(int(bc),int(rn),today))
					label3=Tk.Label(current,text="Success",bg='black', fg='white')
					label3.place(relx=0.43,rely=0.7,relwidth=0.15,relheight=0.1)
				else:
					label3=Tk.Label(current,text="Failed! Check Book ID and try again!",bg='black', fg='white')
					label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)
			else:
				label3=Tk.Label(current,text="Failed! Check Student ID and try again!",bg='black', fg='white')
				label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)
		except:
			label3=Tk.Label(current,text="Failed!",bg='black', fg='white')
			label3.place(relx=0.43,rely=0.7,relwidth=0.15,relheight=0.1)

#Returning Books
def returnb(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Return Books")
	label1=Tk.Label(Frame,text="Enter Student ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Book Code",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Return", command=lambda: returnbcode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def returnbcode(current,prev,p1,p2):
	rn=p1.get()
	bc=p2.get()
    	with con:
		try:		    
    			cur = con.cursor()
    		    	cur.execute("select * from ISSUED where B_ID = %s and S_ID=%s",(int(bc),int(rn)))
			if len(cur.fetchall()) > 0:
				cur.execute("Update BOOKS set Count=Count+1 where B_ID=%s",(int(bc),))
				cur.execute("Delete from ISSUED where B_ID = %s and S_ID=%s",(int(bc),int(rn)))
				label3=Tk.Label(current,text="Success",bg='black', fg='white')
				label3.place(relx=0.43,rely=0.7,relwidth=0.15,relheight=0.1)
			else:
				label3=Tk.Label(current,text="Failed! No such record found",bg='black', fg='white')
				label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)
		except:
			label3=Tk.Label(current,text="Failed! No such record found",bg='black', fg='white')
			label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)

#Lost Books
def lostb(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Lost Books")
	label1=Tk.Label(Frame,text="Enter Student ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Book Code",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Report", command=lambda: lostbcode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def lostbcode(current,prev,p1,p2):
    	rn=p1.get()
    	bc=p2.get()
   	today = date.today()
    	with con:
		try:	    
			if(rn!='' and bc!=''):
	   			cur = con.cursor()
	       			cur.execute("select * from ISSUED where B_ID = %s and S_ID=%s",(int(bc),int(rn)))
				if len(cur.fetchall()) > 0:
					cur.execute("Delete from ISSUED where B_ID = %s and S_ID=%s",(int(bc),int(rn)))
					cur.execute("Select Price from BOOKS where B_ID=%s",(int(bc),))
					p=cur.fetchall()
					cur.execute("INSERT INTO FINESTUDENT (S_ID) VALUES(%s)",(int(rn),))
					cur.execute("INSERT INTO FINE (FineAmount,FineDate) VALUES(%s,%s)",(p,today))
					string="Fine added! Your fine is "+str(p[0][0])+". Inform staff for payment" 
					label3=Tk.Label(current,text=string,bg='black', fg='white')
					label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)

					label4=Tk.Label(current,text="Saved!",bg='black', fg='white')
					label4.place(relx=0.43,rely=0.8,relwidth=0.15,relheight=0.1)
					
				else:
					label3=Tk.Label(current,text="Failed! No such record found",bg='black', fg='white')
					label3.place(relx=0.07,rely=0.7,relwidth=0.85,relheight=0.1)
			else:
				raise

		except:
			label3=Tk.Label(current,text="Failed",bg='black', fg='white')
			label3.place(relx=0.43,rely=0.7,relwidth=0.15,relheight=0.1)
# Add authors addauth()
def addauth(frame,root):
        frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Author Registration")
	label1=Tk.Label(Frame,text="Enter name of Author",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter DOB",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Enter DOD/NULL",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addauthcode(Frame,frame,p1,p2,p3))
	btn.place(relx=0.35,rely=0.65,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.65,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
def addauthcode(current,prev,p1,p2,p3):
	with con:	
    		cur = con.cursor()
		Name=p1.get()
		DOB=p2.get()
		DOD=p3.get()
		try:
			if(Name!='' and DOB !='' and DOD !=''):
				if DOD=='NULL':
					cur.execute("INSERT INTO AUTHOR(Name,DOB,DOD) VALUES(%s,%s,NULL)",(Name,DOB))
				else:
			   		cur.execute("INSERT INTO AUTHOR(Name,DOB,DOD) VALUES(%s,%s,%s)",(Name,DOB,DOD))
				label4=Tk.Label(current,text="Saved!",bg='black', fg='white')
				label4.place(relx=0.43,rely=0.85,relwidth=0.15,relheight=0.1)
			else:
				raise
		except:
			label4=Tk.Label(current,text="Failed",bg='black', fg='white')
			label4.place(relx=0.43,rely=0.85,relwidth=0.15,relheight=0.1)

def addgencat(frame,root): 
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Genre Registration")
	label1=Tk.Label(Frame,text="Enter Genre ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Genre Name",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addgencatcode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def addgencatcode(current,prev,p1,p2):
	with con:	    
    		cur = con.cursor()
		GID=p1.get()
		GName=p2.get()	
		try:
			if(GID!='' and GName!=''):
			   	cur.execute("INSERT INTO GENRE(G_ID,GenreName) VALUES(%s,%s)",(int(GID),GName))
				label3=Tk.Label(current,text="Saved",bg='black', fg='white')
				label3.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.05)
			else:
				raise
		except:
			label3=Tk.Label(current,text="Failed",bg='black', fg='white')
			label3.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.05)

# delete authors
def delauth(frame,root):
    	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Deleting Author")
	label1=Tk.Label(Frame,text="Are you sure you want to delete an author",bg='black', fg='white')
	label1.place(relx=0.10,rely=0.0,relwidth=0.9,relheight=0.05)
	label2=Tk.Label(Frame,text="To continue press Continue other Exit",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.05)
	btn = Tk.Button(Frame, text="Continue", command=lambda: delauth1(Frame,frame,root))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn1 = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn1.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def delauth1(Frame,frame,root):
	Frame.withdraw()
	Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        Frame1.geometry("800x800")
        Frame1.title("Deleting author")
	label1=Tk.Label(Frame1,text="Enter Author ID to delete",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame1,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame1, text="Delete", command=lambda: delauthcode(Frame1,Frame,frame,p1))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
	btn0.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame1.protocol("WM_DELETE_WINDOW", root.destroy)

def delauthcode(curr,conf,prev,p1):
	with con:
		cur=con.cursor()
	    	try:
	    		if(p1.get()!=''):
			    	ac=int(p1.get())
			    	cur.execute("select A_ID from AUTHOR where A_ID=%s",(ac,))
			    	rows = cur.fetchall()
			    	if(rows):
					sql_Delete_query = "Delete from AUTHOR where A_ID = %s"
			   		cur.execute(sql_Delete_query, (ac,))
					label2=Tk.Label(curr,text="Deleted !",bg='black', fg='white')
					label2.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.05)
				else:
				   	label2=Tk.Label(curr,text="Failed! Check A_ID and try again!",bg='black', fg='white')
					label2.place(relx=0.07,rely=0.45,relwidth=0.85,relheight=0.05)
			else:
				raise
		except Exception as e:
	   		label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.05)

# add genres
def addgenre(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Add a genre to a book")
	label1=Tk.Label(Frame,text="Enter Book ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Genre Name",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addgenrecode(Frame,frame,p1,p2))
	btn.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.45,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def addgenrecode(current,prev,p1,p2):
	with con: 
    		cur = con.cursor()
		bc=p1.get()
		gn=p2.get()
		try:
			if(bc!='' and gn !=''):
				cur.execute("Select G_ID from GENRE where GenreName=%s",(gn,))
				p=cur.fetchall()
				if len(p)>0:
					try:	
	   					cur.execute("INSERT INTO GENREBOOK VALUES(%s,%s)",(p,int(bc)))
						label2=Tk.Label(current,text="Saved!",bg='black', fg='white')
						label2.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.05)
					except:
						label2=Tk.Label(current,text="Failed! Check BookID and try again!",bg='black', fg='white')
						label2.place(relx=0.07,rely=0.65,relwidth=0.85,relheight=0.05)
				else:
					label2=Tk.Label(current,text="Failed! Check GenreName and try again!",bg='black', fg='white')
					label2.place(relx=0.07,rely=0.65,relwidth=0.85,relheight=0.05)
			else:
				raise
		except:
			label2=Tk.Label(current,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.05)

#Deleting Genre
def delgen(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Deleting Genre Category")
	label1=Tk.Label(Frame,text="Are you sure you want to delete a Genre Category",bg='black', fg='white')
	label1.place(relx=0.10,rely=0.0,relwidth=0.9,relheight=0.05)
	label2=Tk.Label(Frame,text="To continue press Continue other Exit",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.05)
	btn = Tk.Button(Frame, text="Continue", command=lambda: delgen1(Frame,frame,root))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn1 = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn1.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)


def delgen1(Frame,frame,root):
	Frame.withdraw()
	Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        Frame1.geometry("800x800")
        Frame1.title("Deleting Genre")
	label1=Tk.Label(Frame1,text="Enter GenreName to delete",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame1,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame1, text="Delete", command=lambda: delgencode(Frame1,Frame,frame,p1))
	btn.place(relx=0.35,rely=0.25,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
	btn0.place(relx=0.5,rely=0.25,relwidth=0.15,relheight=0.1)
	Frame1.protocol("WM_DELETE_WINDOW", root.destroy)

def delgencode(curr,conf,prev,p1):
    	with con:
    		cur=con.cursor()
	    	try:
	    	
	    		gc=p1.get()
	    		if(gc!=''):
		    		cur.execute("select G_ID from GENRE where GenreName=%s",(gc,))
		    		rows = cur.fetchall()
		    		if(rows):
				   	sql_Delete_query = "Delete from GENRE where GenreName = %s"
				   	cur.execute(sql_Delete_query, (gc,))
					label2=Tk.Label(curr,text="Deleted!",bg='black', fg='white')
					label2.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.05)
				else:
					label2=Tk.Label(curr,text="Failed! Check GenreName and try again!",bg='black', fg='white')
					label2.place(relx=0.07,rely=0.45,relwidth=0.85,relheight=0.05)
			else:
				raise
		except:
			label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.05)   

# viewenq and coms
def enquery(prev,curr,p1,p11):
	with con:
		cur=con.cursor()
	    	try:
		    	ec=p1.get()
			sc=p11.get()
			if(ec!='' and sc!=''):
			    	cur.execute("select * from ENQSTUDENT where E_ID = %s and S_ID=%s",(ec,sc))
			    	rows = cur.fetchall()
			    	if(rows):
					sql_Delete_query = "Delete from ENQSTUDENT where E_ID = %s and S_ID=%s"
			   		cur.execute(sql_Delete_query, (ec,sc))
					label2=Tk.Label(curr,text="Deleted successfully!",bg='black', fg='white')
					label2.place(relx=0.28,rely=0.75,relwidth=0.45,relheight=0.05)
				else:
				   	label2=Tk.Label(curr,text="Failed! Check values and try again!",bg='black', fg='white')
					label2.place(relx=0.07,rely=0.75,relwidth=0.85,relheight=0.05)
			else:
				raise
		except:
	   		label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.28,rely=0.75,relwidth=0.45,relheight=0.05)
	
def enqco(frame,Frame,root):
	Frame.destroy()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800") 
	Frame.title("Enter Details")
	Label=Tk.Label(Frame,text="Enter EID:",bg='black', fg='white')
	Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry=Tk.Entry(Frame,textvariable=p1)
	entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
	Label1=Tk.Label(Frame,text="Enter SID",bg='black', fg='white')
	Label1.place(relx=0.28,rely=0.35,relwidth=0.45,relheight=0.05)
	p11=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p11)
	entry1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Submit", command=lambda: enquery(frame,Frame,p1,p11))#write the delete query here
	btn.place(relx=0.35,rely=0.55,relwidth=0.15,relheight=0.1)
	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn.place(relx=0.5,rely=0.55,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	Frame.mainloop()
# viewenq and coms
def viewenqco(frame,root):
    frame.withdraw()
    Frame = Tk.Toplevel(bg="#000000",bd=5)
    Frame.geometry("800x800")
    Frame.title("Display All Enquires/Comments")
    with con:
     	cur=con.cursor()
	cur.execute("select ENQSTUDENT.E_ID,ENQSTUDENT.S_ID,ENQCO.Enqco from ENQCO,ENQSTUDENT where ENQCO.E_ID=ENQSTUDENT.E_ID")
	Label=Tk.Label(Frame,text="View All Enquires and Comments",bg="black",fg="white",bd=5).pack(side='top')
	cols=("E:ID","S:ID","Text")
	listBox = ttk.Treeview(Frame, columns=cols, show='headings')
	vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
	vsb.pack(side='right',fill='y')
	listBox.configure(yscrollcommand=vsb.set)
	for col in cols:
    		listBox.heading(col, text=col)    
	listBox.pack(anchor='w')
	m=4
	for i in cur:
		listBox.insert("", "end", values=(i[0],i[1],i[2]))
		m+=1
	hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
	hsb.pack(side='bottom',fill='x')
	listBox.configure(xscrollcommand=hsb.set)
	Label=Tk.Label(Frame,text="Acknowledge and delete queries?",bg="black",fg="white",bd=5).pack()
	btn = Tk.Button(Frame, text="YES", command=lambda: enqco(frame,Frame,root)).pack()
	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	Frame.mainloop()

# View and clear fines paid()
def findel(prev,curr,p1,p11):
	with con:
		cur=con.cursor()
	    	try:
		    	fc=p1.get()
			sc=p11.get()
			if(fc!='' and sc!=''):
			    	cur.execute("select * from FINESTUDENT where F_ID = %s and S_ID=%s",(fc,sc))
			    	rows = cur.fetchall()
			    	if(rows):
					sql_Delete_query = "Delete from FINESTUDENT where F_ID = %s and S_ID=%s"
			   		cur.execute(sql_Delete_query, (fc,sc))
					label2=Tk.Label(curr,text="Deleted!",bg='black', fg='white')
					label2.place(relx=0.28,rely=0.75,relwidth=0.45,relheight=0.05)
				else:
				   	label2=Tk.Label(curr,text="Failed! Check values and try again!",bg='black', fg='white')
					label2.place(relx=0.05,rely=0.75,relwidth=0.85,relheight=0.05)
			else:
				raise
		except:
	   		label2=Tk.Label(curr,text="Failed!",bg='black', fg='white')
			label2.place(relx=0.28,rely=0.75,relwidth=0.45,relheight=0.05)
def finepay(frame,Frame,root):
	Frame.destroy()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800") 
	Frame.title("Enter Details")
	Label=Tk.Label(Frame,text="Enter FID:",bg="black",fg="white")
	Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry=Tk.Entry(Frame,textvariable=p1)
	entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
	Label1=Tk.Label(Frame,text="Enter SID",bg="black",fg="white")
	Label1.place(relx=0.28,rely=0.35,relwidth=0.45,relheight=0.05)
	p11=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p11)
	entry1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
       	btn = Tk.Button(Frame, text="Submit", command=lambda: findel(frame,Frame,p1,p11))#write the delete query here
	btn.place(relx=0.35,rely=0.55,relwidth=0.15,relheight=0.1)
	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn.place(relx=0.5,rely=0.55,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	Frame.mainloop()
	
def finepaid(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Display All Fines")
        with con:
	     	cur=con.cursor()
		cur.execute("select FINE.F_ID,FINESTUDENT.S_ID,FINE.FineAmount,FINE.FineDate from FINE,FINESTUDENT where FINE.F_ID=FINESTUDENT.F_ID")
		
		Label=Tk.Label(Frame,text="View All Fines",bg="black",fg="white",bd=5).pack(side='top')
		cols=("F:ID","S:ID","Amount","Date")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
                hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		Label=Tk.Label(Frame,text="Delete paid fines?",bg="black",fg="white",bd=5).pack()
		btn = Tk.Button(Frame, text="Yes", command=lambda: finepay(frame,Frame)).pack()
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()

# View memberinfo()
def memberinf(frame,Frame,p1,root):
    	Frame.destroy()
    	Frame = Tk.Toplevel(bg="#000000",bd=5)
    	Frame.geometry("800x800") 
    	Frame.title("Display Students")
    	with con:
        	cur=con.cursor()
		sc=p1.get()
		cur.execute("select * from PINFO where S_ID=%s",(sc,))
		Label=Tk.Label(Frame,text="STUDENT INFO ",bg="black",fg="white",bd=5).pack(side='top')
		cols=("ID","City","Phone","Email")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
                hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()

def memberinfo(frame,root):
	frame.withdraw()
   	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Student Info")
	Label=Tk.Label(Frame,text="Enter SID",bg="black",fg="white")
	Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry=Tk.Entry(Frame,textvariable=p1)
	entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Submit", command=lambda:  memberinf(frame,Frame,p1,root))
	btn.place(relx=0.35,rely=0.3,relwidth=0.15,relheight=0.1)
	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn.place(relx=0.5,rely=0.3,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	Frame.mainloop()

    
# viewa() view authors
def viewa(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Authors")
	with con:
	 	cur=con.cursor()
	  	cur.execute("select * from AUTHOR")
	  	Label=Tk.Label(Frame,text="View All Authors",bg="black",fg="white",bd=5).pack(side='top')
	  	cols=("A:ID","Name","DOB","DOD")
	  	listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()

def fines(frame,Frame,p1,root):
	Frame.destroy()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Your Fines")
	with con:
		cur=con.cursor()
		c=p1.get()
		cur.execute("select FINESTUDENT.F_ID,FINESTUDENT.S_ID, FINE.FineAmount,FINE.FineDate from FINE,FINESTUDENT where FINESTUDENT.S_ID=%s and FINE.F_ID=FINESTUDENT.F_ID",(c,))
		Label=Tk.Label(Frame,text=" View  Your  Fines ",bg="black",fg="white",bd=5).pack(side='top')
		cols=("F:ID","S_ID","Amount","Date")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
 		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()
	
def viewf(frame,root):
	frame.withdraw()
        Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("View Your Fines")
        Label=Tk.Label(Frame,text="Enter SID",bg="black",fg="white")
        Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
        p1=Tk.StringVar()
        entry=Tk.Entry(Frame,textvariable=p1)
        entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Submit", command=lambda: fines(frame,Frame,p1,root))
        btn.place(relx=0.35,rely=0.3,relwidth=0.15,relheight=0.1)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn.place(relx=0.5,rely=0.3,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
        Frame.mainloop()

# addenqco() add enquirires or comments
def addenqco(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Enquiries and Comments")
	label1=Tk.Label(Frame,text="Enter Enquiry number",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter Student ID",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Space to enter text",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addenqcocode(Frame,frame,p1,p2,p3))
	btn.place(relx=0.35,rely=0.6,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.6,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def addenqcocode(current,prev,p1,p2,p3):
	with con: 
    		cur = con.cursor()
		ec=p1.get()
		sc=p2.get()
		text=p3.get()	
		try:	
			if(ec!='' and sc!='' and text!=''):
	   			cur.execute("INSERT INTO ENQSTUDENT (E_ID,S_ID) VALUES(%s,%s)",(int(ec),int(sc)))
				cur.execute("INSERT INTO ENQCO (E_ID,Enqco) VALUES(%s,%s)",(int(ec),text))
				label4=Tk.Label(current,text="Saved!",bg='black', fg='white')
				label4.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.05)
			else:
				raise
		except:
			label4=Tk.Label(current,text="Failed! Check S_ID,E_ID,Text and try again!",bg='black', fg='white')
			label4.place(relx=0.07,rely=0.8,relwidth=0.85,relheight=0.05)
# viewbg() view books by genres
def viewbg(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Books By Genre")
	with con:
	 	cur=con.cursor()
	  	cur.execute("select GENRE.GenreName,BOOKS.B_ID,BOOKS.Title,BOOKS.Count from BOOKS,GENRE,GENREBOOK where GENRE.G_ID=GENREBOOK.G_ID and GENREBOOK.B_ID=BOOKS.B_ID group by GenreName,BOOKS.B_ID")
	  	Label=Tk.Label(Frame,text="Books by Genre categories",bg="black",fg="white",bd=5).pack(side='top')
	  	cols=("Genre","B_ID","Title","Count")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop() 
 
def viewba(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
  	Frame.geometry("800x800")
  	Frame.title("Books By Author")
  	with con:
	 	cur=con.cursor()
	  	cur.execute("select AUTHOR.Name,BOOKS.B_ID,BOOKS.Title,BOOKS.Count from BOOKS,AUTHOR where BOOKS.A_ID=AUTHOR.A_ID group by AUTHOR.Name,BOOKS.B_ID")
	  	Label=Tk.Label(Frame,text="Books by Author Names",bg="black",fg="white",bd=5).pack(side='top')
	  	cols=("Author","B_ID","Title","Count")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()  

def addmemberinfo(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Add Personal Info")
	label1=Tk.Label(Frame,text="Enter Student ID",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter City",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Enter phone number",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
	label4=Tk.Label(Frame,text="Enter Email ID",bg='black', fg='white')
	label4.place(relx=0.28,rely=0.58,relwidth=0.45,relheight=0.05)
	p4=Tk.StringVar()
	entry4=Tk.Entry(Frame,textvariable=p4)
	entry4.place(relx=0.28,rely=0.68,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: addmemberinfocode(Frame,frame,p1,p2,p3,p4))
	btn.place(relx=0.35,rely=0.8,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.8,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def addmemberinfocode(current,prev,p1,p2,p3,p4):
	with con: 
    		cur = con.cursor()
		sc=p1.get()
		c=p2.get()
		p=p3.get()
		e=p4.get()
		try:
			if(sc!='' and c!='' and p!='' and e!=''):
				cur.execute("INSERT INTO PINFO VALUES(%s,%s,%s,%s)",(int(sc),c,int(p),e))
				label4=Tk.Label(current,text="Saved",bg='black', fg='white')
				label4.place(relx=0.28,rely=0.9,relwidth=0.45,relheight=0.05)
			else:
				raise
		except:
			label5=Tk.Label(current,text="Failed",bg='black', fg='white')
			label5.place(relx=0.28,rely=0.9,relwidth=0.45,relheight=0.05)
			

def asearch(frame,Frame,p1,root):
	Frame.destroy()
    	Frame = Tk.Toplevel(bg="#000000",bd=5)
    	Frame.geometry("800x800") 
    	Frame.title("Display Books By Author")
    	with con:
        	cur=con.cursor()
	 	a=p1.get()
	 	cur.execute("select AUTHOR.Name,BOOKS.B_ID,BOOKS.Title,BOOKS.Count from BOOKS,AUTHOR where BOOKS.A_ID=AUTHOR.A_ID and AUTHOR.NAME=%s",(a,))
		Label=Tk.Label(Frame,text="STUDENT INFO ",bg="black",fg="white",bd=5).pack(side='top')
		cols=("Author","B_ID","Title","Count")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2],i[3]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()

def searcha(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Display Books By Author")
        Label=Tk.Label(Frame,text="Enter Author Name",bg="black",fg="white")
        Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
        p1=Tk.StringVar()
        entry=Tk.Entry(Frame,textvariable=p1)
        entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Submit", command=lambda:  asearch(frame,Frame,p1,root))
        btn.place(relx=0.35,rely=0.3,relwidth=0.15,relheight=0.1)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn.place(relx=0.5,rely=0.3,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
        Frame.mainloop()

def tsearch(frame,Frame,p1,root):
	Frame.destroy()
        Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800") 
        Frame.title("Display Books By Title")
        with con:
        	cur=con.cursor()
		b=p1.get()
		cur.execute("select BOOKS.B_ID,BOOKS.Title,BOOKS.Count from BOOKS where BOOKS.Title=%s",(b,))
		Label=Tk.Label(Frame,text="BOOKS BY TITLE ",bg="black",fg="white",bd=5).pack(side='top')
		cols=("B_ID","Title","Count")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()
		
def searcht(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
	Frame.geometry("800x800")
	Frame.title("Display Books by title")
	Label=Tk.Label(Frame,text="Enter Book Name",bg="black",fg="white")
	Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry=Tk.Entry(Frame,textvariable=p1)
	entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
	btn = Tk.Button(Frame, text="Submit", command=lambda:  tsearch(frame,Frame,p1,root))
	btn.place(relx=0.35,rely=0.3,relwidth=0.15,relheight=0.1)
	btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn.place(relx=0.5,rely=0.3,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
	Frame.mainloop()

def gsearch(frame,Frame,p1,root):
	Frame.destroy()
        Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800") 
        Frame.title("Display Books By Title")
        with con:
        	cur=con.cursor()
		g=p1.get()
		cur.execute("select BOOKS.B_ID,BOOKS.Title,BOOKS.Count, GENRE.GenreName from BOOKS,GENRE,GENREBOOK where BOOKS.B_ID=GENREBOOK.B_ID and GENREBOOK.G_ID=GENRE.G_ID and GENRE.GenreName=%s",(g,))
		Label=Tk.Label(Frame,text="BOOKS BY GENRE ",bg="black",fg="white",bd=5).pack(side='top')
		cols=("B_ID","Title","Count")
		listBox = ttk.Treeview(Frame, columns=cols, show='headings')
		vsb = ttk.Scrollbar(Frame, orient="vertical", command=listBox.yview)
		vsb.pack(side='right',fill='y')
		listBox.configure(yscrollcommand=vsb.set)
		for col in cols:
    			listBox.heading(col, text=col)    
		listBox.pack(anchor='w')
		m=4
		for i in cur:
			listBox.insert("", "end", values=(i[0],i[1],i[2]))
			m+=1
		hsb = ttk.Scrollbar(Frame, orient="horizontal", command=listBox.xview)
		hsb.pack(side='bottom',fill='x')
		listBox.configure(xscrollcommand=hsb.set)
		btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame)).pack()
		Frame.protocol("WM_DELETE_WINDOW", root.destroy)
		Frame.mainloop()
	
def searchg(frame,root): 
	frame.withdraw()
        Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Search by genre")
        Label=Tk.Label(Frame,text="Enter Genre Name",bg="black",fg="white")
        Label.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.05)
        p1=Tk.StringVar()
        entry=Tk.Entry(Frame,textvariable=p1)
        entry.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Submit", command=lambda:  gsearch(frame,Frame,p1,root))
        btn.place(relx=0.35,rely=0.3,relwidth=0.15,relheight=0.1)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
        btn.place(relx=0.5,rely=0.3,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)
        Frame.mainloop()

def updatea(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Modify Author Details")
	label0=Tk.Label(Frame,text="Enter A_ID of author to be modified",bg='black', fg='white')
	label0.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p0=Tk.StringVar()
	entry0=Tk.Entry(Frame,textvariable=p0)
	entry0.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
	label1=Tk.Label(Frame,text="Enter name of Author",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
	label2=Tk.Label(Frame,text="Enter DOB",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
	label3=Tk.Label(Frame,text="Enter DOD/NULL",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.58,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.63,relwidth=0.45,relheight=0.1)
        btn = Tk.Button(Frame, text="Save", command=lambda: updateacode(Frame,frame,p0,p1,p2,p3))
	btn.place(relx=0.35,rely=0.8,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.8,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def updateacode(current,prev,p1,p2,p3,p4):
	with con:	    
    		cur = con.cursor()
    		n=p1.get()
		try:
			cur.execute("select * from AUTHOR where A_ID = %s",(int(n),))
			if len(cur.fetchall()) > 0:
				Name=p2.get()
				DOB=p3.get()
				DOD=p4.get()
				try:		
						if(Name!='' and DOB !='' and DOD!=''):	
							if DOD=='NULL':
								cur.execute("Update AUTHOR set Name=%s,DOB=%s,DOD=NULL where A_ID=%s",(Name,DOB,int(n)))
							else:
								cur.execute("Update AUTHOR set Name=%s,DOB=%s,DOD=%s where A_ID=%s",(Name,DOB,DOD,int(n)))				
							label4=Tk.Label(current,text="Updated!",bg='black', fg='white')
							label4.place(relx=0.28,rely=0.95,relwidth=0.45,relheight=0.05)
						else:
							raise
				except:   
						label4=Tk.Label(current,text="Failed! Check values and try again!",bg='black', fg='white')
						label4.place(relx=0.07,rely=0.95,relwidth=0.85,relheight=0.05)
				else:
					raise
			else:
				label4=Tk.Label(current,text="No record found!",bg='black', fg='white')
				label4.place(relx=0.07,rely=0.95,relwidth=0.85,relheight=0.05)
				  
		except:
			label4=Tk.Label(current,text="Failed! Check A_ID",bg='black', fg='white')
			label4.place(relx=0.07,rely=0.95,relwidth=0.85,relheight=0.05)

def updateb(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Modify Book Details")
	label0=Tk.Label(Frame,text="Enter BookID",bg='black', fg='white')
	label0.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
	p0=Tk.StringVar()
	entry0=Tk.Entry(Frame,textvariable=p0)
	entry0.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.05)
	label1=Tk.Label(Frame,text="Enter name of Book",bg='black', fg='white')
	label1.place(relx=0.28,rely=0.15,relwidth=0.45,relheight=0.05)
	p1=Tk.StringVar()
	entry1=Tk.Entry(Frame,textvariable=p1)
	entry1.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
	label2=Tk.Label(Frame,text="Enter Price",bg='black', fg='white')
	label2.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.05)
	p2=Tk.StringVar()
	entry2=Tk.Entry(Frame,textvariable=p2)
	entry2.place(relx=0.28,rely=0.35,relwidth=0.45,relheight=0.05)
	label3=Tk.Label(Frame,text="Enter count ",bg='black', fg='white')
	label3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.05)
	p3=Tk.StringVar()
	entry3=Tk.Entry(Frame,textvariable=p3)
	entry3.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.05)
	label4=Tk.Label(Frame,text="Enter Author_ID/NULL ",bg='black', fg='white')
	label4.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.05)
	p4=Tk.StringVar()
	entry4=Tk.Entry(Frame,textvariable=p4)
	entry4.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.05)
        btn = Tk.Button(Frame, text="Save", command=lambda: updatebcode(Frame,frame,p0,p1,p2,p3,p4))
	btn.place(relx=0.35,rely=0.75,relwidth=0.15,relheight=0.1)
	btn0= Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn0.place(relx=0.5,rely=0.75,relwidth=0.15,relheight=0.1)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def updatebcode(current,prev,p0,p1,p2,p3,p4):
	with con:	    
    		cur = con.cursor()
    		n=p0.get()
		try:
			cur.execute("select * from BOOKS where B_ID = %s",(int(n),))
			if len(cur.fetchall()) > 0:
				Title=p1.get()
				Price=p2.get()
				Count=p2.get()
				AuthorID=p4.get()	
				try:
					if(Title!='' and Price!='' and Count!='' and AuthorID!=''):		
						if AuthorID=='NULL':
							cur.execute("Update BOOKS set Title=%s,Price=%s,Count=%s,A_ID=NULL where B_ID=%s",(Title,int(Price),int(Count),int(n)))
						else:
							cur.execute("Update BOOKS set Title=%s,Price=%s,Count=%s,A_ID=%s where B_ID=%s",(Title,int(Price),int(Count),int(AuthorID),int(n)))	
						label5=Tk.Label(current,text="Updated!",bg='black', fg='white')
						label5.place(relx=0.45,rely=0.9,relwidth=0.45,relheight=0.05) 
					else:	
						raise
				except:
					label5=Tk.Label(current,text="Failed! Check values",bg='black', fg='white')
					label5.place(relx=0.07,rely=0.9,relwidth=0.85,relheight=0.05)
   
			else:
				label5=Tk.Label(current,text="Failed! No record found!",bg='black', fg='white')
				label5.place(relx=0.07,rely=0.9,relwidth=0.85,relheight=0.05)
		except:
			label5=Tk.Label(current,text="Failed! Check B_ID!",bg='black', fg='white')
			label5.place(relx=0.07,rely=0.9,relwidth=0.85,relheight=0.05)  

def updates(frame,root):
	frame.withdraw()
	Frame = Tk.Toplevel(bg="#000000",bd=5)
        Frame.geometry("800x800")
        Frame.title("Student Details")
	btn = Tk.Button(Frame, text="Change administrative info", command=lambda: updates1(Frame,frame,1,root),bg='black', fg='white')
	btn.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.15)
	btn = Tk.Button(Frame, text="Change personal info", command=lambda: updates1(Frame,frame,2,root),bg='black', fg='white')
	btn.place(relx=0.28,rely=0.20,relwidth=0.45,relheight=0.15)
        btn = Tk.Button(Frame, text="Exit", command=lambda: onbuttonclick(Frame,frame))
	btn.place(relx=0.48,rely=0.4)
	Frame.protocol("WM_DELETE_WINDOW", root.destroy)

def updates1(Frame,frame,n,root):
	if n==1:
		Frame.withdraw()
		Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        	Frame1.geometry("800x800")
        	Frame1.title("Admin Details")
		label1=Tk.Label(Frame1,text="Enter SID",bg='black', fg='white')
		label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
		p1=Tk.StringVar()
		entry1=Tk.Entry(Frame1,textvariable=p1)
		entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
		label2=Tk.Label(Frame1,text="Enter changed/old name",bg='black', fg='white')
		label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
		p2=Tk.StringVar()
		entry2=Tk.Entry(Frame1,textvariable=p2)
		entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
		label3=Tk.Label(Frame1,text="Enter changed/old department",bg='black', fg='white')
		label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
		p3=Tk.StringVar()
		entry3=Tk.Entry(Frame1,textvariable=p3)
		entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
        	btn = Tk.Button(Frame1, text="Save", command=lambda: updatescode(Frame1,frame,Frame,p1,p2,p3,'',1))
		btn.place(relx=0.35,rely=0.6,relwidth=0.15,relheight=0.1)
		btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
		btn0.place(relx=0.5,rely=0.6,relwidth=0.15,relheight=0.1)
		Frame1.protocol("WM_DELETE_WINDOW", root.destroy)

	elif n==2:
		Frame.withdraw()
		Frame1 = Tk.Toplevel(bg="#000000",bd=5)
        	Frame1.geometry("800x800")
        	Frame1.title("Personal Details")
		label1=Tk.Label(Frame1,text="Enter SID",bg='black', fg='white')
		label1.place(relx=0.28,rely=0.0,relwidth=0.45,relheight=0.05)
		p1=Tk.StringVar()
		entry1=Tk.Entry(Frame1,textvariable=p1)
		entry1.place(relx=0.28,rely=0.05,relwidth=0.45,relheight=0.1)
		label2=Tk.Label(Frame1,text="Enter changed/old city",bg='black', fg='white')
		label2.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.05)
		p2=Tk.StringVar()
		entry2=Tk.Entry(Frame1,textvariable=p2)
		entry2.place(relx=0.28,rely=0.25,relwidth=0.45,relheight=0.1)
		label3=Tk.Label(Frame1,text="Enter changed/old phone number",bg='black', fg='white')
		label3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.05)
		p3=Tk.StringVar()
		entry3=Tk.Entry(Frame1,textvariable=p3)
		entry3.place(relx=0.28,rely=0.45,relwidth=0.45,relheight=0.1)
		label4=Tk.Label(Frame1,text="Enter changed/old EmailID",bg='black', fg='white')
		label4.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.05)
		p4=Tk.StringVar()
		entry4=Tk.Entry(Frame1,textvariable=p4)
		entry4.place(relx=0.28,rely=0.65,relwidth=0.45,relheight=0.1)
        	btn = Tk.Button(Frame1, text="Save", command=lambda: updatescode(Frame1,frame,Frame,p1,p2,p3,p4,2))
		btn.place(relx=0.35,rely=0.8,relwidth=0.15,relheight=0.1)
		btn0= Tk.Button(Frame1, text="Exit", command=lambda: onbuttonclick(Frame1,Frame))
		btn0.place(relx=0.5,rely=0.8,relwidth=0.15,relheight=0.1)
		Frame1.protocol("WM_DELETE_WINDOW", root.destroy)
def updatescode(current,prev,menu,p1,p2,p3,p4,num):
	with con:	
		n=p1.get()   
    		if num==1:
			try:
				cur = con.cursor()
				cur.execute("select * from STUDENT where S_ID = %s",(int(n),))
				if len(cur.fetchall())>0:
					Name=p2.get()
					Department=p3.get()
					if(Name!='' and Department!=''):
						cur.execute("Update STUDENT set Name=%s,Department=%s where S_ID=%s",(Name,Department,int(n)))
						label5=Tk.Label(current,text="Updated!",bg='black', fg='white')
						label5.place(relx=0.45,rely=0.85,relwidth=0.15,relheight=0.05)  
					else:
						raise
				else:
					label5=Tk.Label(current,text="Failed! Check S_ID and try again!",bg='black', fg='white')
					label5.place(relx=0.07,rely=0.85,relwidth=0.85,relheight=0.05)  
			except:
				label5=Tk.Label(current,text="Failed! Check S_ID and try again1!",bg='black', fg='white')
				label5.place(relx=0.07,rely=0.85,relwidth=0.85,relheight=0.05)  
  
		elif num==2:
			try:
				cur = con.cursor()
				cur.execute("select * from PINFO where S_ID = %s",(int(n),))
				if len(cur.fetchall()) > 0:
					c=p2.get()
					p=p3.get()
					e=p4.get()	
					if(c!='' and p!='' and e!=''):
						cur.execute("Update PINFO set City=%s,Phone=%s,Email=%s where S_ID=%s",(c,int(p),e,int(n)))
						label5=Tk.Label(current,text="Updated!",bg='black', fg='white')
						label5.place(relx=0.45,rely=0.9,relwidth=0.15,relheight=0.05)  
					else:
						raise
				else:
					label5=Tk.Label(current,text="Failed! Check S_ID and try again!",bg='black', fg='white')
					label5.place(relx=0.07,rely=0.9,relwidth=0.85,relheight=0.05) 
    			except:
				label5=Tk.Label(current,text="Failed! Check S_ID and try again1!",bg='black', fg='white')
				label5.place(relx=0.07,rely=0.9,relwidth=0.85,relheight=0.05) 

