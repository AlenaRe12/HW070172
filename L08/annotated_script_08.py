import re
# imports regular expressions library 
import os
#the os module in Python provides functions for interacting with the operating system. 
source = "./Dispatch/" # source folder
target = "./Dispatch_Processed/"  # target folder, needs to be created beforehand

lof = os.listdir(source)
# os.listdir() lists all files in that directory
counter = 0  # general counter to keep track of the progress

for f in lof:
    if f.startswith("dltext"):  # fileName test
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like

        issueVar = []
        with open(source + f, "r", encoding="utf8") as f1:
# opening the file. 
# "r" = open a file for reading
# utf8 encodes unicode characters. 
            text = f1.read()
            date = re.search(r'<date value="([\d-]+)"', text).group(1)
            split = re.split("<div3 ", text)
            # splitting the issue into articles/items at <div3

            for s in split[1:]:
                s = "<div3 " + s  # a step to restore the integrity of each item
# find the unitType
                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"
# find the header
                try:
                    header = re.search(r'<head.*</head>', s).group(0)
                    header = re.sub("<[^<]+>", "", header)

                except:
                    header = "NO HEADER"

                text = s
                text = re.sub("<[^<]+>", " ", text)
                text = re.sub(" +\n|\n +", "\n", text)
                text = text.strip()
                text = re.sub("\n+", ";;; ", text)
                text = re.sub(" +", " ", text)
                text = re.sub(r" ([\.,:;!])", r"\1", text)
# getting a clean text
                itemID = "ID: " + date + "_" + unitType + "_%03d" % c
                #generating necessary bits

                if len(re.sub("\W+", "", text)) != 0:
                    #creating a text variable
                    dateVar = "DATE: " + date
                    unitType = "TYPE: " + unitType
                    header = "HEADER: " + header
                    # @§@ is used to replace ":", because in YML : is used
                    # as a divider between the key and value
                    text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                    var = "\n".join([itemID, dateVar, unitType, header, text])

                    issueVar.append(var)
                    #append() method in python adds a single item to the existing lis

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)
            #saving

        counter += 1
        if counter % 100 == 0:
            print(counter)
            #counting processed issues and printing a progress counter at every 100 issues
