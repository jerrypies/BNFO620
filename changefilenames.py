__author__ = "Jeremy Nguyen"

import os
import re


class fileNameObject(object):
    def __init__(self, serial = "00000", species = "Default", collection = "12345"):
        self.serial = serial
        self.species = species
        self.collection = collection

    def nameOfFile(self):
        return self.serial + "_" + self.species + "_" + self.collection

def cleanUpSpeciesName(foldernames):
    #Some folders had " -- inch units" in the title. Cleaning up the list of species names to remove "-- inch units".
    incoming = foldernames
    newlist = []
    for i in incoming:
        if "--" in i:
            match = re.search(r"(.*) -- inch units",i)
            cleaned = match.group(1)

            newlist.append(cleaned)
        else:
            newlist.append(i)
    return newlist

def changeFolder(userdir, folder):
    # Going into each folder
    os.chdir(userdir)
    thisfolder = folder
    curr = os.getcwd()
    newpath = str(os.path.join(curr, thisfolder))
    os.chdir(newpath)

def renamePhotos(speciesindex,speciesnames):
    thisindex = speciesindex
    thisspecies = speciesnames
    thisfile = fileNameObject()
    filesinfolder = os.listdir()
    collection = parseCollection(filesinfolder)

    serialnum = 0

    for i in filesinfolder:
        serialnum += 1
        newname = fileNameObject(str(serialnum).zfill(5),thisspecies[thisindex],collection).nameOfFile()
        newname += ".jpg"
        os.rename(i,newname)

def parseCollection(filesinfolder):
    #Finding collection number and returning it as a string.
    filenames = filesinfolder
    matchstring = ""

    for i in filenames:
        match1 = None
        if "SMF" in i:
            match1 = re.search(r"(SMF \d{5})",i)
            if match1:
                matchstring = match1.group(1)
        elif "R" in i:
            match1 = re.search(r"(R\d{6})", i)
            if match1:
                matchstring = match1.group(1)

    return matchstring


def main():
    # C:\Users\Jerry\Documents\VCU\BNFO 620 Bioinf Practicum\Images\AMS_photos\AMS_photos
    # userdir = str(input(r"Enter directory/path of folder: "))
    userdir = r"C:\Users\Jerry\Documents\VCU\BNFO 620 Bioinf Practicum\Images\AMS_photos\AMS_photospractice"
    os.chdir(userdir)

    foldernames = os.listdir()

        #Dr. Uetz had named all his folders by species name. Getting all the species names from folders using listdir.
        #Prior to compiling this list, user should manually delete misc content in the directory.
    speciesnames = cleanUpSpeciesName(foldernames)
        #Some folder names had "-- inch units". Using this method to isolate species name.

    speciesindex = -1
    for i in foldernames:
        speciesindex += 1
        changeFolder(userdir,i)
        renamePhotos(speciesindex,speciesnames)



if __name__ == '__main__':
    main()