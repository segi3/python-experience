import csv

import xlwt
from xlwt import Workbook

mci1, mci2, mci3 = [], [], []

with open('survey-lbe.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if(row[3] == 'MCI'):
                tmp = {'NRP': row[1], 'Nama': row[2], 'Alasan': row[13]}
                mci1.append(tmp)
            elif(row[4] == 'MCI'):
                tmp = {'NRP': row[1], 'Nama': row[2], 'Alasan': row[14]}
                mci2.append(tmp)
            elif(row[5] == 'MCI'):
                tmp = {'NRP': row[1], 'Nama': row[2], 'Alasan': row[15]}
                mci3.append(tmp)
            line_count += 1

print(f'pilihan 1 MCI: {len(mci1)}')
for i in range(len(mci1)):
    print(mci1[i]['NRP'] +'-'+ mci1[i]['Nama']);

print(f'\npilihan 2 MCI: {len(mci2)}')
for i in range(len(mci2)):
    print(mci2[i]['NRP'] +'-'+ mci2[i]['Nama']);

print(f'\npilihan 3 MCI: {len(mci3)}')
for i in range(len(mci3)):
    print(mci3[i]['NRP'] +'-'+ mci3[i]['Nama']);

print(f'\ntotal pemilih MCI di 3 teratas: {len(mci1) + len(mci2) + len(mci3)}')
print(f'processed {line_count} lines')

wb = Workbook()

sheet1 = wb.add_sheet('Pilihan 1')

sheet1.write(0, 0, 'NRP')
sheet1.write(0, 1, 'Nama')
sheet1.write(0, 2, 'Nama')

for i in range(len(mci1)):
    sheet1.write(i+1, 0, mci1[i]['NRP'])
    sheet1.write(i+1, 1, mci1[i]['Nama'])
    sheet1.write(i+1, 2, mci1[i]['Alasan'])

sheet2 = wb.add_sheet('Pilihan 2')

sheet2.write(0, 0, 'NRP')
sheet2.write(0, 1, 'Nama')
sheet2.write(0, 2, 'Nama')

for i in range(len(mci2)):
    sheet2.write(i+1, 0, mci2[i]['NRP'])
    sheet2.write(i+1, 1, mci2[i]['Nama'])
    sheet2.write(i+1, 2, mci2[i]['Alasan'])

sheet3 = wb.add_sheet('Pilihan 3')

sheet3.write(0, 0, 'NRP')
sheet3.write(0, 1, 'Nama')
sheet3.write(0, 2, 'Nama')

for i in range(len(mci3)):
    sheet3.write(i+1, 0, mci3[i]['NRP'])
    sheet3.write(i+1, 1, mci3[i]['Nama'])
    sheet3.write(i+1, 2, mci3[i]['Alasan'])


wb.save('survey_lbe_mci.xls')

print("berhasil buat xls")
