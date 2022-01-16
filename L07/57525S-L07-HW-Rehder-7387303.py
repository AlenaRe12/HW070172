import csv
import json


def converter_tsv_to_json(file):
    with open(file) as f1:
        reader = csv.DictReader(f1, delimiter="\t")
        settlements = {}
        for row in reader:
            settlements[row["settlement_id"]] = row
    with open(file.replace(".csv", ".json"), "w") as f9:
        json.dump(settlements, f9, indent=4, ensure_ascii=False)


def converter_tsv_to_yml(file):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read().strip().split("\n")
        header = data[0].split("\t")
        allData = []
        for d in data[1:]:
            temp = d.split("\t")
            tempVar = [temp[0]+":"]
            for i in range(0, len(header)):
                item = "\t%s: %s" % (header[i], temp[i])
                tempVar.append(item)
            tempVarFinal = "\n".join(tempVar)
            allData.append(tempVarFinal)
    ReallyFinalData = "\n\n".join(allData)
    with open(file.replace(".csv", ".yml"), "w", encoding="utf8") as f9:
        f9.write(ReallyFinalData)


def converter_tsv_to_xml(file):
    with open(file) as f1:
        reader = csv.DictReader(f1, delimiter="\t")
        data = []
        for row in reader:
            temp = []
            for k, v in row.items():
                temp.append("<%s>%s</%s>" % (k, v, k))
            tempComplete = "<settlement>\n\t%s\n</settlement>" % "\n\t".join(
                temp)
            data.append(tempComplete)
    ReallyFinalData = "\n\n".join(data)
    with open(file.replace(".csv", ".xml"), "w", encoding="utf8") as f9:
        f9.write(ReallyFinalData)


converter_tsv_to_json("settlements.csv")
converter_tsv_to_yml("settlements.csv")
converter_tsv_to_xml("settlements.csv")
