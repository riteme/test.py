#!/usr/bin/env python3

#
# Copyright 2015 riteme
#

import os
import os.path
import re
import sys

from conf import *

COLOR_NONE = '\033[0m'
COLOR_BLACK = '\033[30m'
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_PURPLE = '\033[35m'
COLOR_DARK_GREEN = '\033[36m'
COLOR_WHITE = '\033[37m'


def log_info(message):
    print(
        COLOR_GREEN + '(info)' + COLOR_NONE + ' ' + message
    )


def log_warning(message):
    print(
        COLOR_YELLOW + '(warn)' + COLOR_NONE + ' ' + message
    )


def log_error(message):
    print(
        COLOR_RED + '(error)' + COLOR_NONE + ' ' + message
    )


def log_fatal(message):
    print(
        COLOR_PURPLE + '(fatal)' + COLOR_NONE + ' ' + message
    )


def log_debug(message):
    if not DEBUG_OUTPUT:
        return

    print(
        COLOR_DARK_GREEN + '(debug)' + COLOR_NONE + ' ' + message
    )


def match_test(filename):
    result = re.match(REGEX_PATTERN, filename)
    return result is not None


def compile_test(filename):
    log_info('Compiling {}...'.format(filename))

    attach = []
    for key in ATTACH_SOURCE:
        if key in filename:
            attach = ATTACH_SOURCE[key]
            break

    if len(ATTACH_LIBRARY) > 0:
        for i in range(0,len(ATTACH_LIBRARY)):
            attach.append('-l{}'.format(ATTACH_LIBRARY[i]))

    attached_files = ''
    if attach is not None:
        attached_files = ' '.join(attach)

    command = '{0} {1} {2} -o {3}'.format(
        COMPILER,
        filename,
        attached_files,
        RUN_COMMAND
    )
    result = os.system(command)

    log_debug('Run: ' + command)

    if result == 0:
        return True
    else:
        log_error(
            'Compilation failed! Compiler returned {}'.format(result)
        )
        return False


def run_test(filename):
    if not compile_test(filename):
        log_error('Cannot run the test.')
        return False
    else:
        log_info('Running {}...'.format(filename))

        result = os.system(RUN_COMMAND)

        if result == 0:
            log_info(
                COLOR_GREEN + 'PASSED' + COLOR_NONE + ': {}'.format(filename))
            return True
        else:
            log_error(
                COLOR_RED + 'FAILED' + COLOR_NONE + ': {}'.format(filename))
            return False

# Main
if __name__ != '__main__':
    log_warning('This program may run in a uncorrect situation.')

log_info('Running all the tests...')

test_list = None
if len(sys.argv) > 1:
    test_list = sys.argv[1:]
else:
    test_list = os.listdir()

status = 0
count = 0
passed_count = 0
failed_count = 0
unpassed = []

for filename in test_list:
    if not match_test(filename):
        continue  # Not a unittest.

    count += 1

    if not run_test(filename):
        status = -1
        failed_count += 1
        unpassed.append(filename)
    else:
        passed_count += 1

if count == 0:
    log_error('No test has been run.')
    exit(-1)

log_info('Unittest Report:')
print('\tTested {} unittest(s).'.format(count))
print('\t{} passed, {} failed.'.format(passed_count, failed_count))
print('\tPassed Ratio: {:.2f}%'.format(
    (float(passed_count) / float(count)) * 100.0))

if len(unpassed) != 0:
    print('\tUnpassed: \n\t\t' + COLOR_YELLOW +
          '{}'.format(',\n\t\t'.join(unpassed)) + COLOR_NONE)

log_info('Program exited.')
exit(status)
