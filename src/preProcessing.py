import re
import unicodedata
import nltk

def convertToLowerCase(text):
    """
    Description
    ===========
        It converts the string passed as input to its lower case.

    Parameters
    ==========
        - string: text to be transformed.

    Results
    =======
    return: 
        - string: the transformed string, i.e., text string in its lower case version.
    """
    return text.lower()

def removePunctuationAndSpecialChar(text):
    """
    Description
    ===========
        It removes any punctuation or special characteres of string passed as argument.

    Parameters
    ==========
        - string: text to be transformed.

    Results
    =======
    return: 
        - string: the transformed string, i.e., text string without punctuations or special characteres.
    """
    return re.sub(r"[^\w\s]","",text)

def wordTokenize(text):
    """
    Description
    ===========
        It breaks the string passed as argument in a list of tokens.

    Parameters
    ==========
        - string: text to be transformed.

    Results
    =======
    return: 
        - list: a list of tokens.
    """
    try:
        wordTokens = nltk.tokenize.word_tokenize(text)
    except: 
        nltk.download('punkt')
        wordTokens = nltk.tokenize.word_tokenize(text)
    return wordTokens

def removePortugueseStopWords(wordTokens):
    """
    Description
    ===========
        It removes portuguese stopwords form a list of tokens.

    Parameters
    ==========
        - wordTokens: a list of tokens.

    Results
    =======
    return: 
        - list: a list comprised by a subset of wordTokens, i.e., wordTokens except portuguese stop words.
    """
    try:
        stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    except:
        nltk.download('stopwords')
        stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    filteredWords = [word for word in wordTokens if not word.lower() in stopwords]
    return filteredWords

def portugueseStemming(wordTokens):
    """
    Description
    ===========
        It transforms each word of the list passed as argument to its root form.

    Parameters
    ==========
        - wordTokens: a list of tokens.

    Results
    =======
    return: 
        - list: a list of tokens where each token is stemmed.
    """
    try:
        stemmer = nltk.stem.RSLPStemmer()
    except:
        nltk.download('rslp')
        stemmer = nltk.stem.RSLPStemmer()
    return list(map(lambda word: stemmer.stem(word), wordTokens))

def removeAccentedCharacters(wordTokens): 
    """
    Description
    ===========
        It remove all accented characters for each word in a list of tokens.

    Parameters
    ==========
        - wordTokens: a list of tokens.

    Results
    =======
    return: 
        - list: a list of tokens without accented characteres.
    """
    return list(
        map (
            lambda x: unicodedata.normalize('NFKD',x).encode('ASCII','ignore').decode('utf-8'),
            wordTokens
        )
    )

def executeFullPipeline(text):
    """
    Description
    ===========
        It executes a full pipeline of text preprocessing.

    Parameters
    ==========
        - text: the string to be preprocessed.

    Results
    =======
    return: 
        - list: a list of tokens where each token is stemmed.
    """
    textTemp = convertToLowerCase(text)
    textTemp = removePunctuationAndSpecialChar(textTemp)
    textTemp = wordTokenize(textTemp)
    textTemp = removePortugueseStopWords(textTemp)
    textTemp = portugueseStemming(textTemp)
    textTemp = removeAccentedCharacters(textTemp)
    return textTemp