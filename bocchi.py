from krita import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import vlc as v
import random
from pathlib import Path

song_dir = Path(__file__).parent / 'songs'
song_files = list(song_dir.rglob('*.mp3'))

class bocchi(QWidget):
    def __init__(self, parent=None):
        super.__init__(parent)

        self.sprite = QLabel()
        self.setdimensions()
        self.sprite.mousePressEvent = self.clicked

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.labelbutton)
        self.setLayout(self.layout)
        self.setFixedSize(self.width, self.height)
        
    def setdimensions(self):
        self.img = QPixmap(str(Path(__file__).parent / "images" / "bocchi1nobg.png"))
        self.img.start()
        self.width = round(self.img.frameRect().width()/10)
        self.height = round(self.img.frameRect().height()/10)

    def clicked(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            p.stop()
            file = random.choice(song_files)
            p = v.MediaPlayer(file)
            p.play()
        elif event.button() == Qt.MouseButton.RightButton:
            p.stop()
    
    for docker in Krita.instance().dockers():
        if(docker.objectName() == 'bocchi'):
           docker.setVisible(docker.isVisible())
        
