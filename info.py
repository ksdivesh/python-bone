import my_module
import my_module as mm
from my_module import find_index as fi, test
from my_module import *

import sys

courses = ['History', 'Math', 'Physics', 'ComputerSc']

index = find_index(courses, 'Math')

print(index)
print(test)

print(sys.path) #In machine, the path where python looks for module