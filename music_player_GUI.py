from shutil import move
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from win32api import GetSystemMetrics
from BlurWindow.blurWindow import blur
from music_player import MusicPlayer
import music_player

music = MusicPlayer()


class MainWindow(QMainWindow):
    def __init__(self, title) -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        # make the background translucent and blur it.
        self.setAttribute(Qt.WA_TranslucentBackground)
        hWnd = self.winId()
        blur(hWnd, Dark=True, Acrylic=True)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_bar)
        self.current_second = 0
        self.is_playing = False
        self.seconds = 0
        self.currently_playing = 0
        self.music_player = MusicPlayer()
        self.MainUI()

    def MainUI(self):
        self.previous_button()
        self.play_button()
        self.next_button()
        self.seek_bar()
        self.show()
        self.showMaximized()

    def play_button(self):
        """
        Play button to play or pause the music
        """
        self.play_btn = QPushButton("", self)
        self.play_btn.setIcon(QIcon("images\play-button.png"))
        self.play_btn.setIconSize(QSize(50, 50))
        self.adjustSize()
        self.play_btn.setGeometry(
            round(self.width // 2), round(self.height // 1.2), 80, 80
        )
        self.play_btn.clicked.connect(self.play)

    def previous_button(self):
        """
        Button to play the previous song
        """
        self.prev_btn = QPushButton("", self)
        self.prev_btn.setIcon(QIcon("images\previous.png"))
        self.prev_btn.setIconSize(QSize(50, 50))
        self.adjustSize()
        self.prev_btn.setGeometry(
            round(self.width // 2.3), round(self.height // 1.2), 80, 80
        )

        self.prev_btn.clicked.connect(self.prev)

    def next_button(self):
        """
        Button to play the next song
        """
        self.nxt_btn = QPushButton("", self)
        self.nxt_btn.setIcon(QIcon(r"images\next.png"))
        self.nxt_btn.setIconSize(QSize(50, 50))
        self.adjustSize()
        self.nxt_btn.setGeometry(
            round(self.width // 1.75), round(self.height // 1.2), 80, 80
        )

        self.nxt_btn.clicked.connect(self.skip)

    def seek_bar(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(20, self.height - 250, self.width - 50, 15)
        self.slider.setMinimum(0)
        self.slider.setMaximum(music.get_song_length() - 10)
        self.slider.setTickInterval(1)
        self.slider.sliderReleased.connect(self.seek_song)

    def play(self):
        """
        play or pause the song
        """
        self.music_player.play_pause()
        self.is_playing = not self.is_playing
        self.timer.start(1000)

    def skip(self):
        """
        skip the song
        """
        self.is_playing = True
        music_player.current_playing += 1
        self.music_player.skip()
        self.slider.setValue(0)
        self.slider.setMaximum(music.get_song_length() - 10)
        self.move_bar()
        self.timer.start(1000)
        self.seconds = 0

    def prev(self):
        """
        play previous song
        """
        self.is_playing = True
        music_player.current_playing -= 1
        self.music_player.previous()
        self.slider.setValue(20)
        self.slider.setMaximum(music.get_song_length() - 10)
        self.move_bar()
        self.timer.start(1000)
        self.seconds = 0

    def move_bar(self):
        if self.is_playing:
            self.slider.setValue(self.seconds)
            self.seconds += 1

    def seek_song(self):
        self.music_player.seek_song(self.slider.value())
        self.slider.setValue(self.slider.value())
        self.seconds = self.slider.value()


def get_stylesheet():
    with open("styles\stylesheet.qss") as file:
        return file.read()


def main():
    app = QApplication(sys.argv)
    window = MainWindow("Music Player")
    window.show()
    # if the app is executed, stop the thread so it doesn't play the music in background
    if not app.exec():
        music_player.kill_thread = True
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
