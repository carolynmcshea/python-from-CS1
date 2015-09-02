__author__ = 'carolynmcshea'
# Saturday 9 May 2015
# city class

class City:
    def __init__(self, country, name, region, population, latitude, longitude):
        self.country = country # 2 letter string
        self.name = name # string
        self.region = region # 2 letter string
        self.population = population # int
        self.latitude = latitude # float
        self.longitude = longitude # float

    def __str__(self):
        return (self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude))

hanover = City("us", "hanover", "northeast", 229000, 38.0, 40.0) # creates a city object