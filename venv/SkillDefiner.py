import numpy
import pandas as pd
from csv import reader
import enum
from multipledispatch import dispatch
from TeamSorterUI import TeamSorterUI


# ----------------------------------------------------------------------------------------------------------------------------------
# SKILL DEFINER
# This class assigns each string of skill description to a weight/ skill level

class SkillDefiner:
    # Skill 1 - Experience:
    experienceLevel1 = TeamSorterUI.experienceLevel1
    experienceLevel2 = TeamSorterUI.experienceLevel2
    experienceLevel3 = TeamSorterUI.experienceLevel3
    experienceLevel4 = TeamSorterUI.experienceLevel4
    experienceLevel5 = TeamSorterUI.experienceLevel5
    
    # Skill 2 - Throws
    throwingLevel1 = TeamSorterUI.throwingLevel1
    throwingLevel2  = TeamSorterUI.throwingLevel2
    throwingLevel3  = TeamSorterUI.throwingLevel3
    throwingLevel4  = TeamSorterUI.throwingLevel4
    throwingLevel5  = TeamSorterUI.throwingLevel5
    
    # Skill 3 - Speed
    speedLevel1 = TeamSorterUI.speedLevel1
    speedLevel2 = TeamSorterUI.speedLevel1
    speedLevel3 = TeamSorterUI.speedLevel1
    speedLevel4 = TeamSorterUI.speedLevel1
    speedLevel5 = TeamSorterUI.speedLevel1


    # Functions

    # Getter methods
    def getDictionaryExperienceWeight():
        # Load experience experience
        allExperienceDescriptionArray = [
            SkillDefiner.experienceLevel1,
            SkillDefiner.experienceLevel2,
            SkillDefiner.experienceLevel3,
            SkillDefiner.experienceLevel4,
            SkillDefiner.experienceLevel5
        ]
    
        dictionaryExperienceWeight = {}
    
        count = 1
        for item in allExperienceDescriptionArray:
            dictionaryExperienceWeight[item] = count
            count = count + 1
    
        return dictionaryExperienceWeight
    
    
    def getDictionaryThrowingWeight():
        # Load throwing experience
        allThrowingDescriptionByLevel = [
            SkillDefiner.throwingLevel1,
            SkillDefiner.throwingLevel2,
            SkillDefiner.throwingLevel3,
            SkillDefiner.throwingLevel4,
            SkillDefiner.throwingLevel5,
        ]
    
        dictionaryThrowingWeight = {}
    
        count = 1
        for item in allThrowingDescriptionByLevel:
            dictionaryThrowingWeight[item] = count
            count = count + 1
    
        return dictionaryThrowingWeight
    
    
    def getDictionarySpeedWeight():
        # Load speed experience
        allSpeedDescriptionByLevel = [
            SkillDefiner.speedLevel1,
            SkillDefiner.speedLevel2,
            SkillDefiner.speedLevel3,
            SkillDefiner.speedLevel4,
            SkillDefiner.speedLevel5
        ]
    
        dictionarySpeedWeight = {}
    
        count = 1
        for item in allSpeedDescriptionByLevel:
            dictionarySpeedWeight[item] = count
            count = count + 1
    
        return dictionarySpeedWeight
    
    
    # Methods that helps with calculation

    # Public method that takes skill description from the form to be translated into a skill weight
    # Judge: Experience
    @dispatch(str)
    def playerSkillWeight(playerExperienceDescription):

        weight = SkillDefiner.getDictionaryExperienceWeight()[playerExperienceDescription]


        return int(weight)


    # Public method that takes skill description from the form to be translated into a skill weight
    # Judge: Experience, Throwing skills
    @dispatch(str, str)
    def playerSkillWeight(playerExperienceDescription, playerThrowingSkillDescription):
        weight = (SkillDefiner.getDictionaryExperienceWeight()[playerExperienceDescription] + SkillDefiner.getDictionaryThrowingWeight()[playerThrowingSkillDescription])/2
        return int(weight)

    # Public method that takes skill description from the form to be translated into a skill weight
    # Judge: Experience, Throwing Skills, Speed
    @dispatch(str, str, str)
    def playerSkillWeight(playerExperienceDescription, playerThrowingSkillDescription, playerSpeedDescription):
        weight = (SkillDefiner.getDictionaryExperienceWeight()[playerExperienceDescription] + SkillDefiner.getDictionaryThrowingWeight()[playerThrowingSkillDescription] + SkillDefiner.getDictionarySpeedWeight()[playerSpeedDescription])/3
        return weight

