import pyexcel as p
qa_collection = []

with open('docs_google.txt', encoding="utf-8") as file:
    listed = [line for line in file.readlines()]
    # print(listed[:20])


# make new list elements for lines with "Q." append other lines
for ln_num, line in enumerate(listed):
    if "?" in line:  # if "?" and "."
        # if "Q." in line:
        qa_collection.append([line, ""])
    else:
        qa_collection[-1][1] += line

print(qa_collection[:4])
p.save_as(array=qa_collection, dest_file_name="docs_google.xls")
