import pandas as pd

entrepreneursBase = None

def readEntrepreneursData():
    """
    Description
    ===========
        It reads entrepreneurs data from ../data/entrepreneurs.csv.

    Parameters
    ==========
        There are no parameters.

    Results
    =======
    return: 
        - pandas DataFrame: entrepreurs base
    """
    global entrepreneursBase
    entrepreneursBase = pd.read_csv("./data/entrepreneurs.csv") 
    return entrepreneursBase

def getMeansColumns():
    """
    Description
    ===========
        Returns a sublist of columns names. These columns stores features of entrepreneurs' means.

    Parameters
    ==========
        There are no parameters.

    Results
    =======
    return: 
        - list: a list of columns names which represents entrepreneurs' means.
    """
    return ['hobbies','habilidades','interacaoSocial']

def getExperienceColumn():
    """
    Description
    ===========
        Returns a sublist of columns names. These columns stores features of entrepreneurs' experience.

    Parameters
    ==========
        There are no parameters.

    Results
    =======
    return: 
        - list: a list of columns names which represents entrepreneurs' experience.
    """
    return ['experiencia']

def printEntrepreneursInfo(entrepreneursIndexes, similarities):
    info = "Aqui está o resultado de sua consulta:\n\n"
    for i,entrepreneur in enumerate(entrepreneursIndexes):
        entrepreneurData = entrepreneursBase.iloc[entrepreneur,:]
        finalSimilarities = similarities['finalSimilarities']
        partialSimilarities = similarities['partialSimilarities']
        info += "Empreendedor %d (Similarity = %.3f):\n"%(i+1,finalSimilarities[i])
        info += "\t- Hobbies (Partial Similarity = %.3f): \n\t\t%s\n"%(partialSimilarities[0][i],entrepreneurData['hobbies'])
        info += "\t- Habilidades (Partial Similarity = %.3f): \n\t\t%s\n"%(partialSimilarities[1][i],entrepreneurData['habilidades'])
        info += "\t- Interação Social (Partial Similarity = %.3f): \n\t\t%s\n"%(partialSimilarities[2][i],entrepreneurData['interacaoSocial'])
        info += "\t- Experiência: \n\t\t%s\n\n"%(entrepreneurData['experiencia'])
    print(info)

def getEntrepreneurCharacteristic(rowIndex,columnName):
    """
    Description
    ===========
        Get the value of a feature for a given entrepreneur of the base.

    Parameters
    ==========
        - int: index of the entrepreneur in the base
        - string: name of the feature (column of the base) to be retrieved

    Results
    =======
    return: 
        - It returns the value of DataFrame cell which corresponds to (rowIndex, columnName).
    """
    if (entrepreneursBase == None):
        readEntrepreneursData()
    return entrepreneursBase[columnName][rowIndex]