from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from Python.PassagerComfortabilityVisualization.Controller.ProfilesPageController import ProfilesPageController
from Python.PassagerComfortabilityVisualization.View.ProfileConfigurationView import ProfileConfigurationView
from Python.PassagerComfortabilityVisualization.View.ProfilesView import ProfilesView
from Python.PassagerComfortabilityVisualization.View.MainView import MainView


class WelcomePageController(QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.profilesController = ProfilesPageController(self)

        self.welcomePageView = MainView()
        self.profileConfigurationView = ProfileConfigurationView()

        self.stackedWidget.addWidget(self.welcomePageView)
        self.stackedWidget.addWidget(self.profilesController.profilePageView)
        self.stackedWidget.addWidget(self.profileConfigurationView)

        self.welcomePageView.profilePageButton.clicked.connect(self.showProfilesPage)
        self.profilesController.profilePageView.backToWelcomePage.clicked.connect(self.showWelcomePage)
        self.profilesController.profilePageView.updateButton.clicked.connect(self.showProfileConfigurationPage)
        self.profileConfigurationView.backToProfilesPage.clicked.connect(self.showProfilesPage)
        self.welcomePageView.closeApplicationButton.clicked.connect(self.closeApplication)

    def showWelcomePage(self):
        self.stackedWidget.setCurrentWidget(self.welcomePageView)

    def showProfilesPage(self):
        self.stackedWidget.setCurrentWidget(self.profilesController.profilePageView)

    def showProfileConfigurationPage(self):
        self.stackedWidget.setCurrentWidget(self.profileConfigurationView)

    def closeApplication(self):
        self.profilesController.profileModel.saveProfiles()
        QApplication.quit()
