from tinydb import TinyDB, Query

class Database:
	#easy acces to database for other classes
	def __init__(self):
		self.LaserQuery = Query()
		self.DB = TinyDB("laserDB.json")

	def change_feedrate(self, feedRate):	#insert F from canvas to change feedrate when change occurs, loop it to catch change
		feedExist = self.DB.search(self.LaserQuery.FeedRate.exists())
		feedExist = len(feedExist)

		if feedExist == 0:
			self.DB.insert({'FeedRate': feedRate})

		self.DB.update({"FeedRate":feedRate},self.LaserQuery.FeedRate.exists())

	def change_SPMM(self, StepPerMM):
		stepExist = self.DB.search(self.LaserQuery.StepsPerMM.exists())
		stepExist = len(stepExist)

		if stepExist == 0:
			self.DB.insert({'StepsPerMM': StepPerMM})

		self.DB.update({"StepsPerMM":StepPerMM},self.LaserQuery.StepsPerMM.exists())

	def change_Traveled_range(self, Traveled_range):
		rangeExist = self.DB.search(self.LaserQuery.TraveledRange.exists())
		rangeExist = len(rangeExist)

		if feedExist == 0:
			self.DB.insert({'TraveledRange': Traveled_range})

		self.DB.update({"TraveledRange":Traveled_range},self.LaserQuery.TraveledRange.exists())

	def change_prev_range(self, prev_range):
		prevRangeExist = self.DB.search(self.LaserQuery.PrevRange.exists())
		prevRangeExist = len(prevRangeExist)

		if prevRangeExist == 0:
			self.DB.insert({'PrevRange': prev_range})

		self.DB.update({"PrevRange":prev_range},self.LaserQuery.PrevRange.exists())

	def get_prev_range(self):
		values = self.DB.all()

		for x in values:
			if 'PrevRange' in x:
				return (int(x['PrevRange']))
			else:
				pass

	def get_Traveled_range(self):
		values = self.DB.all()

		for x in values:
			if 'TraveledRange' in x:
				return (int(x['TraveledRange']))
			else:
				pass

	def get_feedrate(self):
		values = self.DB.all()

		for x in values:
			if 'FeedRate' in x:
				return (int(x['FeedRate']))
			else:
				pass

	def get_SPMM(self):
		values = self.DB.all()
		#print(values)
		for x in values:
			if 'StepsPerMM' in x:
				return (int(x['StepsPerMM']))
			else:
				pass

