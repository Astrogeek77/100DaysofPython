from os import environ as env
import os
import string
import random


class simplifyTheClutterInFolder:

    def showFolder(self):
        username = "Python_Geek_101"
        print(f"\t\tWelcome {username} for Renaming the files\n")
        print("List of the directories Present:\n")
        print("Folder:\t\tFiles:\n\npics")

        revealpng = os.listdir("pics")

        for rev in revealpng:
            print(f"\t\t\t{rev}")

        print("pdfs")

        revealpdf = os.listdir("pdfs")

        for rev in revealpdf:
            print(f"\t\t\t{rev}")

    def createRandomFilesNameForTest(self):
        self.rwordlist = list()

        for x in range(0, 4):
            rword = list()

            for k in range(0, 6):
                rletter = random.choice(string.ascii_letters)
                rword.append(rletter)

            formword = rword[0] + rword[1] + rword[2] + rword[3] + rword[4]
            self.rwordlist.append(formword)

    def takeInput(self):
        self.choosedir = int(
            input(
                "\nEnter which Directory you want to Simplify or Clutter\nEnter 1 -> png\nEnter 2 -> pdf\n\nEnter Here -> "
            ))
        self.choose = input(
            "\nEnter 'c' for cluttering the name of Files present in the Directory\nEnter 's' for simplifing the name of Files present in the Directory\n\nEnter here: "
        )
        if (self.choosedir == 1):
            self.choosedir = 'pics'
            self.form = 'png'
        elif (self.choosedir == 2):
            self.choosedir = 'pdfs'
            self.form = 'pdf'
        else:
            raise ValueError("\n\tEnter 1 and 2 only\n")

    def changingFilesNames(self):
        path = os.chdir(self.choosedir)
        i = 1
        a = 0
        for file in os.listdir(path):
            newFileName = f"{i}.{self.form}"
            clutterword = f"{self.rwordlist[a]}.{self.form}"

            if (self.choose == 'c'):
                os.rename(file, clutterword)
            elif (self.choose == 's'):
                os.rename(file, newFileName)
            else:
                print("Enter c and s only")
            i += 1
            a += 1

    def endResult(self):
        if (self.choose == 'c'):
            print(
                "\nFiles Name have been cluttered\n\n\tOpen the directory to see OR Run again"
            )
        elif (self.choose == 's'):
            print(
                "\nFiles Name have been Simplified\n\n\tOpen the directory to see OR Run again"
            )


s = simplifyTheClutterInFolder()
s.showFolder()
s.createRandomFilesNameForTest()
s.takeInput()
s.changingFilesNames()
s.endResult()
