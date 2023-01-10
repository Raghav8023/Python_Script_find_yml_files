import os
import os

all_count = 0
yml_count = 0
all_files = []
yml_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        
        all_count += 1
        all_files.append(file)
        
        if file.endswith(".yml"):
            yml_count += 1
            yml_files.append(file)

print("Total number of files:", all_count)
print("Total number of .yml files:", yml_count)
print("List of All files:", all_files)
print("List of all .yml files:", yml_files)
