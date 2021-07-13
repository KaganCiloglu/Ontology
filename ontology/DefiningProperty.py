from owlready2 import *
onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()

def DefiningPartOf(domainClass, rangeClass):
    with onto:

        class part_of(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningHasA(domainClass, rangeClass):
    with onto:

        class has_a(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningAtLocation(domainClass, rangeClass):
    with onto:

        class at_location(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningAtTime(domainClass, rangeClass):
    with onto:

        class at_time(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]