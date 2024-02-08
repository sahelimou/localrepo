dictOfWords = {
    "hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 97,
    "here" : 53,
    "now" : 97
    }
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys
listOfKeys = getKeysByValue(dictOfWords, 43)
print("Keys with value equal to 43")
#Iterate over the list of keys
for key  in listOfKeys:
        print(key)
