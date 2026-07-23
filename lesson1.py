
#! When providing a file to the Python Interpreter, always put the path to the file in quotes

#* These are STATEMENTS. A statement is a complete instruction. They can be simple or complex
print('hello python')
print(23 - 5)

#* adding a line between statements for readbility
print('')

#* This line throws this error: SyntaxError: unterminated string literal
# print('Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more. I'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.')

#! The python interpreter will fail if it encounters an error. The file will not be executed at all

#* Adding three quotes fixes the error
print('''Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more. I'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.''')

print('')

#* New lines can be added to a string by using the escape sequence \n
print('''Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more.\nI'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.\n''')

#* Four spaces (tab) can be added to a string by using the escape sequence \t
print('The next word\tis four spaces away from the previous word.\n')

#* Variables are used to store data. They can be assigned values using the assignment operator
#* Variable names can contain letters, numbers, and underscores. They cannot start with a number. They are case-sensitive
lang = "python"

print(lang)
print('')

id = 100
name = 'Idris'

print(id, lang, name)
print('')

print('Language =',lang, '\nName =',name, '\nSuccess rate =',id)
print('')

#* Some data types
integer = 37
string = 'Violet'
float = 100.46
boolean = False
NoneType = None
list = [3.5, 19, 'World Cup', True]
tuple = (10, 20)
range = range(3, 36, 3)
dict = {'Idris': True}
set = {3, 9, 1}

#* type() function reads and prints the data type of a given variable
print(type(integer))
print(type(string))
print(type(100.46))
print(type(set))
print(type(dict))
print(type((3, 36, 3)))

#* String methods
print(len(name)) # print the length of a string
print(name.upper()) # convert the letters to uppercase
print(name.lower()) # convert the letters to lowercase
print(name.capitalize()) # convert the first letter of a string to a capital letter
print(name.title()) # convert the first letter of each word to a capital letter
print(name.replace('Idris', 'Saji')) # replace a given string (or part of a string) with a given replacement string
print(name[3:]) # slice off part of a string from the first character, determined by the number of characters given
print(name[:-3]) # slice off part of a string from the last character, determined by the negative number of characters given
print(name[3:-2]) # these methods can be combined
print(name.count('i')) # count how many times a substring appears in a given string
print(name.strip()) # remove spaces from the beginning and end of a string
print(name.lstrip()) # remove spaces from the beginning of a string
print(name.rstrip()) # remove spaces from the end of a string