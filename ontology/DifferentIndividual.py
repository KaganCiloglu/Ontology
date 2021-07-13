from owlready2 import *
onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()

def DifferentInd(domainInstance, rangeInstance):
    AllDifferent([domainInstance, rangeInstance])
