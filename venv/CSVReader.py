import numpy
import pandas as pd
from csv import reader
import enum
from SkillDefiner import SkillDefiner
import random
import operator

# --------------------------------------------------------------------------------------------------------------------------
# CSV READER
# Represent each element of the column from the csv as numbers to be accessed by data frame

class CSVReader:

    class DataColumnsFromCSV(enum.Enum):
        # Identifies index of each data found in the csv. The variable name is a template
        playerName = 1
        ic = 2
        age = 3
        gender = 4
        contactNumber = 5
        emergencyContact = 6
        email = 7
        experience = 8
        throwingSkills = 9
        speed = 10
        shirtSize = 11
    
    
    # Creates a dictionary to store "name" (key) and "information" (value)
    dictionaryPlayerInformation = {}

    dictionaryPlayerSkillLevel = {}

    
    # Functions
    # Function to read csv


    # Private helper method
    def __readCsvFileLoadPlayerInformation():
        # Read csv
        dataset = pd.read_csv("C:/Users/Admin/Documents/Python_download_8-5/teamSorter/Melaka Christmas Ultimate Frisbee 2020 (Registration Form) (Responses) - Form responses 1 (2).csv")
        df = pd.DataFrame(dataset)
    
        # Obtain vital data from each row
        for index, row in df.iterrows():
    
            # Creates an array to store a player's info
            playerInformationArray = []
    
            # Iterate through all items of a player
            for data in CSVReader.DataColumnsFromCSV:

                # Loading player information
                playerInformationArray.append(row[data.value])


            # Store the information of the player into the dictionary
            CSVReader.dictionaryPlayerInformation[row[CSVReader.DataColumnsFromCSV.playerName.value]] = playerInformationArray

    # Private helper method
    def __readCsvFileLoadSkillInformation(optionSwitch):

        # Choose "optionSwitch" number:
        # This helps judge a player's skill level
        #
        # Option - "1": average of (Experience) weight
        # Option - "2": average of (Throwing) weight
        # Option - "3": average of (Speed) weight
        # Option - "4": average of (Experience, Throwing) weight
        # Option - "5": average of (Experience, Throwing, Speed) weight
        # Option - "5": average of (Experience) weight
        #

        # Read csv
        dataset = pd.read_csv(
            "C:/Users/Admin/Documents/Python_download_8-5/teamSorter/Melaka Christmas Ultimate Frisbee 2020 (Registration Form) (Responses) - Form responses 1 (2).csv")
        df = pd.DataFrame(dataset)

        # Obtain vital data from each row
        for index, row in df.iterrows():

            # Creates an variable to store a player's info
            playerSkillWeight = 0

            if optionSwitch == 'experience':
                # Judge skill based on:- Experience
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.experience.value]))

            if optionSwitch == 'throwing skills':
                # Judge skill based on:- Throwing Skills
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.throwingSkills.value]))

            if optionSwitch == 'speed':
                # Judge skill based on:- Speed - XX MIGHT NOT WORK YET XX Because haven't define speed description
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.speed.value]))

            if optionSwitch == 'experience and throwing skills':
                # Judge skill based on:- Experience, Throwing Skills
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.experience.value]), str(row[CSVReader.DataColumnsFromCSV.throwingSkills.value]))

            if optionSwitch == 'experience, throwing skills and speed':
                # Judge skill based on:- Experience, Throwing Skills, Speed - XX MIGHT NOT WORK YET XX Because haven't define speed description
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.experience.value]), str(row[CSVReader.DataColumnsFromCSV.throwingSkills.value]), str(row[CSVReader.DataColumnsFromCSV.speed.value]))

            if optionSwitch == 'experience':
                # Judge skill based on:- Experience
                playerSkillWeight = SkillDefiner.playerSkillWeight(str(row[CSVReader.DataColumnsFromCSV.experience.value]))


            # Store the information of the player into the dictionary
            CSVReader.dictionaryPlayerSkillLevel[row[CSVReader.DataColumnsFromCSV.playerName.value]] = playerSkillWeight

    # Public method to get all player information
    def getDictionaryAllPlayerInformation():

        CSVReader.__readCsvFileLoadPlayerInformation()
        return CSVReader.dictionaryPlayerInformation

    # Public method to get all player skill level
    def getDictionaryAllPlayerSkillLevel(option, isRandom):
        
        CSVReader.__readCsvFileLoadSkillInformation(option)

        if isRandom:
            keys = list(CSVReader.dictionaryPlayerSkillLevel.keys())
            random.shuffle(keys)
            randomizedArrayTuples = [(key, CSVReader.dictionaryPlayerSkillLevel[key]) for key in keys]
            return dict(randomizedArrayTuples)
        else:
            return CSVReader.dictionaryPlayerSkillLevel





#print(CSVReader.getDictionaryAllPlayerInformation())
#print(CSVReader.getDictionaryAllPlayerSkillLevel('experience', False))
#print(CSVReader.getDictionaryAllPlayerSkillLevel('experience and throwing skills', False))
#print(dict(sorted(CSVReader.getDictionaryAllPlayerSkillLevel('experience', False).items(), key= operator.itemgetter(1), reverse=True)))

# ----------------------------------------------------------------------------------------------------------------------