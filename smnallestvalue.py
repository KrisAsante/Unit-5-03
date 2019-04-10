# Created by: Chris Asante
# Created on: 10-April-2019
# Created for: ICS3U
# Unit 5-03
# This program will find the smallest value in the array and pass it back as a single variable

import random

def find_min_value(array = []):
    min_number = array[0]
   
    for single_number in array:
        if min_number > single_number:
            min_number = single_number           

    return min_number

counter = 0
random_numbers = []

while counter < 7:

    single_number = random.randint(1, 7 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1

smallest_value = find_min_value(random_numbers)

print("\nThe smallest value of the array is " + str(smallest_value) + ".\n")