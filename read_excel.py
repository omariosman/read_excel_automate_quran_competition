import xlrd
import os

path = "file1.xlsx"

inputWorkbook = xlrd.open_workbook(path)

inputWorksheet = inputWorkbook.sheet_by_index(0)

i_base =  6
j_base = 0

no_students = inputWorksheet.cell_value(0,0)
print(no_students)
no_students = int(no_students)


all_hefz_lists = []
all_tagwid_lists = []

counter = 0

student_dict= {}

for student in range(no_students):
    hefz_list = []
    tagwid_list = []
    student_hefz_tagwid = []
    student_id = inputWorksheet.cell_value((i_base*student+5),0)
    for i in range(2):
        for j in range(6):
            cell_value = inputWorksheet.cell_value((i_base*student+6)+i,j+1)
            if (i == 0):
                hefz_list.append(cell_value*0.5)
            else:
                tagwid_list.append(cell_value*0.25)

            #print("i: ",(i_base*student+1)+i, "j: ", j+1)

    counter += 1
    all_hefz_lists.append(hefz_list)
    all_tagwid_lists.append(tagwid_list)
    student_hefz_tagwid.append(hefz_list)
    student_hefz_tagwid.append(tagwid_list)
    student_dict[student_id] = student_hefz_tagwid


print("=== Hefz ===")
for lst in all_hefz_lists:
    for i in lst:
        print(i)


print("=== Tagwid ===")
for lst in all_tagwid_lists:
    for i in lst:
        print(i)

for key, value in student_dict.items():
    print("id: ", key, "value: ", value)




