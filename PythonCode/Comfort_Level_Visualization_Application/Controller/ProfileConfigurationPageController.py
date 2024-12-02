from PyQt6.QtWidgets import QMainWindow


class ProfileConfigurationPageController(QMainWindow):
    def __init__(self, profileModel, profileConfigurationView, parent=None):
        super().__init__(parent)
        self.profileConfigurationView = profileConfigurationView
        self.profileModel = profileModel

    def setConfiguringProfile(self, profile):
        self.profileConfigurationView.setConfiguredProfile(profile)
