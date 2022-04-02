import pyexcel as p
import re

# otwiera plik i tworzy listę linii


def open_txt(filename):
    with open(f"{filename}.txt", encoding="utf-8") as file:
        listed = [line for line in file.readlines()]
        # print(listed[:20])
    return [listed, filename]  # zwraca treść pliku w liście i nazwę listy


# przeszukuje listę z treścią pliku z funkcji  powyżej i dzieli ją na pytania i odpowiedzi - wynik zapisuje do excela
def easy_find(what_where):
    qa_collection = []
    listed, filename = what_where
    # make new list elements for lines with "?" append other lines
    for ln_num, line in enumerate(listed):
        # if "?" in line:  # if "?" and "Q."
        if "?" in line:  # wyszukuje linie zawierające znak zapytania
            # i tworzy nową (zagnieżoną) listę 2. elementów line i "miejsce na odpowiedź"
            qa_collection.append([line, ""])
        else:
            # dodaje do ostatniej pozycji listy w "miejscu na odopowiedź" kolejne linie tekstu
            qa_collection[-1][1] += line
    # print(qa_collection[:4])
    # zapisuje wszystko do xls
    p.save_as(array=qa_collection, dest_file_name=f"{filename}.xls")

# dokładnie to samo co easy_find powyżej tylko że wyszukuje regexem '^\d{1,2}\)'
# na początku linii ^
# szuka 1 lub 2 {1,2} cyfr \d
# po których jest prawy nawias \)


def regex_find(what_where):
    qa_collection = []
    # unpack what_where
    listed, filename = what_where
    pattern = re.compile('^\d{1,2}\)', re.MULTILINE)
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
