from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget


class ProfilesView(QWidget):
    def __init__(self):
        super().__init__()
        self.createButton = None
        self.deleteProfile = None
        self.updateButton = None
        self.selectButton = None
        self.currentProfileInformation = None
        self.backToWelcomePage = None
        self.profileList = None
        self.layout = None
        self.initializeProfilesView()

    def initializeProfilesView(self):
        self.layout = QVBoxLayout()

        self.profileList = QListWidget(self)
        self.selectButton = QPushButton("Select Profile", self)
        self.updateButton = QPushButton("See Profile Details", self)

        self.backToWelcomePage = QPushButton("< Back", self)

        if self.currentProfileInformation is None:
            self.updateButton.setEnabled(False)
            self.currentProfileInformation = QLabel("Current Selected Profile: None", self)

        self.layout.addWidget(self.backToWelcomePage)
        self.layout.addWidget(self.currentProfileInformation)
        self.layout.addWidget(self.profileList)
        self.layout.addWidget(self.selectButton)
        self.layout.addWidget(self.updateButton)

        self.setLayout(self.layout)
