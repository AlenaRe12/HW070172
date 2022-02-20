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
        # checks whether string starts with dltext
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like
        # splits strings at ":"
        #collect and count all XML tags

        issueVar = []
        with open(source + f, "r", encoding="utf8") as f1:
# opening the file. 
# "r" = open a file for reading
# utf8 encodes unicode characters. 
            text = f1.read()
    #Read entire file
            date = re.search(r'<date value="([\d-]+)"', text).group(1)
        # search with regular expressions for the date values
            split = re.split("<div3 ", text)
            # splitting the issue into articles/items at <div3

            for s in split[1:]:
                s = "<div3 " + s 
                # a step to restore the integrity of each item
# find the unitType by using regular expressions
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"
                    
# find the header by using regular expressions
                try:
                    header = re.search(r'<head.*</head>', s).group(0)
                    header = re.sub("<[^<]+>", "", header)
                # The re. sub() function is used to replace occurrences of a particular sub-string with another sub-string

                except:
                    header = "NO HEADER"

                text = s
                text = re.sub("<[^<]+>", " ", text)
                text = re.sub(" +\n|\n +", "\n", text)
                # clearing the text by using regular expressions
                text = text.strip()
                # The strip() method removes characters from both left and right based on the argument 
                text = re.sub("\n+", ";;; ", text)
                text = re.sub(" +", " ", text)
                text = re.sub(r" ([\.,:;!])", r"\1", text)
                # clearing the text further by using regular expressions

                itemID = "ID: " + date + "_" + unitType + "_%03d" % c
                #generating necessary bits

                if len(re.sub("\W+", "", text)) != 0:
                    #creating a text variable by connecting the string "DATE: " to the respective date, the same for type and header
                    dateVar = "DATE: " + date
                    unitType = "TYPE: " + unitType
                    header = "HEADER: " + header
                   
                    text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                    var = "\n".join([itemID, dateVar, unitType, header, text])
                    # creating a text variable out of the itenID, dateVar, unitTYPE, header and text
                    # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                    
                    issueVar.append(var)
                    #append() method in python adds a single item to the existing list
                    
                    #New Part for aggregating data into a tidy format
                    for i in re.findall(r"(<\w+[^>]+>)", s):
                        #re.findall()is used to search for “all” occurrences that match a given pattern
                        if "persName" in i and "authname" in i and "n=" in i:
                            # input(i)
                            itemType = "persName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)
                            # adding persname as itemType and connecting it to the matching ItemUnified and itemID
                            
                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            # creating a temporary variable out of itemID, date, itemType, itemUnified, itemId
                            entities.append(tempVar)   
                            # adding the variable to the entities-list
                            
                        elif "placeName" in i and "authname" in i and "reg=" in i:
                            # input(i)
                            #The elif statement allows to check multiple expressions for TRUE and execute the block of code as soon as one of the conditions evaluates to TRUE
                            itemType = "placeName"
                            itemUnified = re.search(
                                r'reg="([^"]*)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)
                            #adding placename as itemType and connecting it to the matching ItemUnified and itemID
                            
                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            # creating a temporary variable out of itemID, date, itemType, itemUnified, itemId
                            entities.append(tempVar)
                            # adding the variable to the entities-list
                            
                        elif "orgName" in i and "type" in i and "n=" in i:
                            # print(i)
                            itemType = "orgName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'type="([^"]+)"', i).group(1)
                            #adding orgname as itemType and connecting it to the matching ItemUnified ans itemID
                        
                            
                            entities = [itemID, date, itemType, itemUnified, itemId]
                            # defining the list entities

                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                              # creating a temporary variable out of itemID, date, itemType, itemUnified, itemId
                            entities.append(tempVar)  
                            # adding the variable to the entities-list

                        else:
                            pass
                        #The pass statement is a null operation; nothing happens when it executes

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)
            # creating a new version of the issues and saving
        
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
