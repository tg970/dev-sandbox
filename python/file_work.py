import os
import shutil

from_directory = "C:/Users/us59188/Desktop/"
to_directory = "C:/Users/us59188/Desktop/Sub_Folder/"
files_to_move = 3


def find_latest(dir):
    # Find the most recent file created in a given directory
    latest_file_name = ""
    latest_file_created_at = 0.0

    files_in_dir = os.listdir(dir)

    for file in files_in_dir:
        created_at = os.path.getctime(dir + file) # get time created
        if created_at > latest_file_created_at:
            latest_file_name = file
            latest_file_created_at = created_at

    return latest_file_name


def move_file(from_path, to_path):
    # move file from one path to another
    shutil.move(from_path, to_path)


def find_latest_and_move(from_dir, to_dir):
    # find the most recently created file in a directory, and move it
    file_name = find_latest(from_dir)
    print('Moving file:', file_name)
    move_file(from_dir + file_name, to_dir+ file_name)


# Move given number of recently created files
for i in range(0,files_to_move):
    find_latest_and_move(from_directory, to_directory)
