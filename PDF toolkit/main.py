from my_pdf_toolkit import *
import os

# curr_path = os.getcwd()
curr_path = "C:\\Coding\\Python\\100DaysofCode\\PDF toolkit"

toolkit = Python_PDF_Toolkit(curr_path)
all_pdfs = toolkit.getAllPdfs()

index = int(input("Enter index of the pdf file to get its info: "))
if (index < 0 or index > len(all_pdfs)):
    print("Please enter a valid index")

toolkit.getMetaData(all_pdfs[index])
toolkit.getLength(all_pdfs[index])
toolkit.getExtractText(all_pdfs[index])

toolkit.splitPdf(all_pdfs[index])
toolkit.splitPdfFromBetween(all_pdfs[index], 1, 2)
toolkit.splitOnePageFromPdf(all_pdfs[index], 2)

list_of_pdfs = toolkit.getPdfFolder(curr_path + "\\pdfs")
toolkit.mergePdf(list_of_pdfs)
