__author__ = 'carolynmcshea'
# Sunday 17 May 2015
# visualization of 30 most populus cities

# open a graphics window

from cs1lib import *

from quicksort import compare_ints_pop
from quicksort import sort
from sort_cities import read_parse_in_file

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 720

def visualize_cities():

    global_list = read_parse_in_file()

    # sorted by population size
    sort(global_list, compare_ints_pop)
    out_file = open("cities_population.txt", "w") # opens a file for writing

    for city in global_list:
        out_file.write(str(city) + "\n") # write the info for each city and then make a new line for the next one

    while not window_closed():
        clear
        img = load_image("world.png") # load the blank world map
        draw_image(img, 0, 0) # the reference to an object for the image returned by load_image

        for city in range(0, 50): # uses the most populated 50 cities
            draw_rectangle((global_list[city].longitude * 2) + 360, (global_list[city].latitude * 2) + 180, 10, 10) # conversion factor

            request_redraw()
            sleep(0.5) # slow sleep to show cities individually popping up

start_graphics(visualize_cities, "the world", WINDOW_WIDTH, WINDOW_HEIGHT, True) # need "True" to flip