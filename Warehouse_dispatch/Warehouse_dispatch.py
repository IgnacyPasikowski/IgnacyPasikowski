import re
import datetime

def create_invoice(supplier):
    with open("//dictionary_" + supplier + ".csv", encoding="utf8") as dictionary_file:
        dictionary_lines = dictionary_file.readlines()
        for line in dictionary_lines:
            line = line.strip().split(";")
            dictionary_result[line[0]] = line[2]
    for item in result:
        if item[0] in dictionary_result.keys():
            print(dictionary_result[item[0]], item[1].split(".")[0])
            output.write(dictionary_result[item[0]] + ";" + item[1].split(".")[0] + "\n")
        else:
            print(item[0] + " - not in dictionary\n")
            output.write(item[0] + " - not in dictionary\n")
    output.close()

now = datetime.datetime.now()
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%y")
date_string = str(day + "-" + month + "-" + year)

file_name = input("Drop the CSV file here\n")
file_name = file_name.replace("\"", "")
invoice_lines = open(file_name, encoding="utf8").readlines()
line_count = len(invoice_lines)
dictionary_result = {}
result = []
supplier = ""

with open(file_name, encoding="utf8") as invoice_file:
    invoice_text = invoice_file.read()

    if "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split("\t")
            if len(line) >= 3 and re.match("\d+", line[1].strip()) != re.match("\d+", "a"):
                result.append([line[1].strip(), line[2].strip()])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(";")
            if len(line) > 2 and ("Shippingcosts, Con VAT high" not in line or "13326" not in line):
                if "Unit(s)\"" == line[0]:
                    if (re.match("\d+", invoice_lines[i-1].strip().split(";")[0]) != re.match("\d+", "a")
                        and "g" not in invoice_lines[i-1].strip().split(";")[0]
                        and ("Shippingcosts, Con VAT high" not in invoice_lines[i-1] or "13326" not in invoice_lines[i-1])):
                        result.append([invoice_lines[i-1].strip().split(";")[0], invoice_lines[i-1].strip().split(";")[-1][1:]])
                    else:
                        if "Shippingcosts, Con VAT high" not in invoice_lines[i-1] or "13326" not in invoice_lines[i-1]:
                            result.append([invoice_lines[i-2].strip().split(";")[0], invoice_lines[i-1].strip().split(";")[-1][1:]])
                else:
                    if "Unit(s)" in line:
                        u = line.index("Unit(s)")
                        result.append([invoice_lines[i-1].strip().split(";")[0], invoice_lines[i-1].strip().split(";")[u]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if len(line) > 2 and ("Shippingcosts, Con VAT high" not in line or "13326" not in line):
                if "Unit(s)\"" == line[0]:
                    if (re.match("\d+", invoice_lines[i-1].strip().split(",")[0]) != re.match("\d+", "a")
                        and "g" not in invoice_lines[i-1].strip().split(",")[0]
                        and ("Shippingcosts, Con VAT high" not in invoice_lines[i-1] or "13326" not in invoice_lines[i-1])):
                        result.append([invoice_lines[i-1].strip().split(",")[0], invoice_lines[i-1].strip().split(",")[-1][1:]])
                    else:
                        if "Shippingcosts, Con VAT high" not in invoice_lines[i-1] or "13326" not in invoice_lines[i-1]:
                            result.append([invoice_lines[i-2].strip().split(",")[0], invoice_lines[i-1].strip().split(",")[-1][1:]])
                else:
                    if "Unit(s)" in line:
                        u = line.index("Unit(s)")
                        result.append([invoice_lines[i-1].strip().split(",")[0], invoice_lines[i-1].strip().split(",")[u]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if len(line) > 3 and re.match("\d+", line[0].strip()) != re.match("\d+", "a") and line[1].strip() != "":
                if line[1].strip() in ["FURY 2", "FURY EDGE", "FIERCE", "FURY EDGE & ROGUE"]:
                    result.append([line[1].strip(), line[2].strip()])

    elif "###" in invoice_text:
        supplier = "###"
        temp = []
        for i in range(line_count):
            line = invoice_lines[i].strip()
            if "SKU:" in line:
                temp.append(line.strip().split("SKU: ")[1])
            elif "\t" in line and re.match("^\d+", line):
                temp.append(line.strip().split("\t")[0].strip())
            if len(temp) == 2:
                result.append(temp)
                temp = []

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if re.match("\d+", line[0]) != re.match("\d+", "a"):
                if re.match("\d+\s", line[2]) != re.match("\d+", "a") and "54 22" not in line[2]:
                    result.append([line[2], line[0]])

    elif "###" in invoice_text:
        supplier = "###"
        temp = []
        for i in range(line_count):
            line = invoice_lines[i].strip().split(" ")
            if len(line) >= 5:
                if "(" in line[-1]:
                    temp.append(line[-1][1:-1])
                elif line[0] == "Quantity:":
                    temp.append(line[1])
                if len(temp) == 2:
                    result.append(temp)
                    temp = []

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split("\t")
            result.append([line[0], line[1]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if len(line) >= 15 and "TRANS.EX" not in line[0]:
                result.append([line[0], line[4][1:]])
            elif len(line) >= 11 and "TRANS.EX" not in line[0]:
                result.append([line[0], line[3][1:]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if re.match("\d+", line[0]) != re.match("\d+", "a") and " " in line[4]:
                result.append([line[1], line[0]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if len(line) >= 5:
                if re.match("\d+", line[2]) != re.match("\d+", "a"):
                    result.append([line[0], line[2]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].strip().split(",")
            if "PX-" in line[0]:
                result.append([line[0], line[1]])

    elif "###" in invoice_text:
        supplier = "###"
        for i in range(line_count):
            line = invoice_lines[i].replace("'", "")
            line = invoice_lines[i].strip().split(",")
            if re.match("\d+", line[0]) != re.match("\d+", "a"):
                if re.match("\d+", line[1]) != re.match("\d+", "a"):
                    result.append([line[2], line[0]])

output = open("output/" + supplier + " " + date_string + ".csv", "w+", encoding="utf8")
create_invoice(supplier)

input("Press enter to exit")
