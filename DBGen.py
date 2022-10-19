import random
from itertools import product
import os


class GenerateNames:
	def __init__(self):
		# Start by listing mathematical maximum
		self.countMax = 10000

		# Lists
		self.maleNames = []
		self.femaleNames = []
		self.lastNames = []
		self.fullMaleNames = []
		self.fullFemaleNames = []
		self.allNames = []

		# workerDictionary is Birthdays
		self.workerDictionary = {}
		self.hireDates = {}

		# Files
		files = ['CommonFemaleNames.txt', 'CommonMaleNames.txt', 'CommonLastNames.txt']
		with open(files[0]) as female:
			for line in female:
				data = female.read()
				for line in data.split('\n'):
					self.femaleNames.append(line.strip('\n'))

		with open(files[1]) as male:
			for line in male:
				data = male.read()
				for line in data.split('\n'):
					self.maleNames.append(line.strip('\n'))

		with open(files[2]) as last:
			for line in last:
				data = last.read()
				for line in data.split('\n'):
					self.lastNames.append(line.strip('\n'))

	# Generate Names

	def makeMales(self, names, lastName):
		self.fullMaleNames.append(list(product(names, lastName)))

	def makeFemales(self, names, lastName):
		self.fullFemaleNames.append(list(product(names, lastName)))

	# Write Names for Processing

	def writer(self, males, females):
		count = 0
		for male in males[count]:
			first = male[0]
			last = male[1]
			count +=1
			full = str(first)+' '+str(last)
			# f.write(f"{full}\n")
			self.allNames.append(full)

		print(count)
		count = 0
		for female in females[count]:
			first = female[0]
			last = female[1]
			full = str(first)+' '+str(last)
			count += 1
			# f.write(f"{full}\n")
			self.allNames.append(full)
		print(count)

	# Randomly Select from the Many (Interviews)

	def start(self):
		nameList = []
		self.makeMales(self.maleNames, self.lastNames)
		self.makeFemales(self.femaleNames, self.lastNames)
		self.writer(self.fullMaleNames, self.fullFemaleNames)
		with open("Database.txt", 'w+') as f:
			for x in range(self.countMax):
				randomNumber = random.randint(0, 199999)
				if self.allNames[randomNumber] not in nameList:
					nameList.append(self.allNames[randomNumber])

			for name in nameList:
				f.write(name+'\n')

	# Generate Other Fake Information about Names

	def genCSV(self):
		self.malesList = []
		self.femaleList = []

		# Split Names into Males & Females Again for "Employed List"

		with open('Database1.txt', 'r') as f:
			nameList = str(f.read()).split('\n')
			for names in nameList:
				name = names.split(' ')
				if name != '' and name != ' ':
					if name[0] in self.femaleNames:
						self.femaleList.append(names)
					elif name[0] in self.maleNames:
						self.malesList.append(names)
			print(f"MalesCount: {len(self.malesList)}  \nFemalesCount: {len(self.femaleList)}")

		# Generate Hire Date and Birthdate
		longMonths = [1, 3, 5, 7, 8, 10, 12]
		shortMonths = [2, 4, 6, 9, 11]
		
		def resetRandom(leanDay, leanYearmin, leanYearmax):
			randomDay = random.randint(1, leanDay)
			randomYear = random.randint(leanYearmin, leanYearmax)
			return str(randomDay) + '/' + str(randomYear)

		def generateMales():
			for names in self.malesList:
				randomMonth = random.randint(1, 12)
				if randomMonth == 2:
					date = str(randomMonth) + '/' + str(resetRandom(28, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(28, 2013, 2022))

				elif randomMonth in longMonths:
					date = str(randomMonth) + '/' + str(resetRandom(31, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(31, 2013, 2022))

				elif randomMonth in shortMonths:
					date = str(randomMonth) + '/' + str(resetRandom(30, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(30, 2013, 2022))

				# print(f"{names}: Birthday:{date}, HireDay:{hireDate}")
				self.workerDictionary[names] = date
				self.hireDates[names] = hireDate



		def generateFemales():
			for names in self.femaleList:
				randomMonth = random.randint(1, 12)
				if randomMonth == 2:
					date = str(randomMonth) + '/' + str(resetRandom(28, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(28, 2013, 2022))

				elif randomMonth in longMonths:
					date = str(randomMonth) + '/' + str(resetRandom(31, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(31, 2013, 2022))

				elif randomMonth in shortMonths:
					date = str(randomMonth) + '/' + str(resetRandom(30, 1965, 1997))
					randomMonth = random.randint(1,12)
					hireDate = str(randomMonth) + '/' + str(resetRandom(30, 2013, 2022))

				# print(f"{names}: Birthday:{date}, HireDay:{hireDate}")
				self.workerDictionary[names] = date
				self.hireDates[names] = hireDate

		# CallFunctions for workerDictionary
		generateMales()
		generateFemales()

		# Generate PyDict
		with open("PortableDataBase.py", 'w') as f:
			f.write(f'workforceDatabasebyBDay = {self.workerDictionary}\nworkforceDatabasebyHireDay = {self.hireDates}')