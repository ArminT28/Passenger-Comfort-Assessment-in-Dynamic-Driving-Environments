from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


class VisualizationChoiceView(QWidget):
    def __init__(self):
        super().__init__()
        self.comfortZoneVisualizationButton15 = None
        self.livePredictionVisualizationLabel = None
        self.livePredictionVisualizationDescription = None
        self.comfortZoneVisualizationButton05 = None
        self.comfortZoneVisualizationButton10 = None
        self.comfortZoneVisualizationDescripiton = None
        self.comfortZoneVisualizationLabel = None
        self.layout = None
        self.livePredictionVisualizationButton = None
        self.comfortZoneVisualizationButton02 = None
        self.backToMainPageButton = None
        self.initializeVisualizationView()

    def initializeVisualizationView(self):
        self.layout = QVBoxLayout()

        self.backToMainPageButton = QPushButton("< Back To Main Page", self)
        self.comfortZoneVisualizationLabel = QLabel("Comfort Zones Visualization Choices:", self)
        self.comfortZoneVisualizationDescripiton = QLabel("Keep in mind that the larger the step, the slower the "
                                                          "waiting time of the generation.", self)
        self.comfortZoneVisualizationButton02 = QPushButton("Step 0.02 (usually around 10 seconds)", self)
        self.comfortZoneVisualizationButton05 = QPushButton("Step 0.05 (usually around 3-4 seconds)", self)
        self.comfortZoneVisualizationButton10 = QPushButton("Step 0.10 (usually around 1-2 seconds)", self)
        self.comfortZoneVisualizationButton15 = QPushButton("Step 0.15 (usually around 1 seconds)", self)
        self.livePredictionVisualizationLabel = QLabel("Live Prediction Feature:", self)
        self.livePredictionVisualizationDescription = QLabel("Here you can input custom data by hand to see the prediction", self)
        self.livePredictionVisualizationButton = QPushButton("Try out Live Predictions", self)

        self.layout.addWidget(self.backToMainPageButton)
        self.layout.addWidget(self.comfortZoneVisualizationLabel)
        self.layout.addWidget(self.comfortZoneVisualizationDescripiton)
        self.layout.addWidget(self.comfortZoneVisualizationButton02)
        self.layout.addWidget(self.comfortZoneVisualizationButton05)
        self.layout.addWidget(self.comfortZoneVisualizationButton10)
        self.layout.addWidget(self.comfortZoneVisualizationButton15)
        self.layout.addWidget(self.livePredictionVisualizationLabel)
        self.layout.addWidget(self.livePredictionVisualizationDescription)
        self.layout.addWidget(self.livePredictionVisualizationButton)

        self.setLayout(self.layout)
