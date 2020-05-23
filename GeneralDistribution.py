class Distribution:

    
	def __init__(self, mu=0, sigma=1):
	
		""" General distribution class for calculating and 
		visualizing a probability distribution.
	
		Attributes:
			mean (float) representing the mean value of the distribution
			stdev (float) representing the standard deviation of the distribution
			data (list of floats) a list of values extracted from the data file
			"""
		
		self.mean = mu
		self.stdev = sigma
		self.data = []  


	def read_data_file(self, file_name):
	
		"""Function to read data from a text file. The text file should have one value/line .
				
		Args:
			file_name (string): name of a text file to read from
		
		Returns:
			None
		
		"""
			
		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()
	
		self.data = data_list

