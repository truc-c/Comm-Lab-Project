
import os

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
