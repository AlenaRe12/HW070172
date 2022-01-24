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

    counter = 0
    entities = []  # we will collect all extracted data here
    or f in lof:
        counter += 1
        if counter % 100 == 0:
            print(counter)

        if f.startswith("dltext"):  # fileName test
            newF = f.split(":")[-1] + ".yml"  # in fact, yml-like

            issueVar = []
            c = 0  # technical counter
            with open(source + f, "r", encoding="utf8") as f1:
                text = f1.read()
                date = re.search(r'<date value="([\d-]+)"', text).group(1)
                split = re.split("<div3 ", text)

                for s in split[1:]:
                    c += 1
                    s = "<div3 " + s  # a step to restore the integrity of items
# finding unitType
                    try:
                        unitType = re.search(r'type="([^\"]+)"', s).group(1)
                    except:
                        unitType = "noType"
# finding Header
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
#getting a clean text
                    itemID = date + "_" + unitType + "_%03d" % c
#generating necessary bits

                    if len(re.sub("\W+", "", text)) != 0:
                        itemIdvar = "ID: " + itemID
                        dateVar = "DATE: " + date
                        unitType = "TYPE: " + unitType
                        header = "HEADER: " + header
                        # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                        text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                        var = "\n".join(
                            [itemIdvar, dateVar, unitType, header, text])
                        #creating a text variable


                        issueVar.append(var)

                        # NOW, WE CAN ADD SOME CODE TO PROCESS EACH ITEM AND COLLECT ALL INTO OUR TIDY DATA FORMAT
                        # STRUCTURE: itemID, dateVar, EXTRACTED_ITEM (type, unified_form, id)
                        # ADDING TO: entities (list)

                        results = re.findall(r"\b(%s)\b" %
                                             searchTermREGEX, text.lower())
                        matches = str(len(results))
                        tempVar = "\t".join([itemID, date, matches])
                        entities.append(tempVar)

    header = "\t".join(["itemID", "date", searchTermPretty])
    entitiesFinal = header + "\n" + "\n".join(entities)
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

    # the following line will save the graph into a file
    plt.savefig("plot_%s.png" % searchTermPretty, dpi=300, bbox_inches="tight")
    plt.close("all")
    print("Done!")

searchDispatch("deserters?|killed|wounded", "losses_at_war")
# searching the issues for those words
