__author__ = 'carolynmcshea'
# Sunday 10 May 2015
# reads and parses world_cities.txt

from city import City

def read_parse_in_file():

    in_file = "world_cities.txt"

    city_list = open(in_file, "r") # opens "world_cities.txt" for reading

    global_list = [] # creates an empty list to store edited city list

    for line in city_list:
        stripped_line = line.strip() # takes extra characters at the beginning and end off
        split_line = stripped_line.split(",") # splits the string into a list with each item separate

        new_city = City(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5]) # creates a new City object

        global_list.append(new_city) # adds the new city object to the empty list

    return global_list # returns the new list (now full)

    city_list.close() # closes the original file

read_parse_in_file()




