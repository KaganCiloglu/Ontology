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

onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()
objectList, objectLabelList = DefaultOnto.defaultOnt()
segmentationList, wordList = SentenceAnalyzer.analyzeQuestion()
instanceLabelList = []
print(wordList)

print(objectList)
print(objectLabelList)

def getOnto():


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
        print("couldnt do it")

    print(objectList)
    print(objectLabelList)

    """Creating instance for otobusClass"""
    check_list = ["numara", "no", "numaralı", "nolu", "no'lu", "numaranın", "no.'lu", "numarada"]
    check = any(item in check_list for item in wordList)
    print(check)
    if check == True:
        check_list2 = ['605', '606', '607', '608']
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
                print("couldnt do it")
        else:
            pass
    else:
        check_list = ["sarıcivciv", "halkotobüsü", "otobüs", "minibüs", "dolmuş", "belediye otobüsü", "birlik"]
        check = any(item in check_list for item in wordList)
        print(check)
        if check == True:
            check_list2 = ['605', '606', '607', '608']
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
                    print("couldnt do it")
            else:
                pass
        else:
            check_list = ['605', '606', '607', '608']
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
                    print("couldnt do it")
            else:
                print("couldnt do it")


    """instanceName = "no605"
    inWhichClass = otobusClass
    no605 = CreateInstance.CreateI(instanceName, inWhichClass)

    domainInstance = tamUcreti
    rangeInstance = ucret
    CreateRelation.CreateR(domainInstance, rangeInstance)"""

    """className = "ZaferMeydaniDuragi"
    superclass = ZaferMeydani
    zaferMeydaniDuragi = CreateClass.CreateC(className, superclass)

    domainClass = seferClass
    rangeClass = guzergahClass
    DefiningProperty.DefiningHasA(domainClass, rangeClass)

    domainClass = guzergahClass
    rangeClass = ucretClass
    DefiningProperty.DefiningHasA(domainClass, rangeClass)

    domainClass = durakClass
    rangeClass = guzergahClass
    DefiningProperty.DefiningPartOf(domainClass, rangeClass)

    domainClass = seferClass
    rangeClass = guzergahClass
    DisjointClasses.DisjointC(domainClass, rangeClass)"""

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