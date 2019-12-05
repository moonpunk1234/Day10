
"""
File
----------------------------------------------------------
fileHandler = open(fileName,mode)

    Mode 	Description
	'r' 	Open a file for reading. (default)
	'w' 	Open a file for writing. Creates a new file if it does not exist or                 truncates the file if it exists.
	'x' 	Open a file for exclusive creation. If the file already exists, the                 operation fails.
	'a' 	Open for appending at the end of the file without truncating it.                 Creates a new file if it does not exist.
	't' 	Open in text mode. (default)
	'b' 	Open in binary mode.
	'+' 	Open a file for updating (reading and writing)
"""

def ReadFile(fileName):
	try:
		#f= open("test.txt",'r')
		f= open(fileName)	
		
		for line in f:
			print(line)	
			
			f.close()
	except FileNotFoundError:
		print("File Not Found !!!")
	
def WriteFile(fileName,content):
	f= open(fileName,'w')	
	f.write(content)	
	f.close()	
	
	print('Writing Complete ...')

def AppendFile(fileName,content):
	f= open(fileName,'a')	
	f.write(content)	
	f.close()	
	
	print('Writing Complete ...')

def ReadingFile(fileName):
	with open(fileName) as fo:
		lines = fo.readlines()
		
	for line in lines:
		print(line.upper())

mytext ="""
Amar Khub Matha Dhorechee
Asole matha dhora na Ghum Paise
"""

WriteFile('myfile.txt',mytext)
AppendFile('myfile.txt',"Test Message")
AppendFile('yourfile.txt',"Test Message")
AppendFile('yourfile.txt',"Mui Bughte parsi")
ReadFile('myfile1.txt')
ReadingFile('myfile.txt')