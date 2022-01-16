import re
import os
import io
import pandas
import matplotlib.pyplot as plt

source = "C:\\Users\\rehde\\Desktop\\Dispatchhausaufgaben\\dispatchoriginal\\"
lof = os.listdir(source)

template = """
=================================================================================
= Plotting: %s (searching for: `\\b(%s)\\b`)
=================================================================================
"""


def searchDispatch(searchTermREGEX, searchTermPretty):
    print(template % (searchTermREGEX, searchTermPretty))

    counter = 0
    entities = []  # we will collect all extracted data here
    for f in lof:
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

                    try:
                        unitType = re.search(r'type="([^\"]+)"', s).group(1)
                    except:
                        unitType = "noType"

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

                    itemID = date + "_" + unitType + "_%03d" % c

                    if len(re.sub("\W+", "", text)) != 0:
                        itemIdvar = "ID: " + itemID
                        dateVar = "DATE: " + date
                        unitType = "TYPE: " + unitType
                        header = "HEADER: " + header
                        # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                        text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                        var = "\n".join(
                            [itemIdvar, dateVar, unitType, header, text])

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

    # reading our string of data into a pandas dataframe
    entitiesFinalStringIO = io.StringIO(entitiesFinal)
    df = pandas.read_csv(entitiesFinalStringIO, sep="\t", header=0)

    df["month"] = [re.sub("-\d\d$", "-01", str(i)) for i in df["date"]]
    df["month"] = pandas.to_datetime(df["month"], format="%Y-%m-%d")

    df = df[["month", searchTermPretty]]
    df = df.groupby(["month"]).sum()
    df = df.reset_index()

    # plot itself
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
