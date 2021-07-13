import Tokenizer
from pyswip import Prolog
prolog = Prolog()

prolog.consult("analyzer.pl")

headOfQuery1 = '('
tailOfQuery1 = ', L).'
fullQuery1 = ''

headOfQuery2 = '(X,'
tailOfQuery2 = '(X),L).'
fullQuery2 = ''

soln_str = ''

segmentationlist = []
posTaggingList = []
antiDuplicateList = []

sentence = "Adü'den kalkan 607 numarada, 17:15'te (ZaferMeydanı) Zafer Meydanı durağından geçmektedir."


def analyzeQuestion():
    global segmentationlist

    # analyze the sentence
    wordlist = Tokenizer.analyze(sentence)
    # Show word list
    """print("\nTokenized Sentence")
    print(wordList)"""
    for word in (wordlist):
        fullQuery1 = 'analyze' + headOfQuery1 + word + tailOfQuery1
        try:
            query = prolog.query(fullQuery1)
            for soln in query:
                print()
        except:
            continue
        try:
            for n in range(len(soln["L"])):
                soln_str = (soln["L"][0]).value
                antiDuplicateList.append(soln_str)
                segmentationlist = list(dict.fromkeys(antiDuplicateList))
        except:
            continue
    """print("\nsegmentationList: ")
    print(segmentationList)"""

    return segmentationlist, wordlist

"""    for word in (segmentationList):
        fullQuery2 = 'findall' + headOfQuery2 + word + tailOfQuery2
        try:
            query = prolog.query(fullQuery2)
            for soln in query:
                print()
        except:
            continue
        for j in range(len(soln["L"])):
            posTaggingList.append(word)
            soln_str = (soln["L"][j]).value
            posTaggingList.append(soln_str)
    print("\nposTagginlist: ")
    print(posTaggingList)"""

