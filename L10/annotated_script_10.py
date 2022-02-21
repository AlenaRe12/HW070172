import re
# imports regular expressions library 
import os
#the os module in Python provides functions for interacting with the operating system. 
import io
#io module allows to manage the file-related input and output operations
import pandas
#Pandas = library of python used for data manipulation and analysis
import matplotlib.pyplot as plt
# module used for Generating visualizations

source = "./Dispatch/" # source folder
lof = os.listdir(source)
# os.listdir() lists all files in that directory


template = """
=================================================================================
= Plotting: %s (searching for: `\\b(%s)\\b`)
=================================================================================
"""
# loading template for visualizing the data

def searchDispatch(searchTermREGEX, searchTermPretty):
    print(template % (searchTermREGEX, searchTermPretty))
    # starting a new function to for analyzing the Dispatch-Issues and visualizing the data

    counter = 0
    entities = []  # we will collect all extracted data here
    or f in lof:
        counter += 1
        if counter % 100 == 0:
            print(counter)
                    # count processed issues and print progress counter at every 100

        if f.startswith("dltext"):  # fileName test
            # checks whether string starts with dltext
            newF = f.split(":")[-1] + ".yml"  # in fact, yml-like
                    # splits strings at ":"

            issueVar = []
            c = 0  # technical counter
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
                    c += 1
                    s = "<div3 " + s  # a step to restore the integrity of items
                    

                    try:
                        unitType = re.search(r'type="([^\"]+)"', s).group(1)
                    except:
                        unitType = "noType"                    
# finding the unitType by using regular expressions
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.

                    try:
                        header = re.search(r'<head.*</head>', s).group(0)
                        header = re.sub("<[^<]+>", "", header)
# find the header by using regular expressions

                    except:
                        header = "NO HEADER"
#getting a clean text
                    text = s # grab the text
                    text = re.sub("<[^<]+>", " ", text) 
                    text = re.sub(" +\n|\n +", "\n", text)
                    # clearing the text by using regular expressions               
                    text = text.strip()
                    # The strip() method removes characters from both left and right based on the argument 
                    text = re.sub("\n+", ";;; ", text)
                    text = re.sub(" +", " ", text)
                    text = re.sub(r" ([\.,:;!])", r"\1", text)
                    # clearing the text further by using regular expressions
                    itemID = date + "_" + unitType + "_%03d" % c
                    # creating the itemID
                    
#generating necessary bits

                     #creating a text variable
                    if len(re.sub("\W+", "", text)) != 0:
                        itemIdvar = "ID: " + itemID
                        dateVar = "DATE: " + date
                        unitType = "TYPE: " + unitType
                        header = "HEADER: " + header
                        # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                        text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                        var = "\n".join(
                            [itemIdvar, dateVar, unitType, header, text])
                        #creating a text variable out of the itemID, dateVar, unitTYPE, header and text


                        issueVar.append(var)
                         #append() method in python adds a single item (text variable) to the existing list (issueVar)

                        # NOW, WE CAN ADD SOME CODE TO PROCESS EACH ITEM AND COLLECT ALL INTO OUR TIDY DATA FORMAT
                        # STRUCTURE: itemID, dateVar, EXTRACTED_ITEM (type, unified_form, id)
                        # ADDING TO: entities (list)

                        results = re.findall(r"\b(%s)\b" %
                                             searchTermREGEX, text.lower())
                        #re.findall()is used to search for “all” occurrences that match a given pattern
                        matches = str(len(results))
                        #str() function converts values to a string form
                        # The len() function returns the length of the object. It returns total elements in an iterable or the number of chars in a string. In this case the matches are the number of results
                        tempVar = "\t".join([itemID, date, matches])
                        # creating a temporary variable out of itemID, date and matches
                        entities.append(tempVar)
                        # adding the variable to the entities-list
                        

    header = "\t".join(["itemID", "date", searchTermPretty])
    entitiesFinal = header + "\n" + "\n".join(entities)
    #creating a csv file with the results of the data-analysis
    with open("search_results_%s.csv" % searchTermPretty, "w", encoding="utf8") as f9:
        f9.write(entitiesFinal)
        #open the search result data

    # reading our string of data into a pandas dataframe
    entitiesFinalStringIO = io.StringIO(entitiesFinal)
    df = pandas.read_csv(entitiesFinalStringIO, sep="\t", header=0)

    df["month"] = [re.sub("-\d\d$", "-01", str(i)) for i in df["date"]]
    df["month"] = pandas.to_datetime(df["month"], format="%Y-%m-%d")
    #processing the data

    df = df[["month", searchTermPretty]]
    df = df.groupby(["month"]).sum()
    df = df.reset_index()
    # create a new table only with values that we want

    # plot the results
    plt.rcParams["figure.figsize"] = (20, 9)
    df.plot(x='month', y=searchTermPretty, legend=True, color='red')

    plt.ylabel("absolute frequencies")
    plt.xlabel("dates (issues aggregated into months)")
    plt.title("References to \"%s\" (regex: `\\b(%s)\\b`)" %
              (searchTermPretty, searchTermREGEX))
    plt.gca().yaxis.grid(linestyle=':')
    # creating the caption of the graph

    # the following line will save the graph into a file
    plt.savefig("plot_%s.png" % searchTermPretty, dpi=300, bbox_inches="tight")
    plt.close("all")
    print("Done!")

searchDispatch("deserters?|killed|wounded", "losses_at_war")
# searching the issues for those words
