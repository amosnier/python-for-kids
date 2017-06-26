# List
lang_list = ['Python', 'C', 'C++', 'Java', 'Javascript']
print(lang_list)
print(lang_list[0], lang_list[1], lang_list[4])

# Change list item
lang_list[3] = 'C#'
print(lang_list)

# Print part of the list
print(lang_list[1:4])

# Mixed list
mixed_list = ['Why', 'was', 6, 'afraid', 'of', 7, '?', 'Because', 7, 8, 9]
print(mixed_list)

# List of lists
list_of_lists = [lang_list, mixed_list]
print(list_of_lists)

# Append to list
lang_list.append('Ada')
lang_list.append('Pascal')
lang_list.append('Smalltalk')
print(lang_list)

# Adding lists
sum_of_lists = lang_list + mixed_list
print(sum_of_lists)

# Multiplying lists
multiplied_list = lang_list * 3
print(multiplied_list)

# Other operations
#print(multiplied_list / 5)
#print(multiplied_list - 5)
#print(multiplied_list + 5)

# Tuple
lang_tuple = ('Python', 'C', 'C++', 'Java', 'Javascript')
print(lang_tuple)
#lang_tuple[3] = 'C#'

# Dictionary
favo_lang = {'Jack'  : 'Python',
             'John'  : 'C',
             'Dave'  : 'C++',
             'Jerry' : 'Java',
             'Bob'   : 'Javascript'}
print("Dave's favorite programming language is", favo_lang['Dave'])

# A Python dictionary can implement a real life dictionnary
dictionary = {'programming'       : 'act of writing computer instructions that do something useful',
              'computer'          : 'electronic machine capable of executing instructions and returning results',
              'programmer'        : 'person how programs a computer',
              'software engineer' :  'programmer with a fancy title'}
print("The definition of software engineer is:", dictionary['software engineer'])

# Addding dictionary entries
dictionary['new'] = 'something that did not exist before'
print('New means:', dictionary['new'])

# Changing dictionary entry
dictionary['software engineer'] = 'programmer who knows how to write programs that actually work'
print("The definition of software engineer is:", dictionary['software engineer'])
