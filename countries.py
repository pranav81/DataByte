countries = {}

# Opening the data file and storing it as a dictionary

with open('countries.csv', 'r') as fin:

    for line in fin:
        a, b = line.strip()[:-3], line.strip()[-2:]
        countries[a] = b

# Residual data is also getting stored in the dictionary, we are deleting it

countries.pop('Name,C')

# Asking for 2 country codes as input

code1 = input('Enter Country Code 1: ')
code2 = input('Enter Country Code 2: ')

# Creating a list to store the country names in alphabetical order
# name1 and name2 are the countries received as input

country_list = []

for i,j in countries.items():
    if j == code1:
        name1 = i
    if j == code2:
        name2 = i
    country_list.append(i)

# Sorting the list by name

country_list.sort()

# Creating sub_list which contains names of all countries falling between name1 and name2

if name1<name2:
    sub_list = country_list[(country_list.index(name1) + 1):(country_list.index(name2))]

if name2<name1:
    sub_list = country_list[(country_list.index(name2) + 1):(country_list.index(name1))]

# Printing the required country names 

for i in sub_list:
    print(i)
