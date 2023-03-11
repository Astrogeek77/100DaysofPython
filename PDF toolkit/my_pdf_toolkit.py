import os
import string
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


class Python_PDF_Toolkit:
    curr_path = "C:\\Coding\\Python\\100DaysofCode\\PDF toolkit"

    def __init__(self, curr_path):
        self.curr_path = curr_path

    def get_next_char(self, ch):
        if ch.isupper():
            letters = string.ascii_uppercase
        else:
            letters = string.ascii_lowercase

        index = letters.index(ch)
        next_char = letters[index + 1]
        return next_char

    def simplify_pdf_names(self, pdf_files):
        ch = 'A'
        for file in pdf_files:
            file_ext = os.path.splitext(file)[1]
            if file.endswith((".pdf")):
                # print(file)
                os.rename(f"{self.curr_path}\\pdfs\\{file}",
                          f"{self.curr_path}\\pdfs\\{ch}{file_ext}")
                ch = self.get_next_char(ch)

    def getMetaData(self, pdfPath):
        '''Returns the meta data of a PDF file found at the given path'''
        with open(pdfPath, 'rb') as f:
            reader = PdfReader(f)
            info = reader.metadata
            print("\n")
            for key, value in info.items():
                print(f"{key}: {value}")

    def getLength(self, pdfPath):
        '''Get the length of PDF file (pages)'''
        total_pages = 0
        with open(pdfPath, 'rb') as f:
            reader = PdfReader(f)
            total_pages = len(reader.pages)
            # print(f"\nTotal pages: {total_pages}")
        return total_pages

    def getAllPdfs(self):
        all_pdfs = {}

        reveal = os.listdir(self.curr_path + '\\pdfs')
        for index, rev in enumerate(reveal):
            # print(f"\t{index+1}. {rev}")
            all_pdfs[index+1] = self.curr_path + '\\pdfs\\' + rev

        for pdf_file in all_pdfs:
            print(
                f"{pdf_file}. {all_pdfs[pdf_file]} - {self.getLength(all_pdfs[pdf_file])} pages")

        # print(getPdfFolder(curr_path + '\\pdfs'))
        print("\n")
        return all_pdfs

    def getPdfFolder(self, parentFolder):
        '''get the list of PDF files from a provided folder'''
        listOfPdfs = []
        for path, subdirs, pdfs in os.walk(parentFolder):
            for pdf in pdfs:
                if pdf.endswith('.pdf'):
                    listOfPdfs.append(os.path.join(path, pdf))
        return listOfPdfs

    def getExtractText(self, pdfPath):
        '''Extract PDF file text'''
        with open(pdfPath, 'rb') as f:
            reader = PdfReader(f)
            result = []
            for pageNumber in range(0, len(reader.pages)):
                selectedPage = reader.pages[pageNumber]
                text = selectedPage.extract_text()
                result.append(text)
            print('\n\n\n'.join(result))
            return '\n\n\n'.join(result)

    def splitPdf(self, pdf_path):
        '''split the pdf into new single page pdf files for each page'''
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            for pageNumber in range(0, len(reader.pages)):
                selectedPage = reader.pages[pageNumber]
                writer = PdfWriter()
                writer.add_page(selectedPage)
                fileName = pdf_path.split('.')[0]
                outputFileName = f"{fileName}_pg_{pageNumber+1}.pdf"
                with open(outputFileName, 'wb') as out:
                    writer.write(out)
                print(f"\nCreated a Pdf: {outputFileName}")

    def splitPdfFromBetween(self, pdf_path, start_pg, stop_pg):
        '''split only the pages in the given range into new pdf file of len(given range)'''
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            writer = PdfWriter()
            for pageNumber in range(start_pg - 1, stop_pg):
                selectedPage = reader.pages[pageNumber]
                writer.add_page(selectedPage)
                fileName = pdf_path.split('.')[0]
                outputFileName = f"{fileName}_from_{start_pg}_to_{stop_pg}.pdf"
            with open(outputFileName, 'wb') as out:
                writer.write(out)
            print(f"Created a Pdf: {outputFileName}")

    def splitOnePageFromPdf(self, pdf_path, x_page):
        '''split one particular page from pdf'''
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            writer = PdfWriter()
            selectedPage = reader.pages[x_page - 1]
            writer.add_page(selectedPage)
            fileName = pdf_path.split('.')[0]
            outputFileName = f"{fileName}_pg_no{x_page}.pdf"
            with open(outputFileName, 'wb') as out:
                writer.write(out)
            print(f"Created a Pdf: {outputFileName}")

    def mergePdf(self, list_of_pdfs, output_filename='merged_file.pdf'):
        '''merges all pdfs in given list of pdfs'''

        merger = PdfMerger()
        with open(self.curr_path + "\\pdfs\\" + output_filename, 'wb') as f:
            for file in list_of_pdfs:
                merger.append(file)
            merger.write(f)
            print("files have been merged")
