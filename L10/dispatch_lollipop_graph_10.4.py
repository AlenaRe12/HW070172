import re
import pandas
import matplotlib.pyplot as plt

template = """> Plotting data: %s"""

# load entities data
df = pandas.read_csv("entities.csv", sep="\t", header=0)
print(df)

def searchDispatchData(searchTerm, fileName="fromTagged"):
    print(template % (searchTerm))

    # processing our data
    df["month"] = [re.sub("-\d\d$", "-01", str(i)) for i in df["date"]]
    df["month"] = pandas.to_datetime(df["month"], format="%Y-%m-%d")

    # create a new table only with values that we want
    dfTemp = df[df.itemUnified.str.contains(searchTerm, na=False)]
    dfTemp = dfTemp[["month", "itemType"]]
    dfTemp = dfTemp.groupby(["month"]).count()
    dfTemp = dfTemp.reset_index()
    dfTemp[searchTerm] = dfTemp["itemType"]
    dfTemp = dfTemp[["month", searchTerm]]

    # plotting the results - lollipop
    plt.rcParams["figure.figsize"] = (20, 9)
    plt.stem(dfTemp['month'], dfTemp[searchTerm])

    plt.ylabel("absolute frequencies")
    plt.xlabel("dates (issues aggregated into months)")
    plt.title("entities with \"%s\" in them" % (searchTerm))
    plt.gca().yaxis.grid(linestyle=':')

    # the following line will save the graph into a file
    fileNameToSave = "plot1_lollipop_%s_%s.png" % (fileName, searchTerm)
    plt.savefig(fileNameToSave, dpi=300, bbox_inches="tight")
    plt.close("all")

searchDispatchData("shiloh", "shiloh")
