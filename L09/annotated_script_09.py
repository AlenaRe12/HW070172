import re # imports regular expressions library 

import os
#the os module in Python provides functions for interacting with the operating system. 

source = "C:\\Users\\rehde\\Desktop\\Dispatchhausaufgaben\\dispatchoriginal\\"
# source folder
target = "C:\\Users\\rehde\\Desktop\\Dispatchhausaufgaben\\dispatchnew2\\"
# target folder, needs to be created beforehand

lof = os.listdir(source)
counter = 0  # general counter to keep track of the progress

for f in lof:
    if f.startswith("dltext"):  # fileName test
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like
        #collect and count all XML tags

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

                itemID = "ID: " + date + "_" + unitType + "_%03d" % counter
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
                    #New Part for aggregating data into a tidy format
                    for i in re.findall(r"(<\w+[^>]+>)", s):
                        #re.findall()is used to search for “all” occurrences that match a given pattern
                        if "persName" in i and "authname" in i and "n=" in i:
                            # input(i)
                            itemType = "persName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)
                            # adding persname as itemType and connecting it to the matching ItemUnified ans itemID
                            
                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)   
                            
                        elif "placeName" in i and "authname" in i and "reg=" in i:
                            # input(i)
                            itemType = "placeName"
                            itemUnified = re.search(
                                r'reg="([^"]*)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)
                            #adding placename as itemType and connecting it to the matching ItemUnified ans itemID
                            
                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)
                            
                        elif "orgName" in i and "type" in i and "n=" in i:
                            # print(i)
                            itemType = "orgName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'type="([^"]+)"', i).group(1)
                            #adding orgname as itemType and connecting it to the matching ItemUnified ans itemID
                        
                            
                            entities = [itemID, date, itemType, itemUnified, itemId]

                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)  
                            
                        else:
                            pass

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)
        
        # count processed issues and print progress counter at every 100
        counter += 1  # counter = counter + 1
        # if counter is divisible by 100 (i.e., no remainder), then print it
        if counter % 100 == 0:
            print(counter)

header = "\t".join(["articleID", "date", "itemType", "itemUnified", "itemID"])
entitiesFinal = header + "\n" + "\n".join(entities).lower()
with open("entities.csv", "w", encoding="utf8") as f9:
    f9.write(entitiesFinal)
    # creating a final csv-file with all the data in tiny format

print("Done!")
