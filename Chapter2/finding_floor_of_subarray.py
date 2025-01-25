def getMeanFloorOfSubarray():
    numberOfArrayElements, numberOfQueries = getElementsQueryCount()
    arrayElements = getArrayElementsFromUser()
    prefixSumArray = calculatePrefixSum(arrayElements)
    resultOfQueries = []
    for queries in range(numberOfQueries):
        arrayStartIndex, arrayEndIndex = getQueryUserInput()
        meanFloorValueOfSubarray = calculateMeanFloorOfSubarray(prefixSumArray, arrayStartIndex, arrayEndIndex)
        resultOfQueries.append(meanFloorValueOfSubarray)
    printingResult(resultOfQueries)

def getElementsQueryCount():
    return map(int, input().split())

def getArrayElementsFromUser():
    return list(map(int, input().split()))

def calculatePrefixSum(arrayElements):
    prefixSumArray = [0] * (len(arrayElements) + 1)
    for index in range(1, len(arrayElements) + 1):
        prefixSumArray[index] = prefixSumArray[index - 1] + arrayElements[index - 1]
    return prefixSumArray

def calculateSubarraySum(prefixSumArray, arrayStartIndex, arrayEndIndex):
    return prefixSumArray[arrayEndIndex] - prefixSumArray[arrayStartIndex - 1]

def getQueryUserInput():
    return tuple(map(int, input().split()))

def calculateMeanFloorOfSubarray(prefixSumArray, arrayStartIndex, arrayEndIndex):
    subarraySum = calculateSubarraySum(prefixSumArray, arrayStartIndex, arrayEndIndex)
    subarrayLength = arrayEndIndex - arrayStartIndex + 1
    return subarraySum // subarrayLength

def printingResult(resultOfQueries):
    print("\n".join(map(str, resultOfQueries)))

getMeanFloorOfSubarray()
