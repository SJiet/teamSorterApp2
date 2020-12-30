import numpy
import pandas as pd
from csv import reader
import enum
from multipledispatch import dispatch


# ----------------------------------------------------------------------------------------------------------------------------------
# SKILL DEFINER
# This class assigns each string of skill description to a weight/ skill level

class SkillDefiner:
    # Skill 1 - Experience:
    experienceLevel1 = "1"
    experienceLevel2 = "2"
    experienceLevel3 = "3"
    experienceLevel4 = "4"
    experienceLevel5 = "5"
    
    # Skill 2 - Throws
    throwingLevel1 = "I can barely hold a disc"
    throwingLevel2  = "I can only do short distance backhand"
    throwingLevel3  = "I\'m able to do both backhand and forehand throws"
    throwingLevel4  = "I can huck"
    throwingLevel5  = "I can huck, hammer, break. Call me a solid handler"
    
    # Skill 3 - Speed
    speedLevel1 = "I can huck, hammer, break. Call me a solid handler"
    speedLevel2 = "I can huck"
    speedLevel3 = "I\'m able to do both backhand and forehand throws"
    speedLevel4 = "I can only do short distance backhand"
    speedLevel5 = "I can barely hold a disc"


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

