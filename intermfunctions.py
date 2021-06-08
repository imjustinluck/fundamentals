x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael','last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
print(x)

# 2
students[0]['last_name']="Bryant"
print(students)

# 3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# 4
z[0]['y']=30
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for item in students:
#         print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")

# iterateDictionary(students)

def iterateDictionary2(list, key):
    for item in list:
        print(item[key])

iterateDictionary2(students, "first_name")
iterateDictionary2(students, "last_name")



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dic, key):
    print(f"{len(dic[key])} {key.upper()}")
    for i in range (0, len(dic[key])):
        print(dic[key][i])

printInfo(dojo, 'instructors')
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
# Devon
