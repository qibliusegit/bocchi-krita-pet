from krita import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import vlc as v
import random
from pathlib import Path

p = ""
song_dir = Path(__file__).parent / 'songs'
song_files = list(song_dir.rglob('*.mp3'))

class bocchi(DockWidget):
    def __init__(self):
        super.__init__()
        self.setWindowTitle("bocchi_mp3")
        self.img = QPixmap(str(Path(__file__).parent / "images" / "bocchi1nobg.png"))

        self.labelbutton = QLabel()
        self.labelbutton.setPixmap(self.img)
        self.labelbutton.mousePressEvent = self.clicked

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelbutton)
        
       
        self.setFixedSize(self.width, self.height)

        self.rootwidget = QWidget(self)
        self.rootwidget.setLayout(self.layout)
        self.rootwidget.setdimensions()
        
    def setdimensions(self):
        self.rootwidget.width = round(self.img.width()/10)
        self.rootwidget.height = round(self.img.height()/10)

    def clicked(self, event):
        global p
        if p == "":
            if event.button() == Qt.MouseButton.LeftButton:
                file = random.choice(song_files)
                p = v.MediaPlayer(file)
                p.play()
            elif event.button() == Qt.MouseButton.RightButton:
                print("hi")
        if event.button() == Qt.MouseButton.LeftButton:
            p.stop()
            file = random.choice(song_files)
            p = v.MediaPlayer(file)
            p.play()
        elif event.button() == Qt.MouseButton.RightButton:
            p.stop()

    def canvasChanged(self, canvas):
        pass


Krita.instance().addDockWidgetFactory(DockWidgetFactory("bocchimp3", DockWidgetFactoryBase.DockPosition.DockRight, bocchi))
    
for docker in Krita.instance().dockers():
    if(docker.objectName() == 'bocchi'):
        docker.setVisible(docker.isVisible())

a = bocchi()