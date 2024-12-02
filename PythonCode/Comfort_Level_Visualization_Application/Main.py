import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication
from Python.PassagerComfortabilityVisualization.Controller.MainController import MainController
from Python.PassagerComfortabilityVisualization.Model.ProfileModel import ProfileModel
from Python.PassagerComfortabilityVisualization.View.ComfortZonesView import ComfortZonesView
from Python.PassagerComfortabilityVisualization.View.LivePredictionView import LivePredictionView
from Python.PassagerComfortabilityVisualization.View.ProfileConfigurationView import ProfileConfigurationView
from Python.PassagerComfortabilityVisualization.View.ProfilesView import ProfilesView
from Python.PassagerComfortabilityVisualization.View.MainView import MainView
from Python.PassagerComfortabilityVisualization.View.VisualizationChoiceView import VisualizationChoiceView


def main():
    app = QApplication(sys.argv)
    profileModel = ProfileModel()
    profileConfigView = ProfileConfigurationView()
    profilesView = ProfilesView()
    mainView = MainView()
    visualizationChoiceView = VisualizationChoiceView()
    comfortZoneView = ComfortZonesView()
    livePredictionView = LivePredictionView()

    font = QFont()
    font.setPointSize(30)
    font.setBold(True)
    app.setFont(font)

    mainController = MainController(profileModel, profileConfigView, profilesView, mainView, visualizationChoiceView, comfortZoneView, livePredictionView)
    mainController.run()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
