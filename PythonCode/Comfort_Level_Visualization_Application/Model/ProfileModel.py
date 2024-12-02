import json
import os
import pickle
from Python.PassagerComfortabilityVisualization.Model.Profile import Profile
from keras.src.models.model import model_from_json


class ProfileModel:
    def __init__(self):
        self.modelHistory = None
        self.profiles = None
        self.filePath = 'Data/Profiles/profiles.json'
        self.loadProfiles()
        self.selectedProfile = None
        self.selectedModel = None

    def loadProfiles(self):
        json_data = None
        if os.path.exists(self.filePath):
            print('File exists')
            with open(self.filePath, 'r') as file:
                try:
                    json_data = json.load(file)
                except json.JSONDecodeError:
                    print("Error decoding JSON from the file")

        if json_data is None:
            self.profiles = self.getDefaultProfiles()
        else:
            self.profiles = []
            for singleProfile in json_data:
                profile = Profile(
                    singleProfile['name'],
                    singleProfile['modelFilePath'],
                    singleProfile['lastUpdatedModel']
                )
                self.profiles.append(profile)
        return self.profiles

    def saveProfiles(self):
        profiles_to_save = [
            {
                "name": profile.getName(),
                "modelFilePath": profile.getModelFilePath(),
                "lastUpdatedModel": profile.getLastUpdatedModel()
            }
            for profile in self.profiles
        ]
        with open(self.filePath, 'w') as file:
            json.dump(profiles_to_save, file)

    def getProfiles(self):
        return self.profiles

    def getSelectedProfile(self):
        return self.selectedProfile

    def getSelectedModel(self):
        return self.selectedModel

    def getDefaultProfiles(self):
        return [Profile("Default Profile", "../AIModels/BaselineModel", "2024-05-18")]

    def setSelectedProfile(self, profileName):
        for profile in self.profiles:
            if profile.getName() == profileName:
                self.selectedProfile = profile
                self.loadModel(profile)
                return
        print("Profile not found")
        self.selectedProfile = None

    def loadModel(self, profile):
        try:
            if os.path.exists(profile.getModelFilePath()):
                with open(profile.getModelFilePath() + 'DrivingComfortabilityPredictingModel.json',
                          'r') as json_file:
                    model_json = json_file.read()
                    self.selectedModel = model_from_json(model_json)
                self.selectedModel.load_weights(
                    profile.getModelFilePath() + 'DrivingComfortabilityPredictingModel.weights.h5')
                self.selectedModel.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                                           metrics=['accuracy'])
                with open(profile.getModelFilePath() + 'DrivingComfortabilityPredictingModelHistory.pkl', 'rb') as history_file:
                    self.modelHistory = pickle.load(history_file)
            else:
                print("Profile Path does not exist")
        except Exception as e:
            print("Please try again. Error at loading model")
            print(e)
