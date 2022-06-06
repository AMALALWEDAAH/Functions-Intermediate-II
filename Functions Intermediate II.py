# 1 Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# 2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)
# 3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][2] = 'Andres'
print(sports_directory)
# 4 Change the value 20 in z to 30

z[0]['y'] = 30
print(z)
# 2 Iterate Through a List of Dictionaries


def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for k in some_list[x]:
            print(some_list[x][k])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonelcopy


# 3 Get Values From a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        for key, some_list in students[0].items():
            print(f"{key_name} : {some_list}")


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4 Iterate Through a Dictionary with List Values


def printInfo(some_dict):
    for key, some_list in some_dict.items():
        print("{}  {}".format(len(some_list), key.upper()))
        x = 0
        while x < len(some_list):
            print(some_list[x], "\n ")
            x = x+1


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devoncopy
