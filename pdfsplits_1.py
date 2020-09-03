import sys
from PyPDF2 import PdfFileWriter,PdfFileReader
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


total_pages = 10

def pdf_splitter(file,start,end):
    #we will save new splited pdf as "nameofpdf splitted.pdf"
    #example if pdf name is "abc.pdf" then it will be saved as "abc splitted.pdf"
    new_file_name = file.split(".")[0] + " " + "splitted.pdf"

    read_file = PdfFileReader(open(file,"rb")) #read pdf
    new_pdf = PdfFileWriter() #create write object
    start-=1
    try:
        with open(new_file_name,"wb") as f:
            for i in range(start, end):
              new_pdf.addPage(read_file.getPage(i))
              new_pdf.write(f)
              i+=1
            print("PDF splitted Successfully")
    except Exception as e:
        print(e)

def ofile():
	opfile = filedialog.askopenfilename(initialdir=r"C:\Users\Parme\Documents\Downloads",title="Select",filetypes=(('TEXT DOCUMENT',"*.pdf"),("All Files","")))
	global file_path
	file_path = str(opfile)
	temp_read = PdfFileReader(open(file_path,"rb"))
	total_pages = temp_read.getNumPages()
	sca1['to'] = total_pages
	sca2['to'] = total_pages

root = Tk()
root.title("PDF SPPPPP")
root.configure(background='black')


head = Label(root,
			 text='PDF Splitter',
			 font=('Algerian',25),
                        fg="#fff",
                        bg="#000")

head.grid(column=0,   
          row=0,
         columnspan=4,
         pady=20
             )

s1 = Label(root,
         text="Step #1",
         font=('Bradley Hand ITC',18),
         fg="#fff",
         bg="#000"
           )

s1.grid(column=0,
        row=1,
        )

openbut = Button(root,
         text="Please Select a File",
         bg='#fff',
         fg='#000',
         font=('Arial Bold',10),
         relief='ridge',
         bd=5,
         command=ofile
         )      

openbut.grid(column=0,
     row=2,
     columnspan=4,
     pady=15
      )

s2 = Label(root,
         text="Step #2",
         font=('Bradley Hand ITC',18),
         fg="#fff",
         bg="#000"
           )

s2.grid(column=0,
        row=3,
        padx=6
        )
Label(root,text='Select Start Page',
			fg='white',
			bg='black',
		    font=('Hobo Std',18)).grid(row=4,column=0,pady=8,padx=1,sticky=W)

sca1 = Scale(root,from_=1,to=5,bg='black',fg='white',orient=HORIZONTAL,length=220)
sca1.grid(row=5,column=0,pady=4,padx=8)

Label(root,text='Select End Page',
			fg='white',
			bg='black',
		    font=('Hobo Std',18)).grid(row=6,column=0,pady=8,padx=1,sticky=W)


sca2 = Scale(root,from_=1,to=5,bg='black',fg='white',orient=HORIZONTAL,length=220)
sca2.grid(row=7,column=0,pady=4,padx=8)

gobut = Button(root,
			   text="Split",
			   bg='#fff',
         fg='#000',
         font=('Arial Bold',10),
         relief='ridge',
         bd=5,
         command=lambda: pdf_splitter(file_path,sca1.get(),sca2.get())).grid(row=8,column=0,pady=10,padx=8)

root.mainloop()
