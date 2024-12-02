from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class ProfileCreationView(QWidget):
    def __init__(self):
        super().__init__()
        self.createButton = None
        self.lastTrainedModelInput = None
        self.lastTrainedModelLabel = None
        self.lastUpdatedInput = None
        self.lastUpdatedLabel = None
        self.profileNameLabel = None
        self.profileNameInput = None
        self.backToProfilesButton = None
        self.layout = None
        self.initializeProfileCreationView()

    def initializeProfileCreationView(self):
        self.layout = QVBoxLayout()

        self.backToProfilesButton = QPushButton("< Back", self)

        self.profileNameLabel = QLabel("Profile Name:", self)
        self.profileNameInput = QLineEdit(self)

        self.lastUpdatedLabel = QLabel("Last updated at:", self)
        self.lastUpdatedInput = QLineEdit(self)

        self.lastTrainedModelLabel = QLabel("Last trained model:", self)
        self.lastTrainedModelInput = QLineEdit(self)

        self.createButton = QPushButton("Create", self)

        self.layout.addWidget(self.backToProfilesButton)
        self.layout.addWidget(self.profileNameLabel)
        self.layout.addWidget(self.profileNameInput)
        self.layout.addWidget(self.lastUpdatedLabel)
        self.layout.addWidget(self.lastUpdatedInput)
        self.layout.addWidget(self.lastTrainedModelLabel)
        self.layout.addWidget(self.lastTrainedModelInput)
        self.layout.addWidget(self.createButton)

        self.setLayout(self.layout)

    def createProfile(self):
        profileName = self.profileNameInput.text()
        lastUpdated = self.lastUpdatedInput.text()
        lastTrainedModel = self.lastTrainedModelInput.text()

        print(
            f"Creating profile with Name: {profileName}, Last Updated: {lastUpdated}, Last Trained Model: {lastTrainedModel}")

        return profileName
