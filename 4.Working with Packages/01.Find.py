from sys import argv
from os import walk, path

def find_file(start_directory: str, file_name: str):

    paths = []

    if file_name.endswith("*"):
        file_name = file_name[:-1]  # remove the * from the file name

        for dirpath, _, filenames_list in walk(start_directory):

            for file in filenames_list:

                if file.startswith(file_name):

                    path_to_file = path.join(dirpath, file)
                    paths.append(path_to_file)

    else:
        for dirpath, _, filenames_list in walk(start_directory):

            if file_name in filenames_list:
                path_to_file = path.join(dirpath, file_name)

                paths.append(path_to_file)

    return paths

##########################################

if len(argv) >= 3:
    start_directory = argv[1]  # /home/netherblood/Downloads
    file_name = argv[2] # jen* OR jenata na marto.jpg

    result = find_file(start_directory, file_name)

    if result:
        if len(result) == 1:
            print("The full path to the file you were searching for is: {}".format(result[0]))
        else:
            print("Multiple files were found, here are their paths:")
            for path in result: print(path)
    else:
        print("Could not find the file you were searching for.")
else:
    print("Please provide two parameters - the directory to search in and the name of the file. :)")