from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout


class LivePredictionView(QWidget):
    def __init__(self):
        super().__init__()
        self.backToVisualizationChoicePageButton = None
        self.layout = None
        self.currentComfortLabel = None
        self.lateralAccelerationLabel = None
        self.lateralAccelerationInput = None
        self.longitudinalAccelerationLabel = None
        self.longitudinalAccelerationInput = None
        self.predictLiveValueButton = None
        self.initializeLivePredictionView()

    def initializeLivePredictionView(self):
        self.layout = QVBoxLayout()

        self.backToVisualizationChoicePageButton = QPushButton("< Back To Visualization Page", self)
        self.layout.addWidget(self.backToVisualizationChoicePageButton)

        self.currentComfortLabel = QLabel("Current Comfort Level: None", self)
        self.layout.addWidget(self.currentComfortLabel)

        lateralLayout = QHBoxLayout()
        self.lateralAccelerationLabel = QLabel("Lateral Acceleration Sensor:", self)
        self.lateralAccelerationInput = QLineEdit(self)
        lateralLayout.addWidget(self.lateralAccelerationLabel)
        lateralLayout.addWidget(self.lateralAccelerationInput)
        self.layout.addLayout(lateralLayout)

        longitudinalLayout = QHBoxLayout()
        self.longitudinalAccelerationLabel = QLabel("Longitudinal Acceleration Sensor:", self)
        self.longitudinalAccelerationInput = QLineEdit(self)
        longitudinalLayout.addWidget(self.longitudinalAccelerationLabel)
        longitudinalLayout.addWidget(self.longitudinalAccelerationInput)
        self.layout.addLayout(longitudinalLayout)

        label_width = max(self.lateralAccelerationLabel.sizeHint().width(),
                          self.longitudinalAccelerationLabel.sizeHint().width())
        self.lateralAccelerationLabel.setMinimumWidth(label_width)
        self.longitudinalAccelerationLabel.setMinimumWidth(label_width)

        self.predictLiveValueButton = QPushButton("Predict Live Value", self)
        self.layout.addWidget(self.predictLiveValueButton)

        self.setLayout(self.layout)
