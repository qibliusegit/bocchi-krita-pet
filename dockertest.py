from PyQt6.QtWidgets import *
from krita import *

class MyDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Docker")

        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        buttonExportDocument = QPushButton("Export Document", mainWidget)

        buttonExportDocument.clicked.connect(self.exportDocument)

    def exportDocument(self):
        print("Export button clicked!")
         
    def canvasChanged(self, canvas):
        pass
Krita.instance().addDockWidgetFactory(DockWidgetFactory("myDocker", DockWidgetFactoryBase.DockPosition.DockRight, MyDocker))
