def createLinkList(locationList):
    X = []
    linkTemplate = "https://velo.ffc.fr/liste-clubs/?discipline=route&activite=cyclisme-pour-tous&region={}"
    for element in locationList:
        X.append(linkTemplate.format(element))
    print(X)
    return X