import re

file = "C:\\Users\\rehde\\Desktop\\Dispatch\\ordner\\dltext@doc=Perseus%3Atext%3A2006.05.0004"

with open(file, "r", encoding="utf8") as f1:
    raw = f1.read()
    date = re.search(r'<date value="([-\d]+)"', raw).group(1)
    counter = 0
    for article in re.split("<div3", raw)[1:]:
        counter += 1
        articeID = date + "-" + str(counter)
        # Header
        try:
                    header = re.search(r'<head>(.*)</head>', s).group(1)
                    header = re.sub("<[^<]+>", "", header)
        except:
                    header = "NO HEADER"
        # next, process the main body of the article
        # next, extract the type of the article
        # try to find a unitType
        try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
        except:
                    unitType = "noType"
        # next, collect all variables into some general variable (list of dictionary)
    # convert all collected data into the format of your 
