import xml.etree.ElementTree as ET

object = ET.parse('turkish_wordnet.xml')

root = object.getroot()

wholeList = []
turList = []
turList2 = []
typeList = []
wordNetList = []
head_str = "./SYNSET/[ID='"
tail_str = "']"
"""for SYNSET in root.findall("./SYNSET/[ID='TUR10-0593960']"):
    given = SYNSET
    for child in given:
        for little in child:
            myList.append(little.text)
    print(myList[0])"""

def xmlkelime_parser(value):
    object = ET.parse(
        "turkish_wordnet.xml")
    source = object.getroot()
    while True:
        """value = str(input("Kelime giriniz:"))"""
        value = value.lower()

        for given in source:
            state = search(given,value)

        break

def search(given,text):        #search işlemi yapmak için tanımladık
    for child in given:
        if child.tag == "SYNONYM":
            for little in child:
                if little.text == text:
                    printSynset(given)
                    return 1

def printSynset(given):        #tagları ekrana yazdırmak için gereken metod
    for child in given:
        if child.tag == "SYNONYM":
            """print(child.text)"""
            wholeList.append(child.text)
            for little in child:
                """print(little.tag + " - " + little.text)"""
                wholeList.append(little.tag + " - " + little.text)
        elif child.tag == "SR":
            """print(child.text)"""
            wholeList.append(child.text)
            for little in child:
                """print(little.tag + " - " + little.text)"""
                wholeList.append(little.tag + " - " + little.text)
        else:
            """print(child.tag + " - " + child.text)"""
            wholeList.append(child.tag + " - " + child.text)
    """print("-----------END-----------------")"""

def wordNet():
    """print("\n")
    print("wholeList")
    print(wholeList)"""
    check_list = ["TUR"]
    for word in wholeList:
        for item in check_list:
            try:
                if item in word:
                    if "ID" not in word:
                        turList.append(word)
            except:
                continue
    """print("turList")
    print(turList)"""

    check_list = ["TYPE"]
    for word in wholeList:
        for item in check_list:
            try:
                if item in word:
                    typeList.append(word)
            except:
                continue
    """print("typeList")
    print(typeList)"""

    for i in range(3):
        try:
            for SYNSET in root.findall(head_str + turList[i] + tail_str):
                for child in SYNSET:
                    for little in child:
                        if little.text.islower() == True:
                            turList2.append(little.text)
        except:
            pass

    for i in range(3):
        try:
            wordNetList.append(turList2[i])
            wordNetList.append(typeList[i])
        except:
            pass
    """print(turList2)
    print(wordNetList)"""
    return wordNetList

    """tag = source.tag

    for x in source[1]:
            for y in x:
                print(x.tag)
                print(y.text)
        print("---")

       """

"""def xml_parser():
    object = ET.parse(
        "C:/Users/Fatih/Downloads/Compressed/TurkishWordNet-master/src/main/resources/turkish_wordnet.xml")
    source = object.getroot()
    for x in source[1].findall("DEF"):
        print("Kelimeler:", x.text)"""





