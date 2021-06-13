import pandas as pd
import math

def computeTF(document):
    """
    Description
    ===========
        Given a document, it computes all terms frequencies of its words.

    Parameters
    ==========
        - document: a list of tokens.

    Results
    =======
    return: 
        - dict: a dictionary with words as keys and words' frequencies as values.
    """
    numberOfWords = len(document)
    documentSeries = pd.Series(document)
    termFrequency = dict(documentSeries.value_counts()/numberOfWords)
    
    return termFrequency

def getNumberOfDocumentsWhereTermOccurs(word, documentCorpus):
    """
    Description
    ===========
        It calculates the number of documents in corpus for which a given word occurs.

    Parameters
    ==========
        - word: a string of the word to be evaluated.
        - documentCorpus: a list of documents, where a document is a list of words.

    Results
    =======
    return: 
        - int: the number of documents in corpus for which the given word occurs.
    """
    documents = [set(tuple(document)) for document in documentCorpus]
    occurrenceCount = 0
    for document in documents:
        if word in document:
            occurrenceCount += 1
    return occurrenceCount

def computeIDF(documentCorpus):
    """
    Description
    ===========
        Given a corpus, it computes the Inverse Document Frequence (IDF) for the vocabulary.

    Parameters
    ==========
        - documentCorpus: a list of documents, where a document is a list of words.

    Results
    =======
    return: 
        - dict: a dictionary with words as keys and words' idfs as values.
    """
    vocabulary = set()
    for document in documentCorpus:
        vocabulary = vocabulary.union(set(tuple(document)))
    vocabulary = list(vocabulary)

    numberOfDocuments = len(documentCorpus)
    
    idfDict = dict.fromkeys(vocabulary,0)

    for word in vocabulary:
        termDocumentsOccurence = getNumberOfDocumentsWhereTermOccurs(word, documentCorpus) 
        idfDict[word] = math.log(numberOfDocuments / (termDocumentsOccurence + 1))
        
    return idfDict