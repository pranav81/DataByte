countries = {}

with open('countries.csv', 'r') as fin:

    for line in fin:
        a, b = line.strip()[:-3], line.strip()[-2:]
        countries[a] = b

countries.pop('Name,C')

code1 = input('Enter Country Code 1: ')
code2 = input('Enter Country Code 2: ')

country_list = []

for i,j in countries.items():
    if j == code1:
        name1 = i
    if j == code2:
        name2 = i
    country_list.append(i)

country_list.sort()

if name1<name2:
    sub_list = country_list[(country_list.index(name1) + 1):(country_list.index(name2))]

if name2<name1:
    sub_list = country_list[(country_list.index(name2) + 1):(country_list.index(name1))]

for i in sub_list:
    print(i)
