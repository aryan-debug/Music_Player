import os
import shutil
from pathlib import Path

source = Path.home() / "Downloads"
destination = Path(__file__).parent / "music_files"


def get_files(directory, *extensions):
    """
    Get the files in the directory that match the extensions
    """
    music_list = []
    for subdirs, dirs, files in os.walk(directory):
        for file in files:
            for extension in extensions:
                if file.endswith(extension):
                    filepath = subdirs + os.sep + file
                    music_list.append(filepath)
    return music_list


def copy_files(source, destination):
    """
    Copy the files to a destination
    """
    for file in source:
        shutil.copy2(file, destination)


def copy_music_files():
    """
    sort of the main function
    """
    extensions = ("mp3", "mp4")
    file_location = get_files(source, extensions)
    copy_files(file_location, destination)


if __name__ == "__main__":
    copy_music_files()
