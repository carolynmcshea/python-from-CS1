__author__ = 'carolynmcshea'
# Sunday 17 May 2015
# sorts cities according to various criteria via recursive quicksort function


def partition(list, p, r, compare_func):

    i = p-1 # initial value for i

    pivot = list[r] # pivot is the value of index r

    for j in range(p, r):

        # to switch from largest to smallest, reorder list[j] and pivot
        if not compare_func(list[j], pivot):
        # if the value of j is greater than pivot, increase j by 1 (do nothing)
        # if the value of j is less than pivot, increase i by 1 and switch the values of i and j
            i += 1
            (list[i], list[j]) = (list[j], list[i])

    # when j gets to r, assign the value of j to the index i+1 (inbetween the two groups) and return that index
    (list[i+1], list[r]) = (list[r], list[i+1])
    return i+1



from string import lower

def compare_ints_pop(city1, city2): # compares the populations sizes or latitudes of 2 cities
    return city1.population <= city2.population

def compare_ints_lat(city1, city2): # compares the populations sizes or latitudes of 2 cities
    return city2.latitude <= city1.latitude

def compare_strings(city1, city2): # compares the names of 2 cities
    return lower(city2.name) <= lower(city1.name)



def quicksort(list, p, r, compare_func):

    if p < r:
        q = partition(list, p, r, compare_func) # assign q the returned value of partition
        quicksort(list, p, q-1, compare_func) # recursively quicksort the lists on either side of q
        quicksort(list, q+1, r, compare_func)


def sort(list, compare_func):
    quicksort(list, 0, len(list)-1, compare_func)
