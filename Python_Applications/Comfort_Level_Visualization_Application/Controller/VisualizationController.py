import re
import numpy as np
import pandas as pd
from PyQt6.QtWidgets import QMainWindow


class VisualizationController(QMainWindow):
    def __init__(self, profileModel, visualizationChoiceView, comfortZoneView, livePredictionView, parent=None):
        super().__init__(parent)
        self.comfortZoneView = comfortZoneView
        self.visualizationChoiceView = visualizationChoiceView
        self.livePredictionView = livePredictionView
        self.profileModel = profileModel
        self.livePredictionView.predictLiveValueButton.clicked.connect(self.predictLiveValue)

    def predictComfortZones(self,step):
        dataframe = pd.DataFrame()
        lateral_min = -5.0
        lateral_max = 5.0
        longitudinal_min = -5.0
        longitudinal_max = 5.0
        lateral, longitudinal = np.meshgrid(np.arange(lateral_min, lateral_max, step),
                                            np.arange(longitudinal_min, longitudinal_max, step))
        try:
            predictions = self.profileModel.selectedModel.predict(np.c_[lateral.ravel(), longitudinal.ravel()], verbose=0)
        except Exception as e:
            print("VisualizationController: " + e)
            return
        label_predictions = np.argmax(predictions, axis=1)

        dataframe['Lateral acceleration'] = lateral.ravel()
        dataframe['Longitudinal acceleration'] = longitudinal.ravel()
        dataframe['Prediction'] = label_predictions

        return dataframe

    def setComfortZones(self, step):
        predictedDataframe = self.predictComfortZones(step)
        self.comfortZoneView.updatePlot(predictedDataframe)

    def predictLiveValue(self):
        print("Predicting live value")
        try:
            stringX = self.livePredictionView.lateralAccelerationInput.text()
            if stringX == '':
                stringX = '0.0'
            else:
                stringX = re.sub(r'[^0-9.]', '', stringX)
                if stringX.count('.') > 1:
                    parts = stringX.split('.')
                    stringX = parts[0] + '.' + ''.join(parts[1:])
            floatX = float(stringX)
        except Exception as e:
            print("VisualizationController: " + e)
            return

        try:
            stringY = self.livePredictionView.longitudinalAccelerationInput.text()
            if stringY == '':
                stringY = '0.0'
            else:
                stringY = re.sub(r'[^0-9.]', '', stringY)
                if stringY.count('.') > 1:
                    parts = stringY.split('.')
                    stringY = parts[0] + '.' + ''.join(parts[1:])
            floatY = float(stringY)
        except Exception as e:
            print("VisualizationController: " + e)
            return

        try:
            prediction = self.profileModel.selectedModel.predict(np.array([[floatX, floatY]]), verbose=0)
        except Exception as e:
            print("VisualizationController: " + e)
            return

        labelPrediction = np.argmax(prediction, axis=1)

        comfortLevels = {
            0: ('Acceptable', 'darkgreen'),
            1: ('Excellent', 'lightgreen'),
            2: ('So and So', 'yellow'),
            3: ('Uncomfortable', 'red')
        }

        predicted_comfort_level, color = comfortLevels.get(labelPrediction[0], ('Unknown', 'black'))

        self.livePredictionView.lateralAccelerationInput.setText(stringX)
        self.livePredictionView.longitudinalAccelerationInput.setText(stringY)
        self.livePredictionView.currentComfortLabel.setText(f'Predicted Comfort Level: {predicted_comfort_level}')
        self.livePredictionView.currentComfortLabel.setStyleSheet(f'color: {color};')

