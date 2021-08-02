from owlready2 import *
import types
import os
import pyodbc
import CreateClass
import CreateInstance
import CreateObject
import CreateRelation
import DefaultOnto
import DefiningProperty
import DisjointClasses
import SentenceAnalyzer
import turkish_wordnet_parser

onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()
objectList, objectLabelList = DefaultOnto.defaultOnt()
segmentationList, wordList = SentenceAnalyzer.analyzeQuestion()
instanceLabelList = []
focusList = ["otogar"]
wordNetList = []
print(wordList)
print(segmentationList)
print(objectList)
print(objectLabelList)

def getOnto():

    """Appending new layers to the ontology via Noun Phrases"""
    if segmentationList != []:
        className_str = segmentationList[0].capitalize()
        index = objectLabelList.index("demo." + segmentationList[2].capitalize())
        iri_str = "*" + segmentationList[2].capitalize()
        check_list = onto.search(iri=iri_str)
        if check_list != []:
            className = className_str
            superclass = objectList[index]
            className_str = CreateClass.CreateC(className, superclass)
            objectList.append(className_str)
            objectLabelList.append(str(className_str))
        else:
            print("couldnt do it(1)")
    else:
        pass

    print(objectList)
    print(objectLabelList)

    """Appending new layers to the ontology via WordNet"""
    if focusList != []:
        for i in range(len(focusList)):
            iri_str = "*" + focusList[i].capitalize()
            check_list = onto.search(iri=iri_str)
            if check_list == []:
                value = focusList[i]
                turkish_wordnet_parser.xmlkelime_parser(value)
                wordNetList = turkish_wordnet_parser.wordNet()
                print(wordNetList)
                if "TYPE - HYPERNYM" in wordNetList:
                    index = wordNetList.index('TYPE - HYPERNYM')
                    domainTopic_str = wordNetList[index-1]
                    iri_str = "*" + domainTopic_str.capitalize()
                    check_list = onto.search(iri=iri_str)
                    if check_list != []:
                        className_str = focusList[i].capitalize()
                        index = objectLabelList.index("demo." + domainTopic_str.capitalize())
                        className = className_str
                        superclass = objectList[index]
                        className_str = CreateClass.CreateC(className, superclass)
                        objectList.append(className_str)
                        objectLabelList.append(str(className_str))

    """Creating instances and properties for durakClass"""
    for word in wordList:
        if "durağ" in word:
            index = wordList.index(word)
            instanceName = wordList[index - 1]
            if segmentationList != []:
                if instanceName in segmentationList[0]:
                    iri_str = "*" + instanceName + "durağı"
                    check_list = onto.search(iri=iri_str)
                    if check_list == []:
                        instanceName = segmentationList[0] + "durağı"
                        inWhichClass = objectList[0]
                        instanceName = CreateInstance.CreateI(instanceName, inWhichClass)
                        instanceLabelList.append(instanceName)
                    else:
                        print("couldnt do it(9)")
                else:
                    print("couldnt do it(10)")
            else:
                instanceName = wordList[index - 1]
                iri_str = "*" + instanceName + "durağı"
                check_list = onto.search(iri=iri_str)
                if check_list == []:
                    instanceName = instanceName + "durağı"
                    inWhichClass = objectList[0]
                    instanceName = CreateInstance.CreateI(instanceName, inWhichClass)
                    instanceLabelList.append(instanceName)
                else:
                    print("couldnt do it(8)")
        else:
            pass

    """Creating instances and properties for otobusClass"""
    check_list = ["numara", "no", "numaralı", "nolu", "no'lu", "numaranın", "no.'lu", "numarada"]
    check = any(item in check_list for item in wordList)
    print(check)
    if check == True:
        check_list2 = []
        i=100
        for i in range(999):
            check_list2.append(str(i))
        check2 = any(item in check_list2 for item in wordList)
        print(check2)
        if check2 == True:
            check_list_as_set = set(check_list)
            intersection = check_list_as_set.intersection(wordList)
            intersection_as_list = list(intersection)
            index = wordList.index(intersection_as_list[0])
            instanceName = wordList[index-1]
            iri_str = "*" + instanceName + "numara"
            check_list = onto.search(iri=iri_str)
            if check_list == []:
                instanceName = instanceName + "numara"
                inWhichClass = objectList[1]
                instanceName = CreateInstance.CreateI(instanceName, inWhichClass)
                instanceLabelList.append(instanceName)
            else:
                print("couldnt do it(2)")
        else:
            pass
    else:
        check_list = ["sarıcivciv", "halk otobüsü", "otobüs", "minibüs", "dolmuş", "belediye otobüsü", "birlik"]
        check = any(item in check_list for item in wordList)
        print(check)
        if check == True:
            check_list2 = []
            i = 100
            for i in range(999):
                check_list2.append(str(i))
            check2 = any(item in check_list2 for item in wordList)
            print(check2)
            if check2 == True:
                check_list_as_set = set(check_list2)
                intersection = check_list_as_set.intersection(wordList)
                intersection_as_list = list(intersection)
                instanceName = intersection_as_list[0]
                iri_str = "*" + instanceName + "numara"
                check_list = onto.search(iri=iri_str)
                if check_list == []:
                    instanceName = instanceName + "numara"
                    inWhichClass = objectList[1]
                    instanceName = CreateInstance.CreateI(instanceName, inWhichClass)
                else:
                    print("couldnt do it(3)")
            else:
                check_list_as_set = set(check_list)
                intersection = check_list_as_set.intersection(wordList)
                intersection_as_list = list(intersection)
                if intersection_as_list[0] != "otobüs":
                    className_str = intersection_as_list[0]
                    iri_str = "*" + intersection_as_list[0].capitalize()
                    print(iri_str)
                    check_list = onto.search(iri=iri_str)
                    if check_list == []:
                        className = className_str
                        superclass = objectList[1]
                        className_str = CreateClass.CreateC(className, superclass)
                        objectList.append(className_str)
                        objectLabelList.append(str(className_str))

                        domainClass = className_str
                        rangeClass = objectList[1]
                        DefiningProperty.DefiningSynonym(domainClass, rangeClass)
                    else:
                        print("couldnt do it(4)")
                else:
                    print("couldnt do it(5)")
        else:
            check_list = []
            i = 100
            for i in range(999):
                check_list.append(str(i))
            check = any(item in check_list for item in wordList)
            print(check)
            if check == True:
                check_list_as_set = set(check_list)
                intersection = check_list_as_set.intersection(wordList)
                intersection_as_list = list(intersection)
                instanceName = intersection_as_list[0]
                iri_str = "*" + instanceName + "numara"
                check_list = onto.search(iri=iri_str)
                if check_list == []:
                    instanceName = instanceName + "numara"
                    inWhichClass = objectList[1]
                    instanceName = CreateInstance.CreateI(instanceName, inWhichClass)
                else:
                    print("couldnt do it(6)")
            else:
                print("couldnt do it(7)")

    print("\nclasses:")
    print(list(onto.classes()))
    print("\ninstances:")
    print(list(onto.individuals()))
    print("\nallDisjointness:")
    print(list(onto.disjoint_classes()))
    check_str = onto.search(iri="*Durak")
    print(check_str)

    """onto.save(file="C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl", format="rdfxml")"""

def main():

    getOnto()

if __name__ == '__main__':
    main()