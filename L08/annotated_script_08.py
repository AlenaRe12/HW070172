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

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)
            #creating the yml-versions of the issues and saving

        counter += 1
        if counter % 100 == 0:
            print(counter)
            #counting processed issues and printing a progress counter at every 100 issues
