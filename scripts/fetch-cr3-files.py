import argparse
from ast import arguments
import os
from os import listdir
from os.path import isfile, join, exists
import shutil

def get_cr3_for_jpg(jpg, cr3_files):
    """
    """
    for cr3_file in cr3_files:
        filename, _ = cr3_file.split('.')
        if jpg == filename:
            return cr3_file

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('path_to_jpgs', type=str)
argument_parser.add_argument('path_to_cr3', type=str)
argument_parser.add_argument('cr3_dst', type=str)
arguments = argument_parser.parse_args()

path_to_jpgs = arguments.path_to_jpgs
path_to_cr3 = arguments.path_to_cr3
cr3_dst = arguments.cr3_dst

jpgs = []
for root, dirs, files in os.walk(path_to_jpgs, topdown=False):
    jpgs.extend([os.path.join(root, f) for f in files if 'JPG' in os.path.basename(f).split('.')[1]])

# jpgs = [f.split('.')[0] for f in listdir(path_to_jpgs) if isfile(join(path_to_jpgs, f))]
# if not jpgs:
#     raise Exception(f"No jpgs found in {path_to_jpgs}")

print(jpgs)
import pdb; pdb.set_trace()
print(len(jpgs))

print("Fetching respective CR3 files.")

cr3_files = listdir(path_to_cr3)

print(cr3_files)

# print("copying files over to cr3 dst " + cr3_dst)
# for cr3_file in cr3_files:
#     print(f"Copying {cr3_file} to {cr3_dst}")
#     if not exists(join(cr3_dst, cr3_file)):
#         shutil.copy(join(path_to_cr3, cr3_file), cr3_dst)
#     else:
#         print(f"Skipping {cr3_file}, already exists.")
import pdb; pdb.set_trace()

for jpg in jpgs:
    # Get the CR3 file for the jpg.
    basename = os.path.basename(jpg).split('.')[0]
    basepath = os.path.dirname(jpg)
    cr3_file = get_cr3_for_jpg(jpg=basename, cr3_files=cr3_files)
    if cr3_file is None:
        print(f"Unable to find CR3 file for jpg {jpg}")
        continue
    cr3_dst = os.path.join(basepath, cr3_file)
    if not exists(cr3_dst):
        print(f"Copying {join(path_to_cr3, cr3_file)} to {cr3_dst}")
        # shutil.copy(join(path_to_cr3, cr3_file), cr3_dst)
    else:
        print(f"Skipping {cr3_dst}, already exists.")
