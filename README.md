# Music Player
A music player made by using PyQt5 and PyGame.

---
# How it works

## File Manager

Let's start with `file_manager.py`. This file is responsible for getting `mp3` and `mp4` files from the `Downloads` folder of your PC.
After that, it copies the files from the folder and pastes it in `music_files` folder. This is made so you don't have to copy and paste the files manually everytime you download a song.

## Music Player

This is the heart of the app. It plays, pauses, skips and plays the previous song. To do all of this, it uses PyGame.

## Music Player GUI

This controls GUI (Graphical User Interface) of the app. In order to make it smoother, I used Threading. The music will play in the background and you can easily interact with the GUI.

---
## How to use it

In order to use it, download the code from GitHub and make sure to make a folder named `music_files`. Make sure the folder is in the same folder where `file_manager.py` is. Also, make sure you have installed the requirements from `requirements.txt`.

---
Enjoy!

