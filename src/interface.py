import os
numberShellLineChar = int(os.popen("stty size", 'r').read().split()[1])

def displayMenu(options, clear = False):

    if clear:
        clearShell()

    text = "O que você deseja fazer?\n\t"
    options = ["%d - %s"%(i+1,option) for i,option in enumerate(options)]
    text += "\n\t".join(options)

    print(text)

    selectedOption = int(input("\nDigite o número da opção desejada: "))
    return selectedOption

def queryMenuOption():
    printSectionSeparator("*")
    listOfQueries = getUserMeans("./utils/meansQuestions.txt","Comece nos falando um pouco sobre você.\n")
    printSectionSeparator("*")
    weights = getMeansWeights(len(listOfQueries),"\nMuito bem! De 0 a 10, quão relevante é encontrar pessoas com respostas similares para:\n")
    
    return (listOfQueries, weights)

def clearShell():
    os.system('clear')

def printSectionSeparator(char):
    print("\n"+char*numberShellLineChar+"\n")

def printWelcome(welcomePath):
    with open(welcomePath, 'r') as f:
        print(f.read())
    input("\nPressione qualquer tecla para continuar...")

def getUserMeans(questionsPath, text):
    
    print(text)

    means = []

    questions = []
    with open(questionsPath,'r') as f:
        questions = f.read().split('\n')
    
    for question in questions:
        means += [input("{}\n\t- ".format(question))]
        print("\n")

    return means

def getMeansWeights(numberOfWeights,text):
    print(text)

    weights = []

    for i in range(numberOfWeights):
        weights += [int(input("\t- Pergunta %d: "%(i+1)))]
        

    return weights