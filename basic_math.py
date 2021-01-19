import numpy as np
def get_greatest(number_list):  
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = np.mean(number_list)
    return mean


def get_median(number_list):
    median = np.median(number_list)
    return median
