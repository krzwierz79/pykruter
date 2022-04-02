import pyexcel as p
import re


def open_txt(filename):
    with open(f"{filename}.txt", encoding="utf-8") as file:
        listed = [line for line in file.readlines()]
        # print(listed[:20])
    return [listed, filename]


def easy_find(what_where):
    qa_collection = []
    listed, filename = what_where
    # make new list elements for lines with "Q." append other lines
    for ln_num, line in enumerate(listed):
        # if "?" in line:  # if "?" and "."
        if "?" in line:
            qa_collection.append([line, ""])
        else:
            qa_collection[-1][1] += line

    # print(qa_collection[:4])
    p.save_as(array=qa_collection, dest_file_name=f"{filename}.xls")


def regex_find(what_where):
    qa_collection = []
    pattern = re.compile('^\d{1,2}\)', re.MULTILINE)
    listed, filename = what_where
    # make new list elements for lines with "Q." append other lines
    for ln_num, line in enumerate(listed):
        if re.match(pattern, line):
            qa_collection.append([line, ""])
        else:
            qa_collection[-1][1] += line

    # print(qa_collection[:4])
    p.save_as(array=qa_collection, dest_file_name=f"{filename}.xls")


# easy_find(open_txt('guru99'))
regex_find(open_txt('guru99'))
