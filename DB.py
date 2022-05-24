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

	def change_SPMM(self, SetpPerMM):
		stepExist = self.db.search(self.LaserQuery.StepsPerMM.exists())
		stepExist = len(stepExist)

		if stepExist == 0:
			self.db.insert({'StepsPerMM': StepPerMM})

		self.db.update({"StepsPerMM":StepPerMM},self.LaserQuery.StepsPerMM.exists())

	def get_feedrate(self):
		values = self.DB.all()

		for x in values:
			if 'FeedRate' in x:
				return (int(x['FeedRate']))
			else:
				pass

	def get_SPMM(self):
		values = self.DB.all()
		print(values)
		for x in values:
			if 'StepsPerMM' in x:
				return (int(x['StepsPerMM']))
			else:
				pass

