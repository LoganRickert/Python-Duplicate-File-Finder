# Written by Logan Rickert
# Februray 28th, 2015
# This document is in CC0 1.0 Universal (CC0 1.0)
# https://creativecommons.org/publicdomain/zero/1.0/

# This program recrusively goes through all directories and files in the C directory
# and reports back to the user the files that are duplicates.
# This program generates an MD5 sum for each file and stores it in a dictonary.

# If an error is thrown when opening up the file to generate an MD5 sum, the file
# is closed and is not added to md5_sums nor dupe_file_paths and the error is
# reported to the user.

#############################
#          imports          #
#############################
import os
import glob
import hashlib

# The initial directory you wish to start at.
# The program will not go outside of this directory.
initial_file_directory = 'C:\\Users\\Logan\\Desktop\\Easy_Longboarding_15'

# Holds the md5 sums for all of the files.
md5_sums = {}

# Holds the file path to all of the duplicate files.
dupe_file_paths = []

# Sources:
# http://bogdan.org.ua/2007/08/12/python-iterate-and-read-all-files-in-a-directory-folder.html#comment-103404
# http://www.pythoncentral.io/hashing-files-with-python/

#############################
#          Methods          #
#############################

def scan_dirs(path):
    """Recursively goes through each directory and adds the md5 sum
    to the md5_sums dictionary. If the md5 sum has already been added,
    it is added to dupe_file_paths.

    Most of the code came from:
    http://bogdan.org.ua/2007/08/12/python-iterate-and-read-all-files-in-a-directory-folder.html#comment-103404
    """
    for current_file in glob.glob( os.path.join(path, '*') ):
        # If the file is a directory, scan that directory
        if os.path.isdir(current_file):
            scan_dirs(current_file)
        else:
            current_sum = md5_sum(current_file)
            # If the sum is 0, there was an error with the file.
            if current_sum != 0:
                if current_sum in md5_sums:
                    dupe_file_paths.append(current_file)
                else:
                    md5_sums[md5_sum(current_file)] = current_file

def md5_sum(filename):
    """Figures out the md5 sum for a file given through the filename.
    If the file has an error on opening, the MD5sume comes back as 0.

    Source:
    http://www.pythoncentral.io/hashing-files-with-python/
    """
    BLOCKSIZE = 65536
    hasher = hashlib.md5()

    # Makes sure file can be read. May be come back permission denied.
    try:
        with open(filename, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()
    except:
        print("Error reading the file: " + filename)
        return "0"

def print_md5_dictonary():
    """Goes through the md5 dictionary and prints out the md5 sums
    along with the complete file path for error checking.
    """
    for md5_sum, path in md5_sums.items():
        print(md5_sum + " " + path)

#############################
#   Start of the program    #
#############################

# Scans the directories and fills the md5_sums and dupe_file_paths
scan_dirs(initial_file_directory)

# Prints out all of the duplicate files
print("Duplicate files: ")
for file_path in dupe_file_paths:
    print(file_path)
