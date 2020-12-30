from CSVReader import CSVReader
import operator
import random
import pandas as pd
from TeamSorterUI import TeamSorterUI


class TeamSorter:

    numberOfTeams = 0
    sortedDictionary = {}
    finalTeamsDictionary = {}
    malePlayersArraySortedBySkills = []
    femalePlayersArraySortedBySkills = []




    def fixTeams(optionToSort, numberOfTeams, isRandom):

        TeamSorter.numberOfTeams = numberOfTeams

        def writeToCSV(numOfTeams):

            # header list
            headerList = [key.name for key in CSVReader.DataColumnsFromCSV]
            appendedColumnForTeamName = ["TeamName"]
            headerList = appendedColumnForTeamName + headerList
            headerList = dataCustomizer(headerList)

            dataListToCSV = []
            for team in TeamSorter.finalTeamsDictionary:

                for names in TeamSorter.finalTeamsDictionary[team]:

                    playerInformation = [team] + CSVReader.getDictionaryAllPlayerInformation()[names]

                    dataListToCSV.append(dataCustomizer(playerInformation))

                dataListToCSV.append([])


            preprocessedDataToWrite = pd.DataFrame(dataListToCSV, columns=headerList)

            preprocessedDataToWrite.to_csv('generatedTeams.csv', index= False)
            preprocessedDataToWrite.to_csv('generatedTeamsBACKUP.csv', index= False)

        # This function filters contents that are important from the player information
        def dataCustomizer(playerInformation):
            # Index 0: teamName
            # Index 1: playerName
            # Index 2: ic
            # Index 3: age
            # Index 4: gender
            # Index 5: contactNumber
            # Index 6: emergencyContact
            # Index 7: email
            # Index 8: experience
            # Index 9:
            # Index 10:

            playerInformation = playerInformation[0:7] # [inclusive: exclusive]
            return playerInformation


        # Sort players by gender
        TeamSorter.__sortPlayersByGender(optionToSort, isRandom)

        # Create empty teams
        for team in range(TeamSorter.numberOfTeams):
            TeamSorter.finalTeamsDictionary[('Team '+ str(team+1))] = []




        teamNumber = 1
        # Assign boys
        for male in TeamSorter.malePlayersArraySortedBySkills:
            if teamNumber == TeamSorter.numberOfTeams + 1:
                teamNumber = 1
            TeamSorter.finalTeamsDictionary['Team '+ str(teamNumber)].append(male)
            teamNumber = teamNumber + 1


        # Assign girls
        for female in TeamSorter.femalePlayersArraySortedBySkills:
            if teamNumber == TeamSorter.numberOfTeams + 1:
                teamNumber = 1
            TeamSorter.finalTeamsDictionary['Team '+ str(teamNumber)].append(female)
            teamNumber = teamNumber + 1

        writeToCSV(numberOfTeams)








    def __sortPlayersByGender(optionToSort, isRandom):

        unsortedGenderDictionaryWithSortedSkills = TeamSorter.__getDictionaryOfPlayersSortBySkill(optionToSort, isRandom)

        informationDictionary = CSVReader.getDictionaryAllPlayerInformation()

        for player in unsortedGenderDictionaryWithSortedSkills:

            # Assigns males
            if informationDictionary[player][CSVReader.DataColumnsFromCSV.gender.value - 1].lower() == 'male':
                TeamSorter.malePlayersArraySortedBySkills.append(player)
            # Assigns females
            else:
                TeamSorter.femalePlayersArraySortedBySkills.append(player)



    def __getDictionaryOfPlayersSortBySkill(optionToSort, isRandom):

        try:
            if optionToSort == 'experience':
                dictionaryBeforeSorting = CSVReader.getDictionaryAllPlayerSkillLevel('experience', isRandom)

                # Sort the players into decending skill levels
                sortedDictionary = dict(sorted(dictionaryBeforeSorting.items(), key= operator.itemgetter(1), reverse=True))
                return sortedDictionary

            if optionToSort == 'throwing skills':
                print('undefined')

            if optionToSort == 'speed skills':
                print('undefined')

            if optionToSort == 'experience and throwing skills':
                dictionaryBeforeSorting = CSVReader.getDictionaryAllPlayerSkillLevel('experience and throwing skills', isRandom)

                # Sort the players into decending skill levels
                sortedDictionary = dict(sorted(dictionaryBeforeSorting.items(), key= operator.itemgetter(1), reverse=True))
                return sortedDictionary

            if optionToSort == 'experience and speed skills':
                print('undefined')

            if optionToSort == 'experience, throwing skills, and speed skills':
                print('undefined')

        except Exception as e:
            print("Invalid option to sort/ Option to sort is not defined/ Error in reading saved dictionary")
            print(e.__class__, ' occured')






random.seed(42)
TeamSorter.fixTeams(optionToSort= 'experience', numberOfTeams=5, isRandom= True)
#print(CSVReader.dictionaryPlayerSkillLevel)
#print(TeamSorter.finalTeamsDictionary)
#print(tuple(TeamSorter.finalTeamsDictionary.keys()))











