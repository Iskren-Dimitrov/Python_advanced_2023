'''Write a program that traverses a given directory for all files. Search through the first level of the directory\
only and write information about each found file in report.txt. The files should be grouped by their extension.\
Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name.\
report.txt should be saved in the chosen directory.
'''

import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)  # dir_name + / + filename

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:  # first_level == False
            save_extensions(file, first_level=True)


directory = input()
extensions = {}  # ex. {.py: [hello_world.py, z_file.py]}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - -{file}")

with open(f"files/report.txt", "w") as file:
    file.write("\n".join(result))
