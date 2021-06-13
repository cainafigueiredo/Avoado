import os
import sys
from typing import Optional
sys.path.append("./src")

import preProcessing
import dataManipulation
import featureExtraction
import filtering
import queryProcessing
import utils
import interface
import pandas as pd
import _pickle as cPickle

class Avoado:
    def __init__(self):
        self.data = None
        
        self.meansColumns = None
        self.experienceColumn = None
        
        self.preProcessedMeans = None
        self.experience = None
        
        self.listOfCorpus = None
        self.listOfVocabularies = None

        self.meansBoWMatrix = None
        self.meansBoWDataFrame = None

        self.meansTFIDFMatrix = None
        self.meansTFIDFDataFrame = None

        self.listOfIDFs = None

        if self.hasSavedVersion():
            self.loadSavedVersion()
        
        else:
            self.updateBase()

    def hasSavedVersion(self):
        if (os.path.exists("./obj/avoado.obj")):
            return True
        return False

    def loadSavedVersion(self):
        with open("./obj/avoado.obj","rb") as f:
            tmp_dict = cPickle.load(f)
            self.__dict__.update(tmp_dict)

    def updateBase(self):
        self.data = dataManipulation.readEntrepreneursData()
        
        self.meansColumns = dataManipulation.getMeansColumns()
        self.experienceColumn = dataManipulation.getExperienceColumn()
        
        self.preProcessedMeans = self.data[self.meansColumns].applymap(lambda x: preProcessing.executeFullPipeline(x))
        self.experience = self.data[self.experienceColumn]
        
        self.listOfCorpus = [list(self.preProcessedMeans.iloc[:,j].values) for j in range(len(self.meansColumns))]
        self.listOfVocabularies = [featureExtraction.getVocabulary(documentCorpus) for documentCorpus in self.listOfCorpus]

        self.meansBoWMatrix = [featureExtraction.generateBoWMatrixOfCorpus(documentCorpus) for documentCorpus in self.listOfCorpus]
        self.meansBoWDataFrame = [featureExtraction.getDataFrameFromFeatureMatrix(matrix) for matrix in self.meansBoWMatrix]

        self.meansTFIDFMatrix = [featureExtraction.generateTFIDFMatrixOfCorpus(documentCorpus) for documentCorpus in self.listOfCorpus]
        self.meansTFIDFDataFrame = [featureExtraction.getDataFrameFromFeatureMatrix(matrix) for matrix in self.meansTFIDFMatrix]
    
        self.listOfIDFs = [utils.computeIDF(documentCorpus) for documentCorpus in self.listOfCorpus]

        with open("./obj/avoado.obj","wb") as f:
            cPickle.dump(self.__dict__,f,2)
        
        self.loadSavedVersion()

while True:

    avoado = Avoado()

    # Interface
    interface.clearShell()
    interface.printSectionSeparator("*")
    interface.printWelcome("./utils/welcome.txt")
    
    interface.printSectionSeparator("*")
    
    selectedOption = interface.displayMenu(["Consultar","Atualizar Base","Sair"])

    if selectedOption == 1:
        listOfQueries,weights = interface.queryMenuOption()
        
        listOfBoWQueries = [queryProcessing.prepareQueryWithBoW(listOfQueries[i],avoado.listOfVocabularies[i]) for i in range(len(listOfQueries))]
        listOfTFIDFQueries = [queryProcessing.prepareQueryWithTFIDF(listOfQueries[i],avoado.listOfIDFs[i]) for i in range(len(listOfQueries))]

        interface.printSectionSeparator("*")

        top_n = int(input("Selecione o número de resultados que você quer visualizar: "))

        print("\nMetodologia baseada em Bag-of-Words:")
        print("====================================\n")
        mostSimilarEntrepreneursBoW = filtering.getTopNMostSimilarEntrepreneurs(top_n,listOfBoWQueries,avoado.meansBoWDataFrame,[1,1,1])
        dataManipulation.printEntrepreneursInfo(mostSimilarEntrepreneursBoW['entrepreneursIndexes'],mostSimilarEntrepreneursBoW['similarities'])

        print("\n\nMetodologia baseada em TF-IDF:")
        print("==============================\n")
        mostSimilarEntrepreneursTFIDF = filtering.getTopNMostSimilarEntrepreneurs(top_n,listOfTFIDFQueries,avoado.meansTFIDFDataFrame,[3,1,1])
        dataManipulation.printEntrepreneursInfo(mostSimilarEntrepreneursTFIDF['entrepreneursIndexes'],mostSimilarEntrepreneursTFIDF['similarities'])

    elif selectedOption == 2:
        avoado.updateBase()
        print("Base atualizada!\n")
    
    elif selectedOption == 3:
        print("\nObrigado por utilizar nosso sistema! ")
        break

    input("Pressione qualquer tecla para continuar...")