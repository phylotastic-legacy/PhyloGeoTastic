# Lampyr filter
""" Basic code to take the html output from Lampyr and produce the a list of
    just the species names. """

import urllib

def getLampyrDatafromAPI(lat, lon, commonOnly, nSpecies):
    """ get the data straight from Lampyr """
    if commonOnly:
        comstr = "no"
    else:
        comstr = "yes"
    page = urllib.URLopener().open("http://www.lampyr.org/app/getNClosestTaxonIDSpeciesCommon.php?lat={}&lon={}&submit=submit-value&common={}&N={}".format(lat,lon,comstr,nSpecies))
    dataStream = page.readlines()    
    return dataStream

def findSpeciesNames(dataList):
    """ filter the html output from Lampyr for species names """
    speciesList = []
    for line in dataList:
        if line.find("<a href=\"taxonInfo.php?") != -1:
            spName = line[line.find("<i>")+3:]
            spName = spName[:spName.find("<")]
            speciesList.append(spName)
    return speciesList    

def main():
    """ main loop """
    
    # sample parameters; the lat/lon represent Tucson
    lat = 32.222150
    lon = -110.926445
    commonOnly = False
    nSpecies = 50

    data = getLampyrDatafromAPI(lat,lon,commonOnly,nSpecies)
    species = findSpeciesNames(data)

    # test
    for s in species:
        print s

main()

""" to use more effectively,
    getLampyrDatafromAPI(lat,lon,commonOnly,nSpecies)
        this calls the Lampyr API with the specified inputs and returns
        a list containing the Lampyr output webpage as html
        lat and lon are the location to be serached, commonOnly is a boolean
        specifying whether to only include common names (for our purposes
        should probably always be False), and nSpecies is the number of
        species desired as output

    findSpeciesNames(data)
        this takes the list generated by the previous function and simply
        filters it for the species names, creating its own list just
        containing the names

    how we want to output the list from findSpeciesNames will depend on the
    precise usage

'""