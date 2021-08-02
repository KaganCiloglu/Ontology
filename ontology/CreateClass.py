from owlready2 import *
import types
onto = get_ontology("file://C:/Users/asus/Desktop/4. Sınıf/4. Sınıf 1. Dönem/Ontoloji Mühendisliği (C2)/demo.owl").load()

def CreateC(className, superclass):

    with onto:

        className = types.new_class(className, (superclass,))

    """className(superclass)"""

    return className