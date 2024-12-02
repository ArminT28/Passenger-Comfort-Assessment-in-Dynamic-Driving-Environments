from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class ProfileConfigurationView(QWidget):
    def __init__(self):
        super().__init__()
        self.profileNameLabel = None
        self.lastUpdatedLabel = None
        self.lastTrainedModelLabel = None
        self.configuringProfile = None
        self.backToProfilesPage = None
        self.layout = None
        self.initializeProfileConfigurationView()

    def initializeProfileConfigurationView(self):
        self.layout = QVBoxLayout()

        self.backToProfilesPage = QPushButton("< Back", self)
        self.profileNameLabel = QLabel("Profile Name:", self)
        self.lastUpdatedLabel = QLabel("Last updated at:", self)
        self.lastTrainedModelLabel = QLabel("Last trained model:", self)

        self.layout.addWidget(self.backToProfilesPage)
        self.layout.addWidget(self.profileNameLabel)
        self.layout.addWidget(self.lastUpdatedLabel)
        self.layout.addWidget(self.lastTrainedModelLabel)

        self.setLayout(self.layout)

    def setConfiguredProfile(self, profile):
        self.configuringProfile = profile
        self.profileNameLabel.setText(f"Profile Name: {profile.getName()}")
        self.lastUpdatedLabel.setText(f"Last updated at: {profile.getLastUpdatedModel()}")
        self.lastTrainedModelLabel.setText(f"Last trained model: {profile.getModelFilePath()}")
