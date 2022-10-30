def removeDuplicates(myList):
    # TODO
    for i in range(0,len(myList)):
        for j in range (i+1, len(myList)-1):
            if myList[i] == myList[j]:
                myList.pop(j)
    return myList


print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))