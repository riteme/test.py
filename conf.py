#
# Copyright 2015 riteme
#

DEBUG_OUTPUT = True
COMPILER = 'g++ -std=c++11 -O0 -g'
RUN_COMMAND = './test.out'
REGEX_PATTERN = 'test_.*\.cpp'

ATTACH_LIBRARY = []

# "testname1": ["attached_files"],
# "testname2": ["attached_files"]
ATTACH_SOURCE = {}
