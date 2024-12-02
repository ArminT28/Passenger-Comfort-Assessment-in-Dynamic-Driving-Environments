class Profile:
    def __init__(self, name, modelFilePath, lastUpdatedModelTimestamp):
        self.name = name
        self.modelFilePath = modelFilePath
        self.lastUpdatedModel = lastUpdatedModelTimestamp

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getModelFilePath(self):
        return self.modelFilePath

    def setModelFilePath(self, model_file_path):
        self.modelFilePath = model_file_path

    def getLastUpdatedModel(self):
        return self.lastUpdatedModel

    def setLastUpdatedModel(self, last_updated_model):
        self.lastUpdatedModel = last_updated_model

    def __str__(self):
        return f'Profile({self.name}, Model File Path: {self.modelFilePath}, Last Updated Model: {self.lastUpdatedModel})'

    def __repr__(self):
        return self.__str__()
