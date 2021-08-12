from file_manager import copy_music_files
from pygame.mixer import music
from threading import Thread
from pathlib import Path
import pygame, pygame.mixer
import os
import time


kill_thread = False

pygame.init()
pygame.mixer.init()


class MusicPlayer:
    def __init__(self):
        self.source = Path(__file__).parent / "music_files"
        self.music_files = self.get_music_files(self.source)
        self.current_playing = 0
        self.is_playing = False
        self.is_pause = True

    def get_music_files(self, source):
        """
        Get the music files from source folder.
        """

        # copy the music files from Downloads and paste them in music_files folder
        copy_music_files()
        music_files = []
        for file in os.listdir(source):
            filepath = os.path.join(source, file)
            music_files.append(filepath)
        return music_files

    def play_pause(self):
        """
        Play or pause the music.
        """
        if not self.is_playing:
            # play the first/last song if index is out of range
            music.load(self.music_files[self.current_playing % len(self.music_files)])
            music.play()
            self.is_playing = True
        elif self.is_pause:
            music.unpause()
            self.is_pause = False
        else:
            music.pause()
            self.is_pause = True
        x = Thread(target=self.queue_next)
        x.start()

    def stop_music(self):
        """
        Stop the music.
        """
        music.stop()
        music.unload()
        self.is_playing = False

    def skip(self):
        """
        Stop the current music and play the next one.
        """
        self.stop_music()
        self.current_playing += 1
        self.play_pause()

    def previous(self):
        """
        Stop the current music and play the previous one.
        """
        self.stop_music()
        self.current_playing -= 1
        self.play_pause()

    def queue_next(self):
        """
        play the next song when one finishes.
        """
        while True:
            played = music.get_pos()
            # if the song has ended, skip to the next one
            if played == -1:
                self.skip()
            if kill_thread:
                music.stop()
            time.sleep(1)
