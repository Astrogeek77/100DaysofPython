import os
import string

curr_path = "C:\\Coding\\Python\\100DaysofCode\\Cluter-simplify-files"

pdf_files = os.listdir(curr_path + "\\pdfs")
png_files = os.listdir(curr_path + "\\pics")
# print(pdf_files)
# print(png_files)

supported_pics = (".jpg", ".heic")

def get_next_char(ch):
    if ch.isupper():
        letters = string.ascii_uppercase
    else:
        letters = string.ascii_lowercase

    index = letters.index(ch)
    next_char = letters[index + 1]
    return next_char


def simplify_png_names():
    i = 1
    for file in png_files:
        file_ext = os.path.splitext(file)[1]
        if file.endswith(supported_pics):
            print(file)
            os.rename(f"{curr_path}\\pics\\{file}",
                      f"{curr_path}\\pics\\{i}{file_ext}")
            i = i + 1


def simplify_png_names2():
    ch = 'a'
    for file in png_files:
        file_ext = os.path.splitext(file)[1]
        if file.endswith(supported_pics):
            print(file)
            os.rename(f"{curr_path}\\pics\\{file}",
                      f"{curr_path}\\pics\\{ch}{file_ext}")
            ch = get_next_char(ch)


def simplify_pdf_names():
    ch = 'A'
    for file in pdf_files:
        file_ext = os.path.splitext(file)[1]
        if file.endswith((".pdf")):
            print(file)
            os.rename(f"{curr_path}\\pdfs\\{file}",
                      f"{curr_path}\\pdfs\\{ch}{file_ext}")
            ch = get_next_char(ch)


simplify_png_names()
simplify_pdf_names()
# simplify_png_names2()
