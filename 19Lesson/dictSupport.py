def printUsers(data):
    for i in data:
        print(i["name"], i["salary"])


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
