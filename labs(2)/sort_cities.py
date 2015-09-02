__author__ = 'carolynmcshea'
# Sunday 17 May 2015
# takes sorted city lists and writes them into 3 separate files
# cities_alpha.txt, cities_population.txt, and cities_latitude.txt


from city import City

from quicksort import compare_ints_pop
from quicksort import compare_ints_lat
from quicksort import compare_strings
from quicksort import sort

def read_parse_in_file():

    in_file = "world_cities.txt"

    city_list = open(in_file, "r") # opens "world_cities.txt" for reading

    global_list = [] # creates an empty list to store unsorted city list

    for line in city_list:

        stripped_line = line.strip() # takes extra characters at the beginning and end off
        split_line = stripped_line.split(",") # splits the string into a list with each item separate

        new_city = City(split_line[0], split_line[1], split_line[2], int(split_line[3]), float(split_line[4]), float(split_line[5])) # creates a new City object

        global_list.append(new_city) # adds the new city object to the empty list

    return global_list # returns the new list (now full)

    city_list.close() # closes the original file

read_parse_in_file()



# sorts global list by the cities' names
def sort_by_names():
    global_list = read_parse_in_file()
    sort(global_list, compare_strings)
    out_file = open("cities_alpha.txt", "w") # opens a file for writing

    for city in global_list:
        out_file.write(str(city) + "\n") # write the info for each city and then make a new line for the next one



# sorts global list by the cities' populations
def sort_by_population():
    global_list = read_parse_in_file()
    sort(global_list, compare_ints_pop)
    out_file = open("cities_population.txt", "w") # opens a file for writing

    for city in global_list:
        out_file.write(str(city) + "\n") # write the info for each city and then make a new line for the next one

    return global_list


# sorts global list by the cities' latitudes
def sort_by_latitude():
    global_list = read_parse_in_file()
    sort(global_list, compare_ints_lat)
    out_file = open("cities_latitude.txt", "w") # opens a file for writing

    for city in global_list:
        out_file.write(str(city) + "\n") # write the info for each city and then make a new line for the next one


sort_by_names()
sort_by_population()
sort_by_latitude()



