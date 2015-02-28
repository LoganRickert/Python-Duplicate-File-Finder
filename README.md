# Python-Duplicate-File-Finder
This program recrusively goes through all directories and files in the C directory and reports back to the user the files that are duplicates. This program generates an MD5 sum for each file and stores it in a dictonary.

If an error is thrown when opening up the file to generate an MD5 sum, the file is closed and is not added to md5_sums nor dupe_file_paths and the error is reported to the user.
