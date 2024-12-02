from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class ComfortZonesView(QWidget):
    def __init__(self):
        super().__init__()
        self.customColorMap = None
        self.colorLabels = None
        self.backToVisualizationChoicePageButton = None
        self.layout = None
        self.figure = None
        self.canvas = None
        self.initializeComfortZonesView()
        self.colorMap = None

    def initializeComfortZonesView(self):
        self.colorMap = {
            'Excellent': '#013901',
            'Acceptable': '#488949',
            'So and So': '#c6c854',
            'Uncomfortable': '#c5635f'
        }

        self.colorLabels = ['Acceptable', 'Excellent', 'So and So', 'Uncomfortable']
        self.customColorMap = ListedColormap([self.colorMap[label] for label in self.colorLabels])
        self.layout = QVBoxLayout()
        self.backToVisualizationChoicePageButton = QPushButton("< Back To Visualization Page", self)
        self.layout.addWidget(self.backToVisualizationChoicePageButton)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def updatePlot(self, dataframe):
        lateralMin = dataframe['Lateral acceleration'].min()
        lateralMax = dataframe['Lateral acceleration'].max()
        longitudinalMin = dataframe['Longitudinal acceleration'].min()
        longitudinalMax = dataframe['Longitudinal acceleration'].max()
        self.figure.clear()
        axis = self.figure.add_subplot(111)
        axis.set_xlim(lateralMin, lateralMax)
        axis.set_ylim(longitudinalMin, longitudinalMax)
        axis.scatter(dataframe['Lateral acceleration'], dataframe['Longitudinal acceleration'], c=dataframe['Prediction'], cmap=self.customColorMap)
        axis.grid(True)
        axis.set_xlabel('Lateral acceleration')
        axis.set_ylabel('Longitudinal acceleration')
        axis.set_title('Personalized Comfort Zones')
        self.canvas.draw()
