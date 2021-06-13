import utils
import numpy as np
import pandas as pd

def getVocabulary(documentCorpus):
    """
    Description
    ===========
        Given a corpus of documents, it returns the corresponding vocabulary.

    Parameters
    ==========
        - documentCorpus: a list of documents, where each document is a list of words.

    Results
    =======
    return: 
        - set: a set comprised of all words that occurs in corpus.
    """
    vocabulary = set()
    for document in documentCorpus:
        vocabulary = vocabulary.union(set(document))
    return vocabulary

def generateBoWVectorOfDocument(vocabulary, document):
    """
    Description
    ===========
        It receives a vocabulary and a document and then it generates the Bag-of-Words vector for 
        this document.

    Parameters
    ==========
        - vocabulary: a set containing all words that occur in corpus
        - document: a list of tokens.

    Results
    =======
    return: 
        - dict: a dictionary with words as keys and words counts as values.
    """
    countVector = dict.fromkeys(vocabulary,0)
    for word in document:
        try:
            countVector[word] += 1
        except:
            continue
    return countVector

def generateBoWMatrixOfCorpus(documentCorpus):
    """
    Description
    ===========
        Given a corpus, it generates a vector representation for each document according to Bag-of-Words
        model.

    Parameters
    ==========
        - documentCorpus: a list of documents, where each document is a list of words.

    Results
    =======
    return: 
        - dict: a dictionary with tokens as keys and lists of tokens counts as values.
    """

    vectorDicts = []

    vocabulary = set()
    for document in documentCorpus:
        vocabulary = vocabulary.union(set(document))

    for documentIndex in range(len(documentCorpus)):
        vector = generateBoWVectorOfDocument(vocabulary,documentCorpus[documentIndex])
        vectorDicts += [vector.copy()]
    
    matrix = dict.fromkeys(vocabulary)
    for key in matrix.keys():
        matrix[key] = []

    for vectorIndex,vector in enumerate(vectorDicts):
        for token in vector.keys():
            matrix[token] += []
            matrix[token] += [vector.copy()[token]]    

    return matrix

def generateTFIDFVectorOfDocument(document, idfs):
    """
    Description
    ===========
        Given a document and a dictionary of Inverse Document Frequencies of the corpus, it generates
        a vector of the document according to TF-IDF model.

    Parameters
    ==========
        - document: a list of tokens.
        - idfs: a dictionary with words as keys and idfs of these words as values.

    Results
    =======
    return: 
        - dict: a dictionary with tokens as keys and tf-idf of these words as values.
    """
    vectorDict = idfs.copy()
    documentTermFrequencies = utils.computeTF(document)

    for word in vectorDict.keys():
        try:
            vectorDict[word] = vectorDict[word] * documentTermFrequencies[word]
        except:
            vectorDict[word] = 0.0

    return vectorDict

def generateTFIDFMatrixOfCorpus(documentCorpus):
    """
    Description
    ===========
        Given a corpus, it generates a vector representation for each document in corpus according to
        TF-IDF model.

    Parameters
    ==========
        - documentCorpus: a list of documents, where each document is a list of words.

    Results
    =======
    return: 
        - dict: a dictionary with tokens as keys and lists of tf-idfs of these words as values.
    """
    idfs = utils.computeIDF(documentCorpus)
    vectorDicts = []
    for documentIndex in range(len(documentCorpus)):  
        vector = generateTFIDFVectorOfDocument(documentCorpus[documentIndex],idfs)
        vectorDicts += [vector.copy()]

    matrix = dict.fromkeys(idfs.keys())
    for key in matrix.keys():
        matrix[key] = []
        
    for vectorIndex,vector in enumerate(vectorDicts):
        for token in vector.keys():
            matrix[token] += []
            matrix[token] += [vector.copy()[token]]

    return matrix

def getDataFrameFromFeatureMatrix(matrix):
    """
    Description
    ===========
        It receives a corpus feature matrix and returns a pandas DataFrame.

    Parameters
    ==========
        - matrix: a dictionary with tokens as keys and lists of attributes as values.

    Results
    =======
    return: 
        - pandas DataFrame: a DataFrame with documents' attributes vectors as rows and features as columns.
    """
    columns = np.array(list(matrix.keys()))
    npMatrix = np.array(list(matrix.values()))
    
    orderIndexes = columns.argsort()

    columnsOrdered = columns[orderIndexes] 
    npMatrixOrdered = npMatrix[orderIndexes]
    
    return pd.DataFrame(data = npMatrixOrdered.transpose(), columns = columnsOrdered)