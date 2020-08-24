from os import listdir, rename
import os.path

def rename_files():
    path = "C:/Users/RYANY/Documents/Projects/CRCaptions/data/"

    # Loop through all files in ./data
    for file_name in listdir('./data'):
        # Get the episode number
        new_file_name = f"{file_name.split(' ')[-3]}.srt"
        old_file_path = os.path.join(path, file_name)
        new_file_path = os.path.join(path, new_file_name)
        rename(old_file_path, new_file_path)

if __name__ == "__main__":
    rename_files()