from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.closeApplicationButton = None
        self.greetingMessage = None
        self.layout = None
        self.dataVisualizationButton = None
        self.profilePageButton = None
        self.initializeMainView()

    def initializeMainView(self):
        self.layout = QVBoxLayout()

        self.greetingMessage = QLabel("Driving Comfortability Prediction App", self)
        self.layout.addWidget(self.greetingMessage)

        self.profilePageButton = QPushButton("Profiles Page", self)
        self.dataVisualizationButton = QPushButton("Visualize Mock Data", self)
        self.closeApplicationButton = QPushButton("Close Application", self)

        self.layout.addWidget(self.profilePageButton)
        self.layout.addWidget(self.dataVisualizationButton)
        self.layout.addWidget(self.closeApplicationButton)

        self.setLayout(self.layout)
