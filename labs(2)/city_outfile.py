__author__ = 'carolynmcshea'
# Sunday 10 May 2015
# creates an output file for world_cities.txt

from city_infile import read_parse_in_file

def create_outfile(global_list):

    out_file = open("cities_out.txt", "w") # opens a file for writing

    for city in global_list:
        out_file.write(str(city) + "\n") # write the info for each city and then make a new line for the next one

n = read_parse_in_file() # n is a temp variable that stores the output of read_parse_in_file

create_outfile(n) # calls the function