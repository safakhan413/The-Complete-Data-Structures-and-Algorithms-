import math
def firstSecond(givenList):
    # TODO
    max1 = -math.inf
    for i in range(0,len(givenList)):
        # for j in range(1,len(givenList))
        # max1 = givenList[i-1]
        # max2 = givenList[i-1]

        # max2 = 
        if givenList[i] > max1:
            max2 = max1
            max1 = givenList[i]
            
    return max1,max2

        
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(firstSecond(myList)) # 90 87