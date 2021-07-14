from owlready2 import *

import CreateInstance
import CreateObject

onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()
objectlist = []
labellist = []

def defaultOnt():

    check_list = onto.search(iri="*Durak")
    if check_list == []:
        objectName = "Durak"
        durakClass = CreateObject.CreateObj(objectName)
        objectlist.append(durakClass)
        labellist.append(str(durakClass))
    else:
        print("Requirement already satisfied")

    check_list = onto.search(iri="*Otobus")
    if check_list == []:
        objectName = "Otobus"
        otobusClass = CreateObject.CreateObj(objectName)
        objectlist.append(otobusClass)
        labellist.append(str(otobusClass))
    else:
        print("Requirement already satisfied")

    check_list = onto.search(iri="*Guzergah")
    if check_list == []:
        objectName = "Guzergah"
        guzergahClass = CreateObject.CreateObj(objectName)
        objectlist.append(guzergahClass)
        labellist.append(str(guzergahClass))
    else:
        print("Requirement already satisfied")

    check_list = onto.search(iri="*Sefer")
    if check_list == []:
        objectName = "Sefer"
        seferClass = CreateObject.CreateObj(objectName)
        objectlist.append(seferClass)
        labellist.append(str(seferClass))
    else:
        print("Requirement already satisfied")

    check_list = onto.search(iri="*Ucret")
    if check_list == []:
        objectName = "Ucret"
        ucretClass = CreateObject.CreateObj(objectName)
        objectlist.append(ucretClass)
        labellist.append(str(ucretClass))
    else:
        print("Requirement already satisfied")

    check_list = onto.search(iri="*Meydan")
    if check_list == []:
        objectName = "Meydan"
        meydanClass = CreateObject.CreateObj(objectName)
        objectlist.append(meydanClass)
        labellist.append(str(meydanClass))
    else:
        print("Requirement already satisfied")

    return objectlist, labellist