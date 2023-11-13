def createLinkList(locationList):
    X = []
    linkTemplate = "https://www.ffc.fr/clubs/?fwp_disciplines=route&fwp_club_region={}&fwp_club_activity=route"
    for element in locationList:
        X.append(linkTemplate.format(element))
    print(X)
    return X