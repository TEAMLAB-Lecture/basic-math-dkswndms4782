def get_greatest(number_list):  
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list)/len(number_list)
    return mean


def get_median(number_list):
    median = 0
    number_list.sort()
    if number_list % 2 == 0:
        median = number_list[(len(number_list)//2) - 1)]
    else:
        median = number_list[len(number_list)//2]
    return median
