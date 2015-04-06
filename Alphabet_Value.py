import sys # Basic import statement

di = {} # Creating a basic dictionary to store the key value pair for the alphabets, this is a global dictionary

'''since,
	A = 1, B=A*2+2 and so on, here applying a basic formula i.e. taking mul as 0 and keep on reassigning it's values on the go .
'''

def makeDict(): # Creating a function makeDict
	mul = 0
	increment = 1
	for i in range(65,91): # Iterating over a range of ascii values
		di[chr(i)] = mul*2+increment #chr() function converts integer to it's corresponding ascii
		mul = di[chr(i)] # Re-assigning mul for the next value
		increment = increment + 1 

# This function calculates the sum of the alphabets you pass on
def calculateSum(string):
	number_list = [] # A blank list is created
	str = string.upper() # Converting to the Upper Case of String if not and storing in str
	list_str = list(str) 
	getNumberList(list_str, number_list) # Calling function getNumberList
	print ('The sum is ', sum(number_list)) # Printing the sum

#This function accepts the string list and converts it to it corresponding number list
def getNumberList(list_str, number_list):
	for i in list_str:
		number_list.append(di[i])


if __name__=='__main__':
	makeDict()
	value = input("Enter the Alphabets : ")
	calculateSum(value)
	#getCorrespondingLetters(1324)
