from my_pdf_toolkit import *
import os

# curr_path = os.getcwd()
curr_path = "C:\\Coding\\Python\\100DaysofCode\\PDF toolkit"
# print(curr_path)

toolkit = Python_PDF_Toolkit(curr_path)
# # while True:
all_pdfs = getAllPdfs(toolkit)

# index = int(input("Enter index of the pdf file to get its info: "))
# if (index < 0 or index >= len(all_pdfs)):
#     print("Please enter a valid index")
# break

# getMetaData(toolkit, all_pdfs[index])
# getLength(all_pdfs[index])
# getExtractText(all_pdfs[index])

# splitPdf(toolkit, all_pdfs[index])
# splitPdfFromBetween(toolkit, all_pdfs[index], 1, 2)
# splitOnePageFromPdf(toolkit, all_pdfs[index], 2)
list_of_pdfs = getPdfFolder(toolkit, curr_path + "\\pdfs")
mergePdf(toolkit, list_of_pdfs)
