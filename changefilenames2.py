import os
import re
"""
Differences:
- Serial incrementally instead of by species 
- Doesn't rely on folder names 
- Use for MNHN RMCA UF SMF AMS
"""

class fileNameObject(object):
    def __init__(self, serial, species,collection):
        self.serial = serial
        self.species = species
        self.collection = collection

    def nameOfFile(self):
        return self.serial +"_"+ self.species + "_" + self.collection

def changeFolder(userdir, folder):
    # Going into each folder
    os.chdir(userdir)
    thisfolder = folder
    curr = os.getcwd()
    newpath = str(os.path.join(curr, thisfolder))
    os.chdir(newpath)

def renamePhotos():
    collectionregex = [r"(UF\s\d{5})", r"\d{4}\s(\d*)\s", r"(\d*R\d*)\s", r"^\d{4}(\s)[A-z][a-z]*\s[a-z]*",
                       r"\d{4}\s(\d*\.\d*)", r"MNHN.(\d*)", r"MNHN.RA.(\d*)", r"\s(R\d*)",r"(SMF\s\d*)"]

    speciesregex = [r"\d{4}\sUF\s\d*\s(.*)", r"^\d{4}\s\d*\s(.*)", r"\d{5}R\d{4}\s(.*)",
                    r"^\d{4}\s([A-Z][a-z]*\s[a-z]*)", r"\d*\.\d*\s(.*)", r"MNHN.\d*\s([A-Z][a-z].*)",
                    r"MNHN.RA.\d*.([A-Z].*)", r"\sR\d*\s(.*)",r"SMF\s\d*\s(.*)"]
    speciesindex = 0
    species = ""
    serial = 0
    filesinfolder = os.listdir()
    collection = ""

    for i in filesinfolder:
        serial +=1
        if len(i) > 4:
            indexofj = -1
            for j in collectionregex:
                indexofj += 1
                colmatch = re.search(j,i)
                if colmatch:
                    collection = colmatch.group(1)

                    speciesmatch = re.search(speciesregex[indexofj],i)
                    if speciesmatch:
                        species = speciesmatch.group(1)
                        if ".jpg" in species:
                            species = species[0:-4]

        newname = fileNameObject(str(serial).zfill(6), species,
                                 collection).nameOfFile()  # changed to 6 digital serial
        newname += ".jpg"
        #print(newname)
        os.rename(i, newname)


def main():
    # C:\Users\Jerry\Documents\VCU\BNFO 620 Bioinf Practicum\Images\MNHN RMCA UF photos
    userdir = r"C:\Users\Jerry\Documents\VCU\BNFO 620 Bioinf Practicum\Images\AMS_photos\AMS_photospractice"

    os.chdir(userdir)
    foldernames = os.listdir()

    for i in foldernames:
        changeFolder(userdir,i)
        renamePhotos()


if __name__ == '__main__':
    main()