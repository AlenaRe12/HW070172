import re

file = "C:\\Users\\rehde\\Desktop\\Dispatch\\ordner\\dltext@doc=Perseus%3Atext%3A2006.05.0004"

with open(file, "r", encoding="utf8") as f1:
    raw = f1.read()
    
    date = re.search(r'<date value="([-\d]+)"', raw).group(1)
    
    for article in re.split("<div3", raw)[1:]:
        counter += 1
        articleID = date + str(counter)
        input(articleID)
        header = re.search(r"<head>(.*)</head>", article).group(1)
        header = re.sub("<[^<]+>", "", header)
        input(header)
