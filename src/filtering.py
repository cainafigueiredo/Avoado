from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def averageMultipleCorpusSimilarities(listOfQueries, listOfCorpus, weights):
    partialSimilarities = []

    weights = np.array(weights)/np.array(weights).sum()

    for i, corpus in enumerate(listOfCorpus):
        query = listOfQueries[i].values
        similarity = cosine_similarity(query,corpus.values)[0]
        partialSimilarities += [similarity]

    finalSimilarity = partialSimilarities[0]*weights[0]
    for similarityIndex in range(1,len(partialSimilarities)):
        finalSimilarity += partialSimilarities[similarityIndex]*weights[i]

    return {"finalSimilarities":finalSimilarity,"partialSimilarities":partialSimilarities}

def indexRankingBySimilarity(similarities):
    similarities = np.array(similarities)
    return similarities.argsort()[::-1]

def getTopNMostSimilarEntrepreneurs(top_n, listOfQueries, listOfCorpus, weights):
    similarities = averageMultipleCorpusSimilarities(listOfQueries, listOfCorpus, weights)
    
    entrepreneursIndexes = indexRankingBySimilarity(similarities['finalSimilarities'])[:top_n]
    
    similarities['finalSimilarities'] = similarities['finalSimilarities'][entrepreneursIndexes][:top_n]
    for i in range(len(similarities['partialSimilarities'])):
        similarities['partialSimilarities'][i] = similarities['partialSimilarities'][i][entrepreneursIndexes][:top_n]

    return {"entrepreneursIndexes":entrepreneursIndexes,"similarities":similarities}