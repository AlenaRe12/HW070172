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

    # create zeros : two columns "month" and "searchTerm" (where all values are zeros)
    dfZeros = df[["month"]]
    dfZeros = dfZeros.reset_index()
    dfZeros[searchTerm] = 0
    dfZeros = dfZeros.drop_duplicates()

    # create a new table only with values that we want
    dfTemp = df[df.itemUnified.str.contains(searchTerm, na=False)]
    dfTemp = dfTemp[["month", "itemType"]]
    dfTemp = dfTemp.groupby(["month"]).count()
    dfTemp = dfTemp.reset_index()
    dfTemp[searchTerm] = dfTemp["itemType"]
    dfTemp = dfTemp[["month", searchTerm]]

    # merge with dfZeros (reason: we need explicit 0 values for dates when our search term is not found
    # otherwise the graph will be misleading as the line on the graph will be connecting only dates with
    # frequencies more than zero)
    dfTemp = dfTemp.append(dfZeros, ignore_index=True)
    dfTemp = dfTemp.groupby(["month"]).sum()
    dfTemp = dfTemp.sort_values(by="month")
    dfTemp = dfTemp.reset_index()

    # plotting the results
    plt.rcParams["figure.figsize"] = (20, 9)
    dfTemp.plot(x='month', y=searchTerm, legend=True, color='blue')

    plt.ylabel("absolute frequencies")
    plt.xlabel("dates (issues aggregated into months)")
    plt.title("entities with \"%s\" in them" % (searchTerm))
    plt.gca().yaxis.grid(linestyle=':')
    
    # the following line will simply open a pop-up with the graph
    # plt.show()

    # the following line will save the graph into a file
    fileNameToSave = "plot1_%s_%s.png" % (fileName, searchTerm)
    plt.savefig(fileNameToSave, dpi=300, bbox_inches="tight")
    plt.close("all")

searchDispatchData("shiloh", "shiloh")
