qa_collection = []

with open('dataflair.txt', encoding="utf-8") as file:
    listed = [line for line in file.readlines()]


# make new list elements for lines with "Q." append other lines
for ln_num, line in enumerate(listed):
    line.replace(";", ",")
    if "Q." in line:
        qa_collection.append(f"{line}\n;Ans: ")
    else:
        qa_collection[-1] += line

print(qa_collection[:2])


# # write to csv
# file = open('dataflair.csv', 'w', encoding="utf-8")
# lines = map(lambda line: line+'\n', qa_collection)
# file.writelines(lines)
# file.close()

# # print as strings (formatting)
# for num, el in enumerate(qa_collection):
#     qa = qa_collection[num]
#     print(str(qa))
