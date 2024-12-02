from PyQt6.QtWidgets import QMainWindow


class ProfilesPageController(QMainWindow):
    def __init__(self,profileModel, profilesView, parent=None):
        super().__init__(parent)

        self.profileModel = profileModel
        self.profilePageView = profilesView
        self.profilePageView.selectButton.clicked.connect(self.selectProfile)
        self.getProfiles()

    def selectProfile(self):
        selectedItems = self.profilePageView.profileList.selectedItems()
        if selectedItems:
            currentSelectedProfileName = selectedItems[0].text()
            self.profileModel.setSelectedProfile(currentSelectedProfileName)
            self.profilePageView.currentProfileInformation.setText(f'Current Selected Profile: {self.profileModel.selectedProfile.getName()}')
            self.profilePageView.updateButton.setEnabled(True)

    def deleteProfile(self):
        selected_items = self.profilePageView.profileList.selectedItems()
        if selected_items:
            selected_profile = selected_items[0].text()
            self.profileModel.deleteProfile(selected_profile)
            self.profilePageView.updateButton.setEnabled(False)
            self.profilePageView.deleteProfile.setEnabled(False)
            self.getProfiles()

    def getProfiles(self):
        new_profiles = self.profileModel.getProfiles()
        self.profilePageView.profileList.clear()
        for profile in new_profiles:
            self.profilePageView.profileList.addItem(profile.getName())
