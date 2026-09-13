from krita import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import vlc as v
import random
from pathlib import Path

p = "" # holds song name
playing = False # checks if song is playing
song_dir = Path("change to your file path!") 
song_files = list(song_dir.rglob('*.mp3')) # finds specifically mp3 files in the file path you gave it

class bocchi(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bocchi_mp3")
        self.img = QPixmap(str(Path(__file__).parent / "images" / "bocchi1nobg.png"))

        self.labelbutton = QLabel()
        self.labelbutton.setPixmap(self.img)
        self.labelbutton.mousePressEvent = self.clicked

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelbutton)
        
       
        self.rootwidget = QWidget(self)
        self.rootwidget.setFixedSize(200, 100)
        self.rootwidget.setLayout(self.layout)
        self.setWidget(self.rootwidget)

    def clicked(self, event):
        global p
        global playing
        self.img = QPixmap(str(Path(__file__).parent / "images" / "bocchi2nobg.png")) # switches picture
        self.labelbutton.setPixmap(self.img)
        if p == "":
            if event.button() == Qt.MouseButton.LeftButton: # plays new track 
                file = random.choice(song_files)
                p = v.MediaPlayer(file)
                p.play()
                playing = True
            elif event.button() == Qt.MouseButton.RightButton: # doesn't do anything, since there's not a song playing alr
                print("hi")
        if event.button() == Qt.MouseButton.LeftButton: # plays new track 
            p.stop()
            file = random.choice(song_files)
            p = v.MediaPlayer(file)
            p.play()
            playing = True
        elif event.button() == Qt.MouseButton.RightButton: # plays/pauses current track if right clicked
            if playing:
                p.pause()
                playing = False
            else:
                p.play()
                playing = True
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.switch)
        self.timer.start(500) # waits half a second before switching back to the original image
        
    def switch(self):
        self.img = QPixmap(str(Path(__file__).parent / "images" / "bocchi1nobg.png"))
        self.labelbutton.setPixmap(self.img)
        self.timer.stop()

        
        
        
        

    def canvasChanged(self, canvas):
        pass


Krita.instance().addDockWidgetFactory(DockWidgetFactory("bocchimp3", DockWidgetFactoryBase.DockPosition.DockRight, bocchi))
    
for docker in Krita.instance().dockers():
    if(docker.objectName() == 'bocchi'):
        docker.setVisible(docker.isVisible())
