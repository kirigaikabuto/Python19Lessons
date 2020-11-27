import json


def printData(data):
    for i in data:
        print(i)


def getMaxDataByParam(data, param):
    maxiUser = data[0]
    for i in data:
        if i[param] > maxiUser[param]:
            maxiUser = i
    return maxiUser


def getMinDataByParam(data, param):
    maxiUser = data[0]
    for i in data:
        if i[param] < maxiUser[param]:
            maxiUser = i
    return maxiUser


def getParamSum(data, param):
    sumi = 0
    for i in data:
        sumi += i[param]
    return sumi


def getDataFromJsonFile(fileName):
    file = open(fileName, "r")
    dataJson = file.read()
    data = json.loads(dataJson)
    return data


def saveDataToJsonFile(fileName, data):
    dataJson = json.dumps(data, indent=4)
    file = open(fileName, "w")
    file.write(dataJson)
    file.close()
