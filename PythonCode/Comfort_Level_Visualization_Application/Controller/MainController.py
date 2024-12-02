from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication

from Python.PassagerComfortabilityVisualization.Controller.ProfileConfigurationPageController import \
    ProfileConfigurationPageController
from Python.PassagerComfortabilityVisualization.Controller.ProfilesPageController import ProfilesPageController
from Python.PassagerComfortabilityVisualization.Controller.VisualizationController import VisualizationController


class MainController(QMainWindow):
    def __init__(self, profileModel, profileConfigView, profilesView, mainView, visualizationChoiceView, comfortZoneView, livePredictionView):
        super().__init__()
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.profileModel = profileModel
        self.profileConfigView = profileConfigView
        self.profilesView = profilesView
        self.mainView = mainView
        self.visualizationChoiceView = visualizationChoiceView
        self.comfortZoneView = comfortZoneView
        self.livePredictionView = livePredictionView

        self.profileConfigController = ProfileConfigurationPageController(self.profileModel, self.profileConfigView, self)
        self.profilesController = ProfilesPageController(self.profileModel, self.profilesView, self)
        self.visualizationController = VisualizationController(self.profileModel, self.visualizationChoiceView, self.comfortZoneView, self.livePredictionView, self)

        self.stackedWidget.addWidget(self.mainView)
        self.stackedWidget.addWidget(self.profilesView)
        self.stackedWidget.addWidget(self.profileConfigView)
        self.stackedWidget.addWidget(self.visualizationChoiceView)
        self.stackedWidget.addWidget(self.comfortZoneView)
        self.stackedWidget.addWidget(self.livePredictionView)

        self.mainView.profilePageButton.clicked.connect(self.showProfilesPage)
        self.profilesView.backToWelcomePage.clicked.connect(self.showWelcomePage)
        self.profilesView.updateButton.clicked.connect(self.showProfileConfigurationPage)
        self.profileConfigView.backToProfilesPage.clicked.connect(self.showProfilesPage)
        self.mainView.closeApplicationButton.clicked.connect(self.closeApplication)
        self.mainView.dataVisualizationButton.clicked.connect(self.showVisualizationChoicePage)
        self.visualizationChoiceView.backToMainPageButton.clicked.connect(self.showWelcomePage)
        self.visualizationChoiceView.comfortZoneVisualizationButton02.clicked.connect(self.showComfortZoneVisualizationPage02)
        self.visualizationChoiceView.comfortZoneVisualizationButton05.clicked.connect(self.showComfortZoneVisualizationPage05)
        self.visualizationChoiceView.comfortZoneVisualizationButton10.clicked.connect(self.showComfortZoneVisualizationPage10)
        self.visualizationChoiceView.comfortZoneVisualizationButton15.clicked.connect(self.showComfortZoneVisualizationPage15)
        self.visualizationChoiceView.livePredictionVisualizationButton.clicked.connect(self.showLivePredictionPage)
        self.comfortZoneView.backToVisualizationChoicePageButton.clicked.connect(self.showVisualizationChoicePage)
        self.livePredictionView.backToVisualizationChoicePageButton.clicked.connect(self.showVisualizationChoicePage)

    def showWelcomePage(self):
        self.stackedWidget.setCurrentWidget(self.mainView)

    def showProfilesPage(self):
        self.profilesController.getProfiles()
        self.stackedWidget.setCurrentWidget(self.profilesView)

    def showProfileConfigurationPage(self):
        if self.profileModel.selectedProfile is not None:
            self.profileConfigController.setConfiguringProfile(self.profileModel.selectedProfile)
            self.stackedWidget.setCurrentWidget(self.profileConfigView)
        else:
            print("Please select a profile to configure first.")

    def showVisualizationChoicePage(self):
        if self.profileModel.selectedProfile is not None:
            self.stackedWidget.setCurrentWidget(self.visualizationChoiceView)
        else:
            print("Please select a profile to Analyze first.")

    def showComfortZoneVisualizationPage02(self):
        self.stackedWidget.setCurrentWidget(self.comfortZoneView)
        self.visualizationController.setComfortZones(0.02)

    def showComfortZoneVisualizationPage05(self):
        self.stackedWidget.setCurrentWidget(self.comfortZoneView)
        self.visualizationController.setComfortZones(0.05)

    def showComfortZoneVisualizationPage10(self):
        self.stackedWidget.setCurrentWidget(self.comfortZoneView)
        self.visualizationController.setComfortZones(0.10)

    def showComfortZoneVisualizationPage15(self):
        self.stackedWidget.setCurrentWidget(self.comfortZoneView)
        self.visualizationController.setComfortZones(0.15)

    def showLivePredictionPage(self):
        self.stackedWidget.setCurrentWidget(self.livePredictionView)

    def closeApplication(self):
        self.profilesController.profileModel.saveProfiles()
        QApplication.quit()

    def run(self):
        self.show()
