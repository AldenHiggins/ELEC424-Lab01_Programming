#! /usr/bin/python
import sys
import pdb

# Change the text in file_name such that every line is of length
# justify_length
def justify(file_name, justify_length):
	file = open(file_name,'r+')
	newFileText = ""
	for line in file:
		newFileText += justifyHelper(line,file,justify_length)
	file.seek(0,0)
	file.write(newFileText)
	file.close()

def justifyHelper(line, file, justify_length):
	# If the line is greater than the justify_length, split off the line
	# at the justify length and justify the rest of the line on another line.
	if (len(line) > justify_length):
		return justifyHelper2(line[0:justify_length - 2] + "\n", file, justify_length) + justifyHelper(line[justify_length - 2:len(line)], file, justify_length)
	else:
		return justifyHelper2(line, file, justify_length)

def justifyHelper2(line, file, justify_length):
	numWords = len(line.split())
	spacesPerWord = (justify_length - len(line))/(numWords)
	newLine = ""
	wordFound = False
	wordsFound = 0
	spacesAdded = 0
	for letter in line:
		newLine += letter
		if (letter == "\n"):
			break
		if (wordFound == False):
			if (letter != ' '):
				wordFound = True
				wordsFound += 1
		if (wordFound):
			if (letter == ' '):
				if (wordsFound == numWords - 1):
					for i in range(justify_length - len(line) - spacesAdded):
						newLine += ' '
				else:
					for i in range(spacesPerWord):
						newLine += ' '
						spacesAdded += 1
				wordFound = False
	#pdb.set_trace()
	#print "old: " + line
	#print len(newLine)
	#print "new: " + newLine
	#file.write(newLine)
	return newLine

# Program justifies text contents of a given file
# This is the actual code that gets run when the
# program is run. 
#
# DO NOT EDIT BELOW HERE.
if __name__ == "__main__":

    file_name = ''
    length = -1

    # Parse command line arguments
    try:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-f':
                file_name = sys.argv[i+1]
            elif sys.argv[i] == '-l':
                length = int(sys.argv[i+1])
    except:
        exit('Input error. Example input: justifytext -f mytextfile -l 80')

    if file_name == '' or length < 1:
        exit('Input error. Example input: justifytext -f mytextfile -l 80')
        
    justify(file_name, length)
	
