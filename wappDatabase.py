#Optimised functions to do a lot of stuff
import numpy as np
#To utilise the pandas dataframe
import pandas as pd
#Makes a datetime object of a date, also used to see if dates are valid
from datetime import datetime as dt
#To read in command-line options
from getopt import getopt
#To get the command-line options
import sys
#To check if files exist
import os

class wappDatabase:
	def __init__(self, readFromFile, nameConversionFile, 
							 dataframeToLoad, saveToDifferentFile,
							 nameDifferentFile):
		"""
		Initialise the class, giving default or given values to variables.
		Parameters:
			- readFromFile: Name of the file which contains the chat.
			- nameConversionFile: Name of the file containing the name conversions.
				See function readInNCF() for more information.
			- dataframeToLoad: Name of the file which contains an already existing
				database. Empty otherwise. See _loadDatabase() and _extractDatabase()
				for more information.
			- saveToDifferentFile: Boolean which determines whether to save in the
				same file as the existing database is read out, or in a new file.
				Cannot be False if dataframeToLoad was empty.
			- nameDifferentFile: Name of file to save the database to. Cannot be
				empty	if saveToDifferentFile is True.
		"""
		self.rff = readFromFile
		self.ncf = nameConversionFile
		self.dftl = dataframeToLoad
		self.namesDict = {} #empty dictionary
		self.peopleWhoLeft = []
		self.peopleAdded = []
		self.peopleWhoGotRemoved = []
		self.changesInName = []
		
	def _extractDatabase(self, database):
		"""
		Extracts the different lists and other data from the database object given.
		It contains:
		[0] - Pandas dataframe containing messages
		[1] - List of people who left the chat
		[2] - List of people who were added to the chat
		[3] - List of people who got removed from the chat
		[4] - List of all the changes in the name of the chat
		"""
		try:
			self.dataframe = database[0]
			self.peopleWhoLeft = database[1]
			self.peopleAdded = database[2]
			self.peopleWhoGotRemoved = database[3]
			self.changesInName = database[4]
			return True
		except ExplicitException as e:
			print(e)
			print("Database object could not be read!")
			return False
	
	
	def _loadDatabase(self):
		"""
		Checks if the given path to the previous database exists, and then
		loads that database in self.database if it does exist.
		Otherwise returns False, so a new database can be made.
		The previous database is assumed to have the same columns as this
		program enforces.
		"""
		if self.dftl != "" and os.path.isfile(self.dftl):
			try:
				database = np.load(self.dftl)
				return self._extractDatabase(database)
			except (IOError, ValueError) as e: #the exceptions load() can give
				print(e)
				print("Database file could not be read!")
		return False
		
	def _createDatabase(self):
		"""
		Either the dataframe is loaded using the function _loadDataFrame(),
		or an empty dataframe is made with the column names as can be set 
		in this function.
		"""
		if (not(loadDataframe())):
			columnNames = ['Date', 'Time', 'Name', 'Message']
			self.dataframe = pd.DataFrame(columns = columnNames)
			
	def _updateLeft(self, date, time, person):
	#temporary function (maybe)
		self.peopleWhoLeft.append([date, time, person])
	
	def _updateAdded(self, date, time, person):
	#temporary function (maybe)
		self.peopleAdded.append(date, time, person)
		
	def _updateRemoved(self, date, time, removingPerson, personRemoved):
	#temporary function (maybe)
		self.peopleWhoGotRemoved.append(date, time, removingPerson, personRemoved)
		
	def _updateChanges(self, date, time, person, oldName, newName):
	#temporary function (maybe)
		self.changesInName.append(date, time, person, oldName, newName)
		
	def _checkDate(self, date):
		"""
		Checks whether the given string is in one of the acceptable date formats.
		If so, a datetime object is returned. Otherwise, False is returned.
		"""
		for dateFormat in ("%d/%m/%y", "%m/%d/%y"): #maybe add more as they come along
			try:
				return dt.strptime(date, dateFormat)
			except ValueError: #the string is not a date in the given format
				pass
		return False 
	
	def _checkLine(self, line):
		"""
		Checks the given line of the chat, and checks whether it is a valid message 
		or not. If it is not the function ends with an empty return, and otherwise 
		the database is updated.
		Each line given is one of the following:
		- <date>, <time> - <name>: <message> (name can contain spaces)
		- <message> (extended message of previous poster)
		- <date>, <time> - <name> left
		- <date>, <time> - <name> created group <groupname>
		- <date>, <time> - <name> added <name>
		- <date>, <time> - <name> removed <name>
		- <date>, <time> - <name> changed the subject from <groupname> to
			<groupname>
		- <date>, <time> - <message about encryption>
		"""
		ls = line.split(" ")
		#check for the date, don't include the ','
		date = self._checkDate(ls[0][:-1])
		if(date == False): #there is no date
			return #return as this message doesn't matter
		
		
		
	
	def readInRFF(self):
		"""
		Read in the log file containing the chat messages.
		Then 
		"""
		with open(self.rff, 'r') as rff:
			for line in rff:
				self._checkline(line)
			
	def readInNCF(self):
		"""
		Reads in the Name Conversion File, which holds information
		as to which name in the chat log corresponds to which name
		in the main database.
		The NCF is assumed to have each line consisting of
		<logName> -> <databaseName>
		so for example
		Klaas Dinges -> Klaas Sint
		This information is then stored in a dictionary, so any
		occurances of the logName can be immediately replaced.
		"""
		with open(self.ncf, 'r') as ncf:
			for line in ncf:
				ls = line.split(" -> ")
				self.namesDict[ls[0]] = ls[1]
		
#do something with getopt to get all the terminal input
def printHelp():
	print(
		"""
		
		"""
	)

def parseCommands(commands):
	"""
	Read out the options given, with their respective values if present, and
	call the class with the appropriate data given.
	"""
	options, values = getopt(commands, )

if __name__=="__main__":
	parseCommands(sys.argv[1:])
