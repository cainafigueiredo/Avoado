import preProcessing
import featureExtraction

def prepareQueryWithBoW(query,vocabulary):
    """
    Description
    ===========

    Parameters
    ==========

    Results
    =======
        - return:
    """
    document = preProcessing.executeFullPipeline(query)
    bowVector = featureExtraction.generateBoWVectorOfDocument(vocabulary,document)
    
    for word in bowVector.keys():
        bowVector[word] = [bowVector[word]]

    return featureExtraction.getDataFrameFromFeatureMatrix(bowVector)

def prepareQueryWithTFIDF(query,idfs):
    """
    Description
    ===========

    Parameters
    ==========

    Results
    =======
        - return:
    """
    document = preProcessing.executeFullPipeline(query)
    tfidfVector = featureExtraction.generateTFIDFVectorOfDocument(document,idfs)
    
    for word in tfidfVector.keys():
        tfidfVector[word] = [tfidfVector[word]]

    return featureExtraction.getDataFrameFromFeatureMatrix(tfidfVector)