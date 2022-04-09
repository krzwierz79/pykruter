# do markdownów
import pyexcel as p


def get_qa(file):
    with open(f"{file}.md", 'r', encoding="utf-8") as f:
        qa = []
        just_q = []
        category = ""
        for count, line in enumerate(f):
            # pytania bez odpowiedzi od ####
            if line.startswith('#### '):
                line.strip()
                just_q.append([line[8:]])
            # kategorie pytań
            elif line.startswith('###'):
                line.strip()
                category = line[4:]
                # print(category)
            # pytania
            elif line.startswith('## Q. '):
                line.strip()
                qa.append([line[6:], "", category])
            # pozostałe linie (odpowiedzi)
            else:
                qa[-1][1] += line
        # print(qa[:2])

        p.save_as(array=qa, dest_file_name=f"{file}.xlsx")
        p.save_as(array=just_q, dest_file_name=f"{file}_bez_odpowiedzi.xlsx")


get_qa('gh_learning-zone')
