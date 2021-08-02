from owlready2 import *
onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()

def DefiningHypernym(domainClass, rangeClass):
    with onto:

        class hypernym(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningHyponym(domainClass, rangeClass):
    with onto:

        class hyponym(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningDomainTopic(domainClass, rangeClass):
    with onto:

        class domainTopic(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningMemberHolonym(domainClass, rangeClass):
    with onto:

        class memberHolonym(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]

def DefiningSynonym(domainClass, rangeClass):
    with onto:

        class synonym(ObjectProperty):
            domain = [domainClass]
            range = [rangeClass]