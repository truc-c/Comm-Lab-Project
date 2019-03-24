from bs4 import BeautifulSoup
import os

"""
source = '/users'
myList = []

# enter the name of file you are annotating

filename = raw_input("Enter file name incuding .eaf at the end: ")

# walk through the directories and look for the file specified
#	"folderPath" now contains the directory path
# once you find the file you use it add it to the end of your folder path variable
#	so that you know the path of the file "fileInfo" contains the whole path
#	including the .eaf file
# then you open the file, read the lines and create a list named "readInfo"

# myList contains a list of all .eaf files, i don't think you need it

for folder, subfolder, files in os.walk(source):
	for file in files:
		if file.endswith(".eaf"):
			myList.append(file)
			if file == filename:
				folderPath = folder
				fileInfo = open(folderPath + '/' + file)
				readInfo = fileInfo.readlines()


#print(myList)
print
print("THE FOLDER PATH IS = " + folderPath)
print
print("readInfo ================================================================ ")
print
print(readInfo)
print

fileInfo.close()
"""



def space():
	print ' '

# We are providing a html version of our .eaf file so that we can use
#	BeautifulSoup
# We open the html file and place it in a object
eaf_html = open('/users/curtchang/desktop/0054_000603_test_copy copy.html')

# We create an BeautifulSoup object
bs_obj = BeautifulSoup(eaf_html.read(),'html.parser')
space()

# Here we use the find_all function to look for the 'cut' tier that we want
# We pass in the tier_id attribute
# The type for cut1 is of ResultSet, it seems like a list separated by newline
#	characters (/n), maybe we can use that to our advantage?
cut1 = bs_obj.find(tier_id='cut')
print 'cut1 ================== \n', cut1
print 'cut1 type = ' , type(cut1)
space()
space()

cut2 = str(cut1)
print cut2



space()
