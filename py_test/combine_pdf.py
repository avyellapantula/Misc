from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
from tkinter import *

gui = Tk()
gui.resizable(0, 0)

gui.geometry("700x300")
gui.title("PDF Combine")

l = StringVar()
l2 = StringVar()
f = StringVar()
e = StringVar()

fin = Entry()
fin_lab = fin.get()
filenamelabel = Label(textvariable=l).place(x=100, y=5)
filenamelabel2 = Label(textvariable=l2).place(x=100, y=35)
exportfolderlabel = Label(textvariable=f).place(x=100, y=70)
fin.place(x=10, y=115)


def openFileDialog():
    global fileName
    fileName = filedialog.askopenfilename(initialdir="F:/!2019 Tax Prep Files/RFCU 2019 stmts", title="Pick a PDF file.",
                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    l.set(fileName)


# initialdir='/Users/'

def openFileDialog2():
    global fileName2
    fileName2 = filedialog.askopenfilename(initialdir="F:/!2019 Tax Prep Files/RFCU 2019 stmts", title="Pick a second PDF file.",
                                           filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    l2.set(fileName2)


def openExportFolderDialog():
    global exportFolder
    exportFolder = filedialog.askdirectory(initialdir='F:/!2019 Tax Prep Files/RFCU 2019 stmts', title='Pick an export folder.')
    f.set(exportFolder)


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


def combinePdf():
    global finalFileName
    output = PdfFileWriter()
    append_pdf(PdfFileReader(open(fileName, "rb")), output)
    append_pdf(PdfFileReader(open(fileName2, "rb")), output)

    output_stream = open(exportFolder + '/' + fin.get() + '.pdf', 'wb')
    output.write(output_stream)
    output_stream.close()



def quit_pgm():
    # gui.destroy()
    sys.exit()


importpdf1 = Button(text="Import PDF", command=openFileDialog).place(x=10, y=0)
importpdf2 = Button(text="Import PDF 2", command=openFileDialog2).place(x=10, y=35)
setexport = Button(text="Set Export Folder", command=openExportFolderDialog).place(x=10, y=70)
combinepdf = Button(text="Combine PDFs", command=combinePdf).place(x=10, y=150)
quit_button = Button(text="Quit After Combining", command=quit_pgm).place(x=10, y=200)

gui.mainloop()
input('Please continue mofo')