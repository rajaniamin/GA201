def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

my_dictionary = {}

add_person(my_dictionary, "John", 25)
print(my_dictionary) 

update_age(my_dictionary, "John", 26)
print(my_dictionary) 

delete_person(my_dictionary, "John")
print(my_dictionary)
