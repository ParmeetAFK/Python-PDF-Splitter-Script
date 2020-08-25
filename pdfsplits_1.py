import sys
from PyPDF2 import PdfFileWriter,PdfFileReader

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

#First step is to check all command line arguments
if len(sys.argv) < 4:
    #if arguments are less then 4 then we will show error message to users.
    print("*"*50)
    print("Invalid Agruments")
    print("-"*50)
    print("python pdfsplits.py pdf_file_name_with_full_path start_page_number end_page_number")
    print("-"*50)
    print("Example")
    print("python pdfsplits.py 'c:\\\\Users\\\\a.pdf' 2 5")
    print("*"*50)
else:
    file_path = sys.argv[1] #file name of PDF file which user want to split
    start_page = int(sys.argv[2]) #start page number 
    end_page = int(sys.argv[3]) #end page number
    pdf_splitter(file_path,start_page,end_page)
