import sys
import os
import subprocess
'''
Given a file containing file names, a hash algorithm (one of MD5 / SHA1 / SHA256) and their 
corresponding hash sums, calculated by the corresponding algorithm and indicated in 
the file with a space. Write a program that reads this file and checks the integrity of the 
files using either the standard Python library or the md5sum / sha1sum / sha256sum program.
'''

if len(sys.argv) < 3:
    print(f'Error. Not enough arguments, expected: 3, got: {len(sys.argv)}')
    exit()
filename = sys.argv[1]
directory_path = sys.argv[2]

if os.path.isfile(filename) and os.path.isdir(directory_path):
    with open(filename) as input_file:
        for line in input_file:
            if len(line.split()) != 3:
                print(f'Not enough arguments in string, expected: 3, got: {len(line.split())}.'
                      f' The current line will be skipped')
                continue
            current_string = line.strip().split()
            current_file, encoding, file_sum = current_string
            if encoding not in ['sha1', 'md5', 'sha256']:
                print(f"{current_file} WRONG ENCODING")
                continue

            if os.path.isfile(f"{directory_path}/{current_file}"):
                command = f"{encoding}sum {directory_path}/{current_file}"
                get_sum = subprocess.check_output(command.split()).decode("utf-8").split()[0]
                result = f"{current_file} OK" if get_sum == file_sum else f"{current_file} FAIL"
                print(result)
            else:
                print(f"{current_file} NOT FOUND")
